import unittest

from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_images_links import split_nodes_image, split_nodes_link
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

    def testImageTypes(self):
        node = TextNode('This is a text with an image ![image alt text](https://www.google.com/24952.jpeg) and ![another image](https://www.pinterest.com/hoy.gif)', TextType.TEXT)
        new_nodes = split_nodes_image([node])

        expected_nodes = [TextNode('This is a text with an image ', TextType.TEXT, None), 
                          TextNode('image alt text', TextType.IMAGES, 'https://www.google.com/24952.jpeg'), 
                          TextNode(' and ', TextType.TEXT, None), 
                          TextNode('another image', TextType.IMAGES, 'https://www.pinterest.com/hoy.gif')]
        
        assert len(new_nodes) == len(expected_nodes), "Node count mismatch"
        for i, (actual, expected) in enumerate(zip(new_nodes, expected_nodes)):
            assert actual.text == expected.text, f"Mismatch in text at index {i}: {actual.text} != {expected.text}"
            assert actual.text_type == expected.text_type, f"Mismatch in type at index {i}: {actual.text_type} != {expected.text_type}"
            assert actual.url == expected.url

    def TestLinkTypes(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        new_nodes = split_nodes_link([node])

        expected_nodes = [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
                ]
        
        assert len(new_nodes) == len(expected_nodes), "Node count mismatch"
        for i, (actual, expected) in enumerate(zip(new_nodes, expected_nodes)):
            assert actual.text == expected.text, f"Mismatch in text at index {i}: {actual.text} != {expected.text}"
            assert actual.text_type == expected.text_type, f"Mismatch in type at index {i}: {actual.text_type} != {expected.text_type}"
            assert actual.url == expected.url
