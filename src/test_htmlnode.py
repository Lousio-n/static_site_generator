import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_prop_to_html(self):
        node = HTMLNode("p", "this is a test", [], {
                        "href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(),
                         ' href="https://www.google.com"')

    def test_props_to_html(self):
        node = HTMLNode("p", "this is a test", [], {
            "href": "https://www.google.com", "target": "hello"})
        self.assertEqual(node.props_to_html(),
                         ' href="https://www.google.com" target="hello"')

    def test_html_values(self):
        node = HTMLNode("div", "this is a test")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "this is a test")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_html_repr(self):
        node = HTMLNode("p", "test test", None, {
            "href": "https://www.google.com"})
        self.assertEqual(
            "HTMLNode(p, test test, children: None, {'href': 'https://www.google.com'})", repr(node))

    def test_leaf_to_html(self):
        node = LeafNode("a", "test", {"href": "google.com", "class": "link"})
        self.assertEqual(
            node.to_html(), '<a href="google.com" class="link">test</a>')

    def test_leaf_value(self):
        node = LeafNode("p", "this is a paragraph")
        self.assertEqual(node.to_html(), '<p>this is a paragraph</p>')

    def test_no_tag(self):
        node = LeafNode(None, "this is raw text")
        self.assertEqual(node.to_html(), 'this is raw text')

    def test_parentnode(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(
        ), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test_nested_parent(self):
        node = ParentNode(
            "div",
            [
                ParentNode("p", [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                ]),
                LeafNode("button", "click!", {"class": "clicker"}),
            ],
            {"class": "main"}
        )
        self.assertEqual(node.to_html(
        ), '<div class="main"><p><b>Bold text</b>Normal text</p><button class="clicker">click!</button></div>')

    def test_parent_no_children(self):
        node = ParentNode("div", [], {"class": "box"})
        self.assertEqual(node.to_html(), '<div class="box"></div>')


if __name__ == "__main__":
    unittest.main()
