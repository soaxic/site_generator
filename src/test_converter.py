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
        markdown = """
>lol
>quote
>time"""
        pn = markdown_to_html_code(markdown)
        print(pn.to_html())