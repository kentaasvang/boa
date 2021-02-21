
default:
	@echo "test, install or pypi";

test:
	coverage run -m pytest -v
	coverage html

install:
	( \
        	. venv/bin/activate; \
        	pip install --editable .; \
    	)

pypi:
	python3 setup.py sdist bdist_wheel;
	python3 -m twine upload --skip-existing dist/* --verbose;

