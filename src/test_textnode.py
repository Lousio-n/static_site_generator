import unittest

from textnode import (
    Textnode,
    text_type_bold,
    text_type_code,
    text_type_link,
    text_type_text,
    text_type_image,
    text_type_italic,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = Textnode("this is a textnode", text_type_bold)
        node2 = Textnode("this is a textnode", text_type_bold)
        self.assertEqual(node, node2)

    def test_url(self):
        node = Textnode("this is a textnode",
                        text_type_link, "https://url.com")
        node2 = Textnode("this is a textnode",
                         text_type_link, "https://url.com")
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = Textnode("this is a textnode", text_type_italic)
        self.assertEqual(node.url, None)

    def test_not_eq_text(self):
        node = Textnode("this is a textnode", text_type_text)
        node2 = Textnode("this is different", text_type_text)
        self.assertNotEqual(node, node2)

    def test_not_eq_text_type(self):
        node = Textnode("this is a textnode", text_type_bold)
        node2 = Textnode("this is a textnode", text_type_italic)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = Textnode("this is a textnode",
                        text_type_link, "https://url.com")
        self.assertEqual(
            "Textnode(this is a textnode, link, https://url.com)", repr(node))


if __name__ == "__main__":
    unittest.main()
