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
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestFib)
    suite = unittest.TestSuite([suite1])
    unittest.TextTestRunner().run(suite)
