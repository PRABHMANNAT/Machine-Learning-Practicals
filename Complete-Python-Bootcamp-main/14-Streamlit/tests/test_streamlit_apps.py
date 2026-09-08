"""Offline smoke tests for every Streamlit learning app.

Streamlit's AppTest executes each file like a user session without opening a
browser or keeping a development server alive.
"""

from pathlib import Path
import unittest

from streamlit.testing.v1 import AppTest


ROOT = Path(__file__).resolve().parents[1]

APP_FILES = [
    ROOT / "app.py",
    ROOT / "widgets.py",
    ROOT / "classification.py",
    *sorted(path for path in (ROOT / "demos").glob("*.py") if path.name != "__init__.py"),
    *sorted((ROOT / "projects").glob("*.py")),
    ROOT / "multipage_app" / "Home.py",
    *sorted((ROOT / "multipage_app" / "pages").glob("*.py")),
]


class StreamlitAppsTest(unittest.TestCase):
    def test_every_app_renders_without_exception(self):
        failures = []
        for path in APP_FILES:
            with self.subTest(app=path.relative_to(ROOT)):
                app_test = AppTest.from_file(str(path)).run(timeout=30)
                if app_test.exception:
                    failures.append(
                        f"{path.relative_to(ROOT)}: "
                        + "; ".join(exception.message for exception in app_test.exception)
                    )
        self.assertEqual(failures, [], "\n".join(failures))

    def test_basic_app_has_expected_learning_elements(self):
        app_test = AppTest.from_file(str(ROOT / "app.py")).run(timeout=30)
        self.assertEqual(app_test.title[0].value, "Hello Streamlit")
        self.assertGreaterEqual(len(app_test.metric), 2)
        self.assertGreaterEqual(len(app_test.dataframe), 1)

    def test_session_counter_changes(self):
        app_test = AppTest.from_file(str(ROOT / "demos" / "04-session-state.py")).run(timeout=30)
        # Button order is −1, +1, Reset, Clear tasks.
        app_test.button[1].click().run(timeout=30)
        self.assertEqual(app_test.metric[0].value, "1")

    def test_new_classifier_projects_render_results(self):
        """Both beginner classifiers should show an answer on their first run."""
        for filename in ["dinosaur_classifier.py", "country_classifier.py"]:
            with self.subTest(project=filename):
                app_test = AppTest.from_file(str(ROOT / "projects" / filename)).run(timeout=30)
                self.assertGreaterEqual(len(app_test.success), 1)
                self.assertGreaterEqual(len(app_test.metric), 1)

    def test_new_topic_files_are_all_present(self):
        """Keep the requested learning catalogue from accidentally shrinking."""
        expected_topics = {
            "08-charts.py",
            "09-authentication.py",
            "10-connections.py",
            "11-images-and-video.py",
            "12-audio.py",
            "13-text.py",
            "14-maps.py",
            "15-dataframes.py",
            "16-graphs.py",
            "17-molecules-and-genes.py",
            "18-code-editors.py",
            "19-page-navigation.py",
            "20-developer-tools.py",
            "21-integrations.py",
            "22-llm-chat-component.py",
        }
        actual_topics = {path.name for path in (ROOT / "demos").glob("*.py")}
        self.assertTrue(expected_topics.issubset(actual_topics))

    def test_authentication_demo_can_log_in(self):
        """The pretend form should teach state by changing to signed-in UI."""
        app_test = AppTest.from_file(str(ROOT / "demos" / "09-authentication.py")).run(timeout=30)
        app_test.text_input[0].set_value("Asha")
        app_test.text_input[1].set_value("practice-password")
        app_test.button[0].click().run(timeout=30)
        self.assertEqual(app_test.success[0].value, "Hello, Asha!")
        self.assertEqual(app_test.metric[0].value, "Signed in")

    def test_llm_demo_remembers_a_local_reply(self):
        """Submitting chat text should append user and assistant messages."""
        app_test = AppTest.from_file(str(ROOT / "demos" / "22-llm-chat-component.py")).run(timeout=30)
        app_test.chat_input[0].set_value("Tell me about dinosaurs").run(timeout=30)
        self.assertEqual(len(app_test.chat_message), 3)
        self.assertIn("Dinosaurs", app_test.chat_message[2].markdown[0].value)

    def test_installed_chat_component_can_be_selected(self):
        """The requested third-party chat renderer should load without errors."""
        app_test = AppTest.from_file(str(ROOT / "demos" / "22-llm-chat-component.py")).run(timeout=30)
        self.assertFalse(app_test.checkbox[0].disabled)
        app_test.checkbox[0].set_value(True).run(timeout=30)
        self.assertEqual(list(app_test.exception), [])


if __name__ == "__main__":
    unittest.main()
