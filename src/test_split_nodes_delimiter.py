import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesFunction(unittest.TestCase):
    def testAllTextTypes(self):
        node = TextNode('la guardia *se* puso de frente', TextType.TEXT)
        node2 = TextNode('Y se le **paso** la entera `guerra` ensima', TextType.TEXT)
        node3 = TextNode('This is an image in the old nodes', TextType.IMAGES, 'https://googleimages.com/148591/')

        new_nodes = split_nodes_delimiter([node, node2, node3], '**', TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, '*', TextType.ITALIC)
        new_nodes = split_nodes_delimiter(new_nodes, '`', TextType.CODE)

        expected_nodes = [
            TextNode('la guardia ', TextType.TEXT, None),
            TextNode('se', TextType.ITALIC, None),
            TextNode(' puso de frente', TextType.TEXT, None),
            TextNode('Y se le ', TextType.TEXT, None),
            TextNode('paso', TextType.BOLD, None),
            TextNode(' la entera ', TextType.TEXT, None),
            TextNode('guerra', TextType.CODE, None),
            TextNode(' ensima', TextType.TEXT, None),
            TextNode('This is an image in the old nodes', TextType.IMAGES, 'https://googleimages.com/148591/')
            ]
        
        assert len(new_nodes) == len(expected_nodes), "Node count mismatch"
        for i, (actual, expected) in enumerate(zip(new_nodes, expected_nodes)):
            assert actual.text == expected.text, f"Mismatch in text at index {i}: {actual.text} != {expected.text}"
            assert actual.text_type == expected.text_type, f"Mismatch in type at index {i}: {actual.text_type} != {expected.text_type}"
            assert actual.url == expected.url