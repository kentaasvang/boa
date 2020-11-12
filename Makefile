
.PHONY: install, uninstall, build, clean, test, run, help


help:
	@echo "there is no help yet"

install:
	cp boa.py ~/.my_binaries/bin/boa
	cp templates.py ~/.my_binaries/bin/
	cp settings.py ~/.my_binaries/bin/
	chmod +x ~/.my_binaries/bin/boa

uninstall:
	rm ~/.my_binaries/bin/templates.py
	rm ~/.my_binaries/bin/settings.py
	rm ~/.my_binaries/bin/boa

test:
	python3 boa.py my_test_project

clean:
	rm -rf my_test_project
