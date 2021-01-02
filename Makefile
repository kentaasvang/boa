
test:
	(\
		source venv/bin/activate; \
		coverage run -m pytest -v; \
		coverage html; \
	)

install: remove
	(source venv/bin/activate; pip install --editable .)

remove:
	(source venv/bin/activate; pip uninstall pboa --yes;)

publish:
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload --skip-existing dist/* --verbose
