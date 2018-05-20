from testCase import TestCase
from wasRun import WasRun


class TestCaseTest(TestCase):
    def setUp(self):
        print("setup")

    def tearDown(self):
        print("tearDown")

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown " == test.log)


TestCaseTest("testTemplateMethod").run()
