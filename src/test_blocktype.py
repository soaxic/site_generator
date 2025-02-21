import unittest
from blocktype import *
from markdown import *

class TestBlockType(unittest.TestCase):
    def test_block_to_blocktype(self):
        testcase = """
# Heading 1

## Heading 2

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6

```
code goes here
with more code
and some more code
```

>This is a
>quote block
>with three lines

* one
* two
* three
- one
- two
- three

1. one
2. two
3. three
4. asdf
5. asdf
6. asdf
7. asdf
8. asdf
9. asdf
10. asdf

this is just some text

so is this
but it takes two lines!"""
        tl = markdown_to_blocks(testcase)
        results = []
        for l in tl:
            results.append(block_to_blocktype(l))
        self.assertListEqual(
            results,
            [BlockType.HEADING, BlockType.HEADING, BlockType.HEADING, BlockType.HEADING, BlockType.HEADING, BlockType.HEADING, BlockType.CODE, BlockType.QUOTE, BlockType.UNORDERED_LIST, BlockType.ORDERED_LIST, BlockType.PARAGRAPH, BlockType.PARAGRAPH]
        )