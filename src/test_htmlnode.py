import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "french fries and the accident of 2025", props={"href": "https://www.google.com", "target": "_blank",})
        node2 = HTMLNode("p", "french fries and the accident of 2025", props={"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node, node2)
    def test_props_to_html(self):
        node = HTMLNode("p", "french fries and the accident of 2025", props={"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')
    def test_props_to_html_empty(self):
        node = HTMLNode("p", "french fries and the accident of 2025")
        self.assertEqual(node.props_to_html(), "")
    def test_values(self):
        node = HTMLNode("p", "div")
        node2 = HTMLNode(value="testing node")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node2.tag, None)
        self.assertEqual(node2.value, "testing node")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("a", "the shining and blinding sunset")
        node2 = LeafNode("a", "the shining and blinding sunset")
        self.assertEqual(node, node2)

    def test_check_for_no_children(self):
        node = LeafNode("a", "the shining and blinding sunset", {"href": "https://www.google.com",})

        self.assertEqual(node.children, None)

    def test_to_html(self):
        node = LeafNode("p", "The shining and blinding sunset")
        node2 = LeafNode("a", "The shining and blinding sunset", {"href": "https://www.google.com"})
        node3 = LeafNode("a", "The shining and blinding sunset", {"href": "https://www.google.com", "target": "_blank"})
        node4 = LeafNode(None, "no tags")

        self.assertEqual(node.to_html(), "<p>The shining and blinding sunset</p>")
        self.assertEqual(node2.to_html(), '<a href="https://www.google.com">The shining and blinding sunset</a>')
        self.assertEqual(node3.to_html(), '<a href="https://www.google.com" target="_blank">The shining and blinding sunset</a>')
        self.assertEqual(node4.to_html(), 'no tags')

    def test_parent_to_html(self):
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        )
        self.assertEqual(node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

        node2 = ParentNode(
        "p",
        [
            LeafNode("a", "Link Text", {'href': "https://www.google.com", "target": "_blank"}),
            LeafNode("b", "Bold text"),
            LeafNode("i", "Italic text"),
            LeafNode(None, "Normal text"),
        ],
        )
        self.assertEqual(node2.to_html(), '<p><a href="https://www.google.com" target="_blank">Link Text</a><b>Bold text</b><i>Italic text</i>Normal text</p>')

    def test_parent_to_html2(self):
        node = ParentNode(
        "div",
        [
            ParentNode("p", [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                            ]),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        )
        self.assertEqual(node.to_html(), '<div><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>Normal text<i>italic text</i>Normal text</div>')

        node2 = ParentNode(
        "p",
        [],
        )

        with self.assertRaises(ValueError) as Context:
            node2.to_html()

        node2 = ParentNode(
        "",
        [LeafNode(None, "Normal text")],
        )

        with self.assertRaises(ValueError) as Context:
            node2.to_html()