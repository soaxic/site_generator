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

    def test_split_nodes_image(self):
        node = TextNode("This is text with two images ![image](linky) and ![image](linky) Wow what great text!", TextType.TEXT)
        self.assertListEqual(
            [TextNode("This is text with two images ", TextType.TEXT, None), TextNode("image", TextType.IMAGE, "linky"), TextNode(" and ", TextType.TEXT, None), TextNode("image", TextType.IMAGE, "linky"), TextNode(" Wow what great text!", TextType.TEXT, None)],
            split_nodes_image([node])
        )

    def test_split_nodes_image_no_image(self):
        node = TextNode("This is text with no image!", TextType.TEXT, None)
        self.assertEqual([node], split_nodes_image([node]))

    def test_split_nodes_image_start_end(self):
        node = TextNode("![image1](link1) This text starts and ends with images ![image2](link2)", TextType.TEXT)
        self.assertListEqual(
            [TextNode("image1", TextType.IMAGE, "link1"), TextNode(" This text starts and ends with images ", TextType.TEXT, None), TextNode("image2", TextType.IMAGE, "link2")],
            split_nodes_image([node])
        )

    def test_split_nodes_image_spaced(self):
        node = TextNode(" ![image1](link1) ![image2](link2) ", TextType.TEXT)
        self.assertListEqual(
            [TextNode(" ", TextType.TEXT, None), TextNode("image1", TextType.IMAGE, "link1"), TextNode(" ", TextType.TEXT, None), TextNode("image2", TextType.IMAGE, "link2"), TextNode(" ", TextType.TEXT, None)],
            split_nodes_image([node])
        )

    def test_split_nodes_link(self):
        node = TextNode("this has a [link](https://localhost/)", TextType.TEXT)
        self.assertListEqual(
            split_nodes_link([node]),
            [TextNode("this has a ", TextType.TEXT, None), TextNode("link", TextType.LINK, "https://localhost/")]
        )

    def test_split_nodes_link_no_link(self):
        node = TextNode("this has no link", TextType.TEXT)
        self.assertListEqual(
            [node],
            split_nodes_link([node])
        )

    def test_split_nodes_link_start_end(self):
        node = TextNode("[link1](url.com) This text starts and ends with links [link2](url.net)", TextType.TEXT)
        self.assertListEqual(
            split_nodes_link([node]),
            [TextNode("link1", TextType.LINK, "url.com"), TextNode(" This text starts and ends with links ", TextType.TEXT, None), TextNode("link2", TextType.LINK, "url.net")]
        )

    def test_split_nodes_link_spaced(self):
        node = TextNode(" [link1](link1.com) [link2](link2.com) ", TextType.TEXT)
        self.assertListEqual(
            [TextNode(" ", TextType.TEXT, None), TextNode("link1", TextType.LINK, "link1.com"), TextNode(" ", TextType.TEXT, None), TextNode("link2", TextType.LINK, "link2.com"), TextNode(" ", TextType.TEXT, None)],
            split_nodes_link([node])
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

class TestTextToTextnodes(unittest.TestCase):
    def test_text_to_testnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        testcase = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertListEqual(
            text_to_textnodes(text),
            testcase
        )

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        self.assertListEqual(
            ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item'],
            markdown_to_blocks(text)
        )