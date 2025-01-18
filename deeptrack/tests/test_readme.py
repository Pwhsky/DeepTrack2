import os
import sys
import re
import unittest

class TestLink(unittest.TestCase):

    def test_links(self):

        sys.path.append("../../")
        with open("README.md", "r", encoding="utf-8") as readme_file:
            readme_content = readme_file.read()
        
        # Find Colab links in the README using regexp.
        colab_links = re.findall(
            r'href="(https://colab.research.google.com[^"]+)"',
            readme_content,
        )

        # Go over each found Colab link.
        for link in colab_links:

            # Get filepath from the Colab link.
            start_index = link.find("tutorials/")  
            path_to_file = link[start_index:]

            # Check if the file exists in repository.
            file_exists = os.path.exists(path_to_file)
            self.assertTrue(file_exists, msg=f"Error: Notebook in {path_to_file} was not found!")

if __name__ == "__main__":
    unittest.main()