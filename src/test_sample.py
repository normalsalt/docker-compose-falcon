from falcon import testing
import sample

class MyTestCase(testing.TestCase):
    def setUp(self):
        super(MyTestCase, self).setUp()
        self.app = sample.api

class TestSample(MyTestCase):
    def test_get_message(self):
        doc = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
                ),
            'author': 'Grace Hopper'
        }
        result = self.simulate_get('/quote')
        self.assertEqual(result.json, doc)
