import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_prop_to_html(self):
        node = HTMLNode("p", "this is a test", [], {
                        "href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(),
                         ' href="https://www.google.com" ')

    def test_props_to_html(self):
        node = HTMLNode("p", "this is a test", [], {
            "href": "https://www.google.com", "target": "hello"})
        self.assertEqual(node.props_to_html(),
                         ' href="https://www.google.com" target="hello" ')

    def test_props_none(self):
        node = HTMLNode("a", "test")
        self.assertEqual(node.props_to_html(), None)

    def test_repr(self):
        node = HTMLNode("p", "test test", ["a", "b", "c"], {
            "href": "https://www.google.com"})
        self.assertEqual(
            "HTMLNode(p, test test, ['a', 'b', 'c'], {'href': 'https://www.google.com'})", repr(node))
