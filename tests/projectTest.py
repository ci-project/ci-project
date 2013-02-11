import unittest
from google.appengine.ext import testbed
from project.models import Project

class TestProjectFunctions(unittest.TestCase):

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.kwargs = {'name' : 'test'}

    def test_init(self):
        self.project = Project.create(**self.kwargs)
        self.assertTrue(self.project.name == 'test')

    def tearDown(self):
        self.testbed.deactivate()

if __name__ == '__main__':
    unittest.main()