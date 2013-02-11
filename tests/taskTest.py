import unittest
from google.appengine.ext import testbed
from project.models import Project, Task

class TestTaskFunctions(unittest.TestCase):

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.projkwargs = {'name' : 'test'}
        self.project = Project.create(**self.projkwargs)
        self.kwargs = {'parent' : self.project, 
                       'title' : 'test', 
                       'description' : 'desctest', 
                       'notes' : []}

    def test_init(self):
        self.task = Task.create(**self.kwargs)
        self.assertTrue(self.task.title == 'test')
        
    def test_findAllFor(self):
        self.task = Task.create(**self.kwargs)
        self.tasks = Task.findAllFor(self.project)
        self.assertTrue(len(self.tasks) == 1)
        
    def tearDown(self):
        self.testbed.deactivate()

if __name__ == '__main__':
    unittest.main()