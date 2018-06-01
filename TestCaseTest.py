from testCase import TestCase
from wasRun import WasRun
from testResult import TestResult


class TestCaseTest(TestCase):
    def setUp(self):
        print("setup")

    def tearDown(self):
        print("tearDown")

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown " == test.log)

    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert("1 run, 0 failed" == result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert("1 run, 1 failed" == result.summary())

    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed" == result.summary())


TestCaseTest("testFailedResult").run()
TestCaseTest("testFailedResultFormatting").run()
