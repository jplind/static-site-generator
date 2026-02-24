import unittest
from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        target = "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"
        self.assertEqual(html, target)

    def test_headings(self):
        md = """
# This is a heading
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        target = "<div><h1>This is a heading</h1></div>"
        self.assertEqual(html, target)
    
    def test_ulist(self):
        md = """
- This is a ulist
- This is an item on the list
- This is another item on the list
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        target = "<div><ul><li>This is a ulist</li><li>This is an item on the list</li><li>This is another item on the list</li></ul></div>"
        self.assertEqual(html, target)
    
    def test_olist(self):
        md = """
1. This is an olist
2. This is an item on the list
3. This is another item on the list
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        target = "<div><ol><li>This is an olist</li><li>This is an item on the list</li><li>This is another item on the list</li></ol></div>"
        self.assertEqual(html, target)
    
    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        target = "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>"
        self.assertEqual(html, target)

if __name__ == "__main__":
    unittest.main()