import unittest

from extract_markdown import extract_markdown_images, extract_markdown_links

class testExtractionFunctions(unittest.TestCase):
    def testImageExtraction(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted_images = extract_markdown_images(text)
        self.assertListEqual(extracted_images, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

        text2 = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.img)"
        extracted_images2 = extract_markdown_images(text2)
        self.assertListEqual(extracted_images2, [("rick roll", "https://i.imgur.com/aKaOqIh.img")])

    def testLinkExtraction(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extracted_links = extract_markdown_links(text)
        self.assertListEqual(extracted_links, [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])

        text2 = "This is text with a link [to boot dev](https://www.boot.dev)"
        extracted_links2 = extract_markdown_links(text2)
        self.assertListEqual(extracted_links2, [("to boot dev", "https://www.boot.dev")])