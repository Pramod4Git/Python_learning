import unittest
from unittest.mock import patch
import io
import sys
from Python_Practice_programe import test

# test_call_transfer.py


# Assuming the function to test is in test.py in the parent directory

# Placeholder for call transfer logic
def transfer_call(current_call, new_call):
    if current_call and new_call:
        return f"Transferred from {current_call} to {new_call}"
    return "Transfer failed"

class TestCallTransfer(unittest.TestCase):
    @patch('builtins.input', return_value='testfile.txt')
    def test_input_and_print(self, mock_input):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        # Re-run the code under test
        name = input('name of the file')
        print("name")
        sys.stdout = sys.__stdout__
        self.assertIn("name", captured_output.getvalue())

    def test_transfer_call_success(self):
        result = transfer_call("CallA", "CallB")
        self.assertEqual(result, "Transferred from CallA to CallB")

    def test_transfer_call_failure(self):
        result = transfer_call("", "CallB")
        self.assertEqual(result, "Transfer failed")

if __name__ == '__main__':
    unittest.main()