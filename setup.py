from setuptools import setup, find_packages


with open("README.md", "r") as file_handler:
    long_description = file_handler.read()

setup(
    name="pboa",
    version="0.0.1",
    author="Kent Martin Åsvang",
    author_email="kentaasvang@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kentaasvang/python_create",
    #py_modules=["boa", "settings", "templates"],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Environment :: Console",
        "Operating System :: OS Independent"],
    entry_points= {
        "console_scripts": ["boa=boa.boa:boa"]},
    python_requires=">=3.8"
)
