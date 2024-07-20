import unittest

from htmlnode import HTMLNode


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

    def test_values(self):
        node = HTMLNode("div", "this is a test")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "this is a test")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode("p", "test test", None, {
            "href": "https://www.google.com"})
        self.assertEqual(
            "HTMLNode(p, test test, children: None, {'href': 'https://www.google.com'})", repr(node))


if __name__ == "__main__":
    unittest.main()
