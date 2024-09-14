import unittest 
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(tag="a", value="Click here", props={"class": "display", "href": "https://www.google.com"}) 
        self.assertEqual(node.props_to_html(), ' class="display" href="https://www.google.com"')

    def test_values(self):
        node = HTMLNode(
            "div",
            "I check values div"
        )
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "I check values div")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode(
            "div",
            "Check test_repr return",
            None,
            {"class": "inner"}
        )
        self.assertEqual(node.__repr__(), "HTMLNode(div, Check test_repr return, children: None, {'class': 'inner'})")

class LeafNode(HTMLNode):
    def test_to_html(self):
        node = LeafNode(tag="p", value="This is a paragraph of text.")
        self.assertEqual('<p>This is a paragraph of text.</p>')
    
    def test_to_html_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual('<a href="https://www.google.com">Click me!</a>')
