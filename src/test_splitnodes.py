import unittest
from splitnodes import *

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