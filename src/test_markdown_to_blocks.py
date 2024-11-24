import unittest

from markdown_to_blocks import markdown_to_blocks, block_to_block_type

class TestMarkdownToBlocks(unittest.TestCase):
    def testbootdevMarkdown(self):
        markdown = '# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item'
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(blocks, ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item'])

        markdown = '# This is a heading\n\n\n    This is a paragraph of text. It has some **bold** and *italic* words inside of it.     \n\n  * This is the first list item in a list block\n* This is a list item\n* This is another list item   '
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(blocks, ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item'])

    def testBlockToBlockType(self):
        blocks = ['# This is a heading', '```This is code text```', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item']
        block_types = []
        for block in blocks:
            block_type = block_to_block_type(block)
            block_types.append(block_type.value)
        self.assertListEqual(block_types, ['heading', 'code', 'normal', 'unordered'])

        block_type = block_to_block_type('##### This is a heading block')
        self.assertEqual(block_type.value, 'heading')
        block_type = block_to_block_type('###### This is a heading block')
        self.assertEqual(block_type.value, 'heading')

    def testOrderedBlock(self):
        block_type = block_to_block_type('1. this is an ordered block\n2. this is a second part of the list')
        self.assertEqual(block_type.value, 'ordered')

        block_type = block_to_block_type('1. this is an ordered block\n3. this is a second part of the list')
        self.assertEqual(block_type.value, 'normal')

        block_type = block_to_block_type('1. this is an ordered block\n2.this is a second part of the list')
        self.assertEqual(block_type.value, 'normal')

        block_type = block_to_block_type('1.')
        self.assertEqual(block_type.value, 'normal')

        block_type = block_to_block_type('1. this is an ordered block\n2. this is a second part of the list\n3. another \
                                         \n4. another')
        self.assertEqual(block_type.value, 'ordered')

    def testUnorderedList(self):
        block_type = block_to_block_type('- this is an unordered list\n- this is the second part of the list')
        self.assertEqual(block_type.value, 'unordered')

        block_type = block_to_block_type('- this is an unordered list\n* this is the second part of the list')
        self.assertEqual(block_type.value, 'unordered')

        block_type = block_to_block_type('-this is not an unordered list\n* this is the second part of the list')
        self.assertEqual(block_type.value, 'normal')

        block_type = block_to_block_type('- this is not an unordered list\nthis is the second part of the list')
        self.assertEqual(block_type.value, 'normal')


    def testQuotes(self):
        block_type = block_to_block_type('>superheroe destruyo el mundo, el FLASH\n>oh no')
        self.assertEqual(block_type.value, 'quote')

        block_type = block_to_block_type('>superheroe destruyo el mundo, el FLASH\noh no')
        self.assertEqual(block_type.value, 'normal')