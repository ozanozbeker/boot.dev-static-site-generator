import unittest

from htmlnode import HTMLNode, HTMLTag


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode(HTMLTag.HEADING_1, "This is a header 1")
        node2 = HTMLNode(HTMLTag.HEADING_1, "This is a header 1")
        self.assertEqual(node1, node2)

    def test_not_eq(self):
        node1 = HTMLNode(HTMLTag.HEADING_1, "This is a header 1")
        node2 = HTMLNode(HTMLTag.HEADING_2, "This is a header 2")
        self.assertNotEqual(node1, node2)

    def test_empty_node(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_props_to_html_basic(self):
        node = HTMLNode(
            tag=HTMLTag.LINK, value="Google", props={"href": "https://www.google.com"}
        )
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_multiple_attrs(self):
        node = HTMLNode(
            tag=HTMLTag.LINK,
            value="Example",
            props={"href": "https://example.com", "target": "_blank"},
        )
        html = node.props_to_html()
        self.assertIn('href="https://example.com"', html)
        self.assertIn('target="_blank"', html)
        self.assertTrue(html.startswith(" "))  # ensure leading space


if __name__ == "__main__":
    unittest.main()
