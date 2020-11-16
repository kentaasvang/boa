from setuptools import setup, find_packages


with open("README.md", "r") as file_handler:
    long_description = file_handler.read()

setup(
    name="pboa",
    version="0.0.1a1",
    author="Kent Martin Åsvang",
    author_email="kentaasvang@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kentaasvang/boa",
    py_modules=["command_line"],
    packages=find_packages(),
    install_requires=["Click"],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Environment :: Console",
        "Operating System :: OS Independent"],
    entry_points= {
        # "console_scripts": ["boa=boa.boa:boa"]},
        "console_scripts": ["boa=command_line:cli"]},
    python_requires=">=3.8"
)
