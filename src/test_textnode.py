import unittest

from textnode import Textnode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = Textnode("this is a textnode", "bold")
        node2 = Textnode("this is a textnode", "bold")
        self.assertEqual(node, node2)

    def test_url(self):
        node = Textnode("this is a textnode", "link", "https://url.com")
        node2 = Textnode("this is a textnode", "link", "https://url.com")
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = Textnode("this is a textnode", "bold")
        self.assertEqual(node.url, None)

    def test_not_eq_text(self):
        node = Textnode("this is a textnode", "bold")
        node2 = Textnode("this is different", "bold")
        self.assertNotEquals(node.text, node2.text)

    def test_not_eq_text_type(self):
        node = Textnode("this is a textnode", "bold")
        node2 = Textnode("this is a textnode", "italic")
        self.assertNotEquals(node.text_type, node2.text_type)


if __name__ == "__main__":
    unittest.main()
