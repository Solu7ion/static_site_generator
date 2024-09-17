import unittest
from main import (
    extract_title
)

class TestMainToHtml(unittest.TestCase):
    def test_extract_title(self):
        markdown = ("# Hello world!")
        self.assertEqual(extract_title(markdown), "Hello world!")
