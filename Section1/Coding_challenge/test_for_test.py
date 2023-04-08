from test_ import TestFib
import test_
import unittest

def setUpModule():
    print('setUpModule')

def tearDownModule():
    print('tearDownModule')


if __name__ == '__main__':
    test_.setUpModule = setUpModule
    test_.tearDownModule = tearDownModule
    Loaded_Suite = unittest.TestLoader().loadTestsFromTestCase(TestFib)
    suite = unittest.TestSuite([Loaded_Suite])
    unittest.TextTestRunner().run(suite)
