import json
import tempfile
import threading
import unittest
from http.server import ThreadingHTTPServer
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import urlopen
from app.main import DEFAULTS, ENV_KEYS, app_port, make_handler, student_info


class StudentTests(unittest.TestCase):
    def test_defaults(self):
        self.assertEqual(student_info({}), DEFAULTS)

    def test_each_environment_variable(self):
        for field, env_key in ENV_KEYS.items():
            with self.subTest(field=field):
                actual = student_info({env_key: " custom-value "})
                self.assertEqual(actual[field], "custom-value")
                for other in DEFAULTS.keys() - {field}:
                    self.assertEqual(actual[other], DEFAULTS[other])

    def test_empty_environment_uses_defaults(self):
        self.assertEqual(student_info({key: " " for key in ENV_KEYS.values()}), DEFAULTS)

    def test_student_id_is_string(self):
        self.assertEqual(student_info({"STUDENT_ID": "0037773"})["student_id"], "0037773")

    def test_config_and_environment_port(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "app.conf"
            path.write_text("[application]\nport = 8123\n")
            self.assertEqual(app_port({"APP_CONFIG": str(path)}), 8123)
            self.assertEqual(app_port({"APP_CONFIG": str(path), "APP_PORT": "8124"}), 8124)

    def test_invalid_port_is_rejected(self):
        for port in ("0", "65536", "abc"):
            with self.subTest(port=port), self.assertRaises(ValueError):
                app_port({"APP_PORT": port})


class HTTPTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.student = student_info({"STUDENT_NAME": "Alisher <script>alert(1)</script>"})
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), make_handler(cls.student))
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=3)

    def test_health(self):
        with urlopen(self.base + "/health", timeout=3) as response:
            self.assertEqual(response.status, 200)
            self.assertEqual(response.read(), b"OK\n")

    def test_student_json(self):
        with urlopen(self.base + "/student", timeout=3) as response:
            self.assertEqual(response.headers.get_content_type(), "application/json")
            self.assertEqual(json.load(response), self.student)

    def test_home_escapes_html(self):
        with urlopen(self.base + "/", timeout=3) as response:
            page = response.read().decode()
            self.assertIn("&lt;script&gt;", page)
            self.assertNotIn("<script>alert(1)</script>", page)
            for key in ("surname", "group", "student_id"):
                self.assertIn(self.student[key], page)

    def test_unknown_path(self):
        with self.assertRaises(HTTPError) as caught:
            urlopen(self.base + "/missing", timeout=3)
        self.assertEqual(caught.exception.code, 404)


if __name__ == "__main__":
    unittest.main()
