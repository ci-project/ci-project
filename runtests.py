import sys
import unittest
import os
from os.path import expanduser

def main():
    sys.path.append(os.path.dirname(os.getcwd()))
    home = expanduser("~")
    sys.path.append(home+'/google_appengine')
    import dev_appserver
    dev_appserver.fix_sys_path()

    suite = unittest.TestLoader().discover('.')
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful():
        sys.exit(1)

    sys.exit(0)

if __name__ == '__main__':
    main()