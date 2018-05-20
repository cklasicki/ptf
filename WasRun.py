from TestCase import TestCase

class WasRun(TestCase):
    
    def __init__(self, name):
        self.wasRun = None
        self.wasSetUp = 1
        TestCase.__init__(self, name)
    
    def testMethod(self):
        self.wasRun = 1
    
    def run(self):
        method = getattr(self, self.name)
        method()

    def setUp(self):
        self.wasSetUp = 1