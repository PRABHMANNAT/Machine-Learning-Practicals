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


if __name__ == "__main__":
    unittest.main()
