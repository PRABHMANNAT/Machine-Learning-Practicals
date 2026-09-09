"""Small test-client suite showing how Flask apps can be tested without a server."""

from pathlib import Path
import sqlite3
import sys
from tempfile import TemporaryDirectory
import unittest


FLASK_FOLDER = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FLASK_FOLDER))

import api
import app as hello_app
import getpost
import jinja
import main
from demos import database_crud, form_calculator, multi_page, responses_errors, sessions_auth
from demos.blueprint_app import create_app as create_blueprint_app


class FlaskExamplesTest(unittest.TestCase):
    def test_original_learning_apps(self):
        self.assertEqual(hello_app.app.test_client().get("/").status_code, 200)
        self.assertEqual(main.app.test_client().get("/index").status_code, 200)
        form_client = getpost.app.test_client()
        self.assertEqual(form_client.get("/form").status_code, 200)
        self.assertEqual(form_client.post("/submit", data={"name": "Asha"}).status_code, 200)
        jinja_client = jinja.app.test_client()
        self.assertEqual(jinja_client.get("/success/75").status_code, 200)
        self.assertEqual(jinja_client.get("/successres/75.0").status_code, 200)
        self.assertEqual(jinja_client.get("/submit").status_code, 200)
        response = jinja_client.post(
            "/submit",
            data={"science": "80", "maths": "70", "c": "60", "datascience": "90"},
        )
        self.assertEqual(response.status_code, 302)

    def test_json_api_crud(self):
        api.items[:] = [item.copy() for item in api.INITIAL_ITEMS]
        client = api.app.test_client()
        created = client.post("/items", json={"name": "Learn Flask", "description": "Practice"})
        self.assertEqual(created.status_code, 201)
        item_id = created.get_json()["id"]
        self.assertEqual(client.get(f"/items/{item_id}").status_code, 200)
        self.assertEqual(client.delete(f"/items/{item_id}").status_code, 204)

    def test_new_page_form_session_and_blueprint_demos(self):
        self.assertEqual(multi_page.app.test_client().get("/hello/Asha?language=Hindi").status_code, 200)
        calculator_response = form_calculator.app.test_client().post(
            "/",
            data={"left": "8", "right": "2", "operation": "divide"},
            follow_redirects=True,
        )
        self.assertEqual(calculator_response.status_code, 200)
        self.assertIn(b"= 4.0", calculator_response.data)
        response_client = responses_errors.app.test_client()
        self.assertEqual(response_client.get("/").status_code, 200)
        self.assertEqual(response_client.get("/missing").status_code, 404)

        auth_client = sessions_auth.app.test_client()
        login = auth_client.post("/login", data={"username": "learner", "password": "flask123"})
        self.assertEqual(login.status_code, 302)
        self.assertEqual(auth_client.get("/dashboard").status_code, 200)

        blueprint_client = create_blueprint_app({"TESTING": True}).test_client()
        self.assertEqual(blueprint_client.get("/api/health").get_json(), {"status": "ok"})

    def test_database_crud_with_temporary_database(self):
        with TemporaryDirectory() as directory:
            database_path = Path(directory) / "test.sqlite3"
            app = database_crud.create_app({"TESTING": True, "DATABASE": str(database_path)})
            client = app.test_client()
            self.assertEqual(client.post("/create", data={"title": "Test task"}).status_code, 302)
            page = client.get("/")
            self.assertIn(b"Test task", page.data)
            connection = sqlite3.connect(database_path)
            try:
                task_id = connection.execute("SELECT id FROM tasks").fetchone()[0]
            finally:
                connection.close()
            self.assertEqual(client.post(f"/delete/{task_id}").status_code, 302)


if __name__ == "__main__":
    unittest.main()
