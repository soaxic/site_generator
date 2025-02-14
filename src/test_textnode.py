import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
        
    def test_to_html_node(self):
        node = TextNode("This is bold text!", TextType.BOLD)
        testcase = "<b>This is bold text!</b>"
        self.assertEqual(text_node_to_html_node(node).to_html(), testcase)
    
    def test_img_to_html(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.somewebsite.com/someimage.jpg")
        testcase = '<img src="https://www.somewebsite.com/someimage.jpg" alt="This is an image"></img>'
        self.assertEqual(text_node_to_html_node(node).to_html(), testcase)

    def test_link_to_html(self):
        node = TextNode("Click here!", TextType.LINK, "https://www.somewebsite.com/")
        testcase = '<a href="https://www.somewebsite.com/">Click here!</a>'
        self.assertEqual(text_node_to_html_node(node).to_html(), testcase)

if __name__ == "__main__":
    unittest.main()