
install:
	cp create.py ~/.my_binaries/bin/create
	cp templates.py ~/.my_binaries/bin/
	cp settings.py ~/.my_binaries/bin/
	chmod +x ~/.my_binaries/bin/create

uninstall:
	rm ~/.my_binaries/bin/templates.py
	rm ~/.my_binaries/bin/settings.py
	rm ~/.my_binaries/bin/create

test:
	python3 create.py my_test_project

clean:
	rm -rf my_test_project
