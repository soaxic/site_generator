import unittest
from markdown import *

class TestSplitNodes(unittest.TestCase):
    def test_split(self):
        node = TextNode("This is text with a **bolded** section", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [TextNode("This is text with a ", TextType.TEXT, None), TextNode("bolded", TextType.BOLD, None), TextNode(" section", TextType.TEXT, None)],
            new_nodes,
        )

    def test_double_split(self):
        node = TextNode("This is text with *italic* and **bold** sections!", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [TextNode("This is text with ", TextType.TEXT, None), TextNode("italic", TextType.ITALIC, None), TextNode(" and ", TextType.TEXT, None), TextNode("bold", TextType.BOLD, None), TextNode(" sections!", TextType.TEXT, None)],
            new_nodes,
        )

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) and a broken link (https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertListEqual(
            [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')],
            extract_markdown_images(text)
        )

    def test_extract_image_from_link(self):
        text = "Wow! [this is a link not an image](https://www.google.com)"
        self.assertEqual([], extract_markdown_images(text))

    def test_extract_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertListEqual(
            [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')],
            extract_markdown_links(text)
        )

    def test_extract_link_from_image(self):
        text = "This is text with an ![image](https://localhost)"
        self.assertListEqual(
            [],
            extract_markdown_links(text)
        )