# tests/test_wsgi.py
from flask_testing import TestCase
from application import application


class TestViews(TestCase):
    def create_app(self):
        application.config['TESTING'] = True
        return application

    def test_one_roll(self):
        quote = self.client.get('/quote').json['quote']
        self.assertEqual(type(quote), str)
        self.assertGreater(len(quote), 0)

