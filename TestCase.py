from testResult import TestResult

class TestCase(object):
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def run(self):
        result = TestResult()
        result.testStarted()
        self.setUp()
        method = getattr(self, self.name)
        print ("Method tested:" + method.__name__)
        method()
        self.tearDown()
        return result

    def tearDown(self):
        pass
