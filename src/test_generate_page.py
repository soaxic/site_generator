import unittest
from generate_page import *

class TestGeneratePage(unittest.TestCase):
    def test_generate_page(self):
        generate_page("./content/index.md", "./template.html", "./public/index.html")