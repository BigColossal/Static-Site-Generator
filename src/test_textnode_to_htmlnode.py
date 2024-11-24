import unittest

from textnode_to_htmlnode import text_node_to_html_node
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestTextnodeConversion(unittest.TestCase):
    def testTextType(self):
        node = TextNode('The assignments were due tomorrow', TextType.TEXT)
        leaf_node = text_node_to_html_node(node)
        self.assertEqual(leaf_node, LeafNode(tag = None, value = 'The assignments were due tomorrow', props = None))

        node2 = TextNode('q viva juan pablo duarte', TextType.BOLD)
        leaf_node2 = text_node_to_html_node(node2)
        self.assertEqual(leaf_node2, LeafNode(tag = "b", value = 'q viva juan pablo duarte', props = None))

        node3 = TextNode('el lugar estaba cerca', TextType.ITALIC)
        leaf_node3 = text_node_to_html_node(node3)
        self.assertEqual(leaf_node3, LeafNode(tag = "i", value = 'el lugar estaba cerca', props = None))


        node4 = TextNode('print(decay)', TextType.CODE)
        leaf_node4 = text_node_to_html_node(node4)
        self.assertEqual(leaf_node4, LeafNode(tag = "code", value = 'print(decay)', props = None))

        node5 = TextNode('The link to the nearest restaurant', TextType.LINKS, 'https://restauranteDominicano.com')
        leaf_node5 = text_node_to_html_node(node5)
        self.assertEqual(leaf_node5, LeafNode(tag = "a", value = 'The link to the nearest restaurant', props = {'href': 'https://restauranteDominicano.com'}))

        node6 = TextNode('An image of the famous Mangu Plate', TextType.IMAGES, 'https://restauranteDominicano.com/photo10/')
        leaf_node6 = text_node_to_html_node(node6)
        self.assertEqual(leaf_node6, LeafNode(tag = "img", value = 'An image of the famous Mangu Plate', props = {'src': 'https://restauranteDominicano.com/photo10/'}))
