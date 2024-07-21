import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("a", "test", {"href": "google.com", "class": "link"})
        self.assertEqual(
            node.to_html(), '<a href="google.com" class="link">test</a>')

    def test_value(self):
        node = LeafNode("p", "this is a paragraph")
        self.assertEqual(node.to_html(), '<p>this is a paragraph</p>')

    def test_no_tag(self):
        node = LeafNode(None, "this is raw text")
        self.assertEqual(node.to_html(), 'this is raw text')
