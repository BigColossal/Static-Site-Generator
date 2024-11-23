import unittest

from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextndoes(unittest.TestCase):
    def TestBasicExample(self):
        text = 'This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        self.assertEqual(text_to_textnodes(text), 
                        'This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)')