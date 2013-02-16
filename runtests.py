import sys
import unittest
from tests import projectTest, taskTest

def main():
    sys.path.insert(0, 'google_appengine')
    import dev_appserver
    dev_appserver.fix_sys_path()
    
    suite = unittest.TestLoader().loadTestsFromTestCase(projectTest.TestProjectFunctions)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful():
        sys.exit(0)
    
    suite = unittest.TestLoader().loadTestsFromTestCase(taskTest.TestTaskFunctions)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful():
        sys.exit(0)

    sys.exit(1)

if __name__ == '__main__':
    main()