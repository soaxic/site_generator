import unittest
from converter import *
from htmlnode import *

class TestConverter(unittest.TestCase):
    def test_converter(self):
        markdown = """
# This is a pretty long document that starts with a header!

### It even has a smaller header!

It's got some paragraphs
full of text
and meaningless information

```
It also has some code blocks.
With code! Who could've guessed?
print("Hello world!")
```

>God save the Queen
>A quote from John Madden
>Probably...

A list of my **favorite** things:

1. My cat
2. Pizza
3. Ordered lists

*Some* things I don't like:

* Bad drivers
* Cold coffee
- Unordered lists with varied flags
* Readable code

Here's a picture of a cat:

![a picture of a cat](https://catpictures.org/areallycutecat.png)

And a link to my [favorite website](https://www.google.com/)
"""
        pn = markdown_to_html_code(markdown)
        testcase = "ParentNode(div, [ParentNode(h1, [LeafNode(None, This is a pretty long document that starts with a header!, None)], None), ParentNode(h3, [LeafNode(None, It even has a smaller header!, None)], None), ParentNode(p, [LeafNode(None, It's got some paragraphs, None)], None), ParentNode(p, [LeafNode(None, full of text, None)], None), ParentNode(p, [LeafNode(None, and meaningless information, None)], None), ParentNode(pre, [ParentNode(code, [LeafNode(None, It also has some code blocks., None)], None), ParentNode(code, [LeafNode(None, With code! Who could've guessed?, None)], None), ParentNode(code, [LeafNode(None, print(\"Hello world!\"), None)], None)], None), ParentNode(blockquote, [LeafNode(None, od save the Queen, None), LeafNode(None,  quote from John Madden, None), LeafNode(None, robably..., None)], None), ParentNode(p, [LeafNode(None, A list of my , None), LeafNode(b, favorite, None), LeafNode(None,  things:, None)], None), ParentNode(ol, [ParentNode(li, [LeafNode(None, My cat, None)], None), ParentNode(li, [LeafNode(None, Pizza, None)], None), ParentNode(li, [LeafNode(None, Ordered lists, None)], None)], None), ParentNode(p, [LeafNode(i, Some, None), LeafNode(None,  things I don't like:, None)], None), ParentNode(ul, [ParentNode(li, [LeafNode(None, Bad drivers, None)], None), ParentNode(li, [LeafNode(None, Cold coffee, None)], None), ParentNode(li, [LeafNode(None, Unordered lists with varied flags, None)], None), ParentNode(li, [LeafNode(None, Readable code, None)], None)], None), ParentNode(p, [LeafNode(None, Here's a picture of a cat:, None)], None), ParentNode(p, [LeafNode(img, , {'src': 'https://catpictures.org/areallycutecat.png', 'alt': 'a picture of a cat'})], None), ParentNode(p, [LeafNode(None, And a link to my , None), LeafNode(a, favorite website, {'href': 'https://www.google.com/'})], None)], None)"
        self.assertEqual(testcase, str(pn))

    def test_heading(self):
        markdown = """
### Heading 3

#### Heading 4

# Heading 1"""
        pn = markdown_to_html_code(markdown)
        testcase = "ParentNode(div, [ParentNode(h3, [LeafNode(None, Heading 3, None)], None), ParentNode(h4, [LeafNode(None, Heading 4, None)], None), ParentNode(h1, [LeafNode(None, Heading 1, None)], None)], None)"
        self.assertEqual(testcase, str(pn))

    def test_code(self):
        markdown = """```
code is here
and here!
```"""
        pn = markdown_to_html_code(markdown)
        testcase = "ParentNode(div, [ParentNode(pre, [ParentNode(code, [LeafNode(None, code is here, None)], None), ParentNode(code, [LeafNode(None, and here!, None)], None)], None)], None)"
        self.assertEqual(testcase, str(pn))

    def test_quote(self):
        markdown = """
>This
>Is
>A
>Quote!"""
        pn = markdown_to_html_code(markdown)
        testcase = "ParentNode(div, [ParentNode(blockquote, [LeafNode(None, his, None), LeafNode(None, s, None), LeafNode(None, uote!, None)], None)], None)"
        self.assertEqual(testcase, str(pn))

    def test_ul(self):
        markdown = """
* This
- Is
* An unordered
- List!"""
        pn = markdown_to_html_code(markdown)
        testcase = "ParentNode(div, [ParentNode(ul, [ParentNode(li, [LeafNode(None, This, None)], None), ParentNode(li, [LeafNode(None, Is, None)], None), ParentNode(li, [LeafNode(None, An unordered, None)], None), ParentNode(li, [LeafNode(None, List!, None)], None)], None)], None)"
        self.assertEqual(testcase, str(pn))

    def test_ol(self):
        markdown = """
1. One!
2. Two!
3. Three!
"""
        pn = markdown_to_html_code(markdown)
        testcase = "ParentNode(div, [ParentNode(ol, [ParentNode(li, [LeafNode(None, One!, None)], None), ParentNode(li, [LeafNode(None, Two!, None)], None), ParentNode(li, [LeafNode(None, Three!, None)], None)], None)], None)"
        self.assertEqual(testcase, str(pn))