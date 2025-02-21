from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "PARAGRAPH"
    HEADING = "HEADING"
    CODE = "CODE"
    QUOTE = "QUOTE"
    UNORDERED_LIST = "UNORDERED_LIST"
    ORDERED_LIST = "ORDERED_LIST"

    def __repr__(self):
        return f"BlockType.{self.value}"

def block_to_blocktype(block):
    lines = block.split("\n")
    for i, line in enumerate(lines, 1):
        if str(i)+". " not in line[0:2+len(str(i))]:
            break
        if i == len(lines):
            return BlockType.ORDERED_LIST
    patterns = {
        r"^#{1,6} " : BlockType.HEADING,
        r"^`{3}[\s\S]*?`{3}$" : BlockType.CODE,
        r"^(>.*(\n|$))+$" : BlockType.QUOTE,
        r"^([\*-] .*(\n|$))+$" : BlockType.UNORDERED_LIST,
    }
    for pattern, blocktype in patterns.items():
        if re.match(pattern, block):
            return blocktype
    return BlockType.PARAGRAPH