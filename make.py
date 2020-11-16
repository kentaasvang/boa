import os


def test():
    os.system("coverage run -m pytest -v") 
    os.system("coverage html")


def install():
    os.system("pip install --editable .")


def pypi():
    os.system("python3 setup.py sdist bdist_wheel")
    os.system("python3 -m twine upload --skip-existing dist/* --verbose")
