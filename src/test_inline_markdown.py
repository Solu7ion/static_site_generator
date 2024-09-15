import unittest
from inline_markdown import (
    split_nodes_delimiter
)
from textnode  import TextNode

class TestMarkdownParser(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        text_type_text = "text"
        text_type_code = "code"

        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)

        expected_output = [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text),
        ]
        
        self.assertEqual(new_nodes, expected_output)

