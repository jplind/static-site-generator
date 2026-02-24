import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        href = "https://www.google.com"
        target = "_blank"
        node = HTMLNode("a", "some_text", None, {"href": href, "target": target})
        html = node.props_to_html()
        target = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(html, target)

if __name__ == "__main__":
    unittest.main()
