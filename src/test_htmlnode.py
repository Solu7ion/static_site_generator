import unittest 
from htmlnode import HTMLNode, LeafNode, ParentNode

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
    
    def test_to_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_to_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
        
    # test for children     
    def test_to_many_children(self):
        node = ParentNode("p", [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "Italic text"),
            LeafNode(None, "Normal text")
        ],)
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>")
    
    def test_to_html_heading(self):
        heading = ParentNode("h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text")
            ]
        )
        self.assertEqual(heading.to_html(), "<h2><b>Bold text</b>Normal text<i>Italic text</i>Normal text</h2>")

    def test_to_html_with_children(self):
        child_node = LeafNode("b", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><b>child</b></div>")

    def test_to_html_with_grandchildren(self):
        grand_node = LeafNode("i", "grandchild")
        child_node = ParentNode("p", [grand_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><p><i>grandchild</i></p></div>")
