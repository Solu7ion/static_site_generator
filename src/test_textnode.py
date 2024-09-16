import unittest

from textnode import (
    TextNode,
    text_node_to_html_node,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold",)
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)


class TestTextNodeToHtmlNode(unittest.TestCase):

    def test_type_text(self):
        node = TextNode("This is a text node", text_type_text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_type_image(self):
        node = TextNode("This is image", text_type_image, "https://img.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props,  {"src": "https://img.com", "alt": "This is image"}, )

if __name__ == "__main__":
    unittest.main()
