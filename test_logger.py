import unittest
from logger import Logger

class TestLogger(unittest.TestCase):

    def setUp(self):
        self.logger = Logger()

    def test_log_adds_message(self):
        message = "Test log message"
        entry = self.logger.log(message)
        self.assertIn(message, entry)
        self.assertEqual(len(self.logger.get_logs()), 1)

    def test_multiple_logs(self):
        self.logger.log("First")
        self.logger.log("Second")
        logs = self.logger.get_logs()
        self.assertEqual(len(logs), 2)
        self.assertIn("First", logs[0])
        self.assertIn("Second", logs[1])

if __name__ == '__main__':
    unittest.main()
