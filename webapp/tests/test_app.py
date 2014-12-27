import unittest
import webtest


class TestApp(unittest.TestCase):

    def test_it(self):
        from webob import Response
        app = Response("Hello")
        app = webtest.TestApp(app)
        res = app.get("/")
        self.assertEqual(res.text, "Hello")
