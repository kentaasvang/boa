

LICENSE = """MIT License

Copyright (c) (( name )) (( year ))
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""


SETUP =	"""from setuptools import setup, find_packages

with open("README.md", "r") as file_handler:
    long_description = file_handler.read()

setup(
    name="(( name ))",
    version="0.0.1",
    author="(( user ))",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)"""


SETTINGS = """import os

DEVELOPMENT = True


filename = ".env.dev" if DEVELOPMENT else ".env"

# Read in key/values from environment file and load
# them into the enrironment
try:
    with open(filename, "r") as file_handler:
        arguments = []

        # read lines in file and append to arguments-list
        while argument := file_handler.readline():
            arguments.append(argument.split("="))

        # load key/values into environment so they can be reached with
        # os.getenv()
        for key, value in arguments:
            os.environ[key] = value

except FileNotFoundError as file_not_found:
    print(f"The file {filename} was not found. Make sure it's created")

"""

MAIN = """def main():
    return "hello, world"

if __name__ == "__main__":
    main()
"""

TEST = """import unittest
import (( name ))

class Test(( name ))(unittest.TestCase):
    def test_(( name ))(self):
        self.assertEqual((( name )).main(), "hello, world")

if __name__ == "__main__":
    unittest.main()
"""
