import sys
import unittest
import os

def main():
    sys.path.append(os.path.dirname(os.getcwd()))
    sys.path.append('fdffdf/opt/google/gae_python_sdk/1.7.latest')
    import dev_appserver
    dev_appserver.fix_sys_path()

    suite = unittest.TestLoader().discover('.')
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful():
        sys.exit(1)

    sys.exit(0)

if __name__ == '__main__':
    main()