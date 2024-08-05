import unittest

from split_nodes import split_nodes_delimiter
from textnode import Textnode, text_type_bold, text_type_code, text_type_italic, text_type_text


class test_split_nodes(unittest.TestCase):
    def test_code_blocks(self):
        node = Textnode("this is a test for `code blocks`", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(new_nodes, [Textnode(
            "this is a test for ", text_type_text), Textnode("code blocks", text_type_code)])

    def test_bold(self):
        node = Textnode("this is a test for **bold text**", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertEqual(new_nodes, [Textnode(
            "this is a test for ", text_type_text), Textnode("bold text", text_type_bold)])

    def test_non_text_type_text(self):
        node = Textnode("this is code", text_type_code)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(new_nodes, [Textnode("this is code", text_type_code)])

    def test_multiple_parts_with_deliminator(self):
        node = Textnode("text *italic* text *italic*", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertEqual(new_nodes, [Textnode("text ", text_type_text), Textnode(
            "italic", text_type_italic), Textnode(" text ", text_type_text), Textnode("italic", text_type_italic)])

    def test_bold_and_italic(self):
        node = Textnode("**bold** and *italic*", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
        self.assertEqual(new_nodes, [Textnode("bold", text_type_bold), Textnode(
            " and ", text_type_text), Textnode("italic", text_type_italic)])


if __name__ == "__main__":
    unittest.main()
