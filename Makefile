help:
	@echo "there is no help yet"

install:
	pip3 install --editable .

uninstall:
	pip3 uninstall --editable pboa

pypi:
	rm ./dist/*
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload --skip-existing dist/* --verbose
