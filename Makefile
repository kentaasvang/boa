
install:
	cp create.py ~/.my_binaries/bin/create
	chmod +x ~/.my_binaries/bin/create

uninstall:
	rm ~/.my_binaries/bin/create

test:
	python3 create.py my_test_project

clean:
	rm -rf my_test_project
