import unittest

from textnode import (
    Textnode,
    text_node_to_html_node,
    text_type_bold,
    text_type_code,
    text_type_link,
    text_type_text,
    text_type_image,
    text_type_italic,
)

from htmlnode import LeafNode


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


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text(self):
        node = Textnode("this is a textnode", text_type_text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "this is a textnode")

    def test_image(self):
        node = Textnode("image", text_type_image, "https://image.test")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {
                         "src": "https://image.test", "alt": "image"})

    def test_text_to_html(self):
        node = Textnode("this is a textnode", text_type_bold)
        self.assertEqual("LeafNode(b, this is a textnode, None)",
                         repr(text_node_to_html_node(node)))

    def test_textnode_with_url(self):
        node = Textnode("test",
                        text_type_link, "https://url.com")
        self.assertEqual(text_node_to_html_node(node).to_html(),
                         '<a href="https://url.com">test</a>')


if __name__ == "__main__":
    unittest.main()
