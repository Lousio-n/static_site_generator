from textnode import Textnode
from htmlnode import HTMLNode, LeafNode


def main():
    node = Textnode("this is a test", "bold", "google.se")
    print(node)
    html = HTMLNode("p", "this is a test", [], {
                    "href": "https://www.google.com"})
    print(html.props_to_html())

    leafnode = LeafNode("a", "test", {"href": "google.com"})
    print(leafnode)


main()
