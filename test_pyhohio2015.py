import pyohio2015

class TestPyohio2015(unittest.TestCase):

    def setUp(self):
        self.hello_message = "Hello, PyOhio!"

    def test_prints_hello_pyohio(self):
        output = pyohio2015.hello()
        assert(output == self.hello_message)
