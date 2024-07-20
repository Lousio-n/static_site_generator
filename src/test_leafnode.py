import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("a", "test", {"href": "google.com"})
        self.assertEqual(node.to_html(), '<a href="google.com">test</a>')
