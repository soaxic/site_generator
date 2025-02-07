import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    #HTMLNode Tests
    def test_props_to_html(self):
        node1_prop = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node1 = HTMLNode(props=node1_prop)
        self.assertEqual(node1.props_to_html(), ' href="https://www.google.com" target="_blank"')
    
    def test_props_neq(self):
        node_tag = "a"
        node_value = "Click here to go to Google!"
        node_props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node1 = HTMLNode()
        node2 = HTMLNode(node_tag, node_value, node1, node_props)
        self.assertNotEqual(node2.tag, None)
        self.assertNotEqual(node2.value, None)
        self.assertNotEqual(node2.children, None)
        self.assertNotEqual(node2.props, None)

    def test_eq(self):
        node1 = HTMLNode()
        self.assertEqual(node1.tag, None)
        self.assertEqual(node1.value, None)
        self.assertEqual(node1.children, None)
        self.assertEqual(node1.props, None)
        
    def test_repr(self):
        node_tag = "a"
        node_value = "Click here to go to Google!"
        node_props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node1 = HTMLNode()
        node2 = HTMLNode(node_tag, node_value, node1, node_props)
        testcase = f"HTMLNode({node2.tag}, {node2.value}, {node2.children}, {node2.props})"
        self.assertEqual(node2.__repr__(), testcase)

    #LeafNode Tests
    def test_leaf_node(self):
        node_tag = "a"
        node_value = "Click here to go to Google!"
        node_props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = LeafNode(node_tag, node_value, node_props)
        testcase = '<a href="https://www.google.com" target="_blank">Click here to go to Google!</a>'
        self.assertEqual(node.to_html(), testcase)

if __name__ == "__main__":
    unittest.main()