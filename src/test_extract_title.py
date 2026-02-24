import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = """
This is some text
#      Here is a title        
Here is some more text
"""
        title = extract_title(md)
        target = "Here is a title"
        self.assertEqual(title, target)

if __name__ == "__main__":
    unittest.main()