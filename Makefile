
install:
	cp create.sh ~/.my_binaries/bin/create
	chmod +x ~/.my_binaries/bin/create

uninstall:
	rm ~/.my_binaries/bin/create

test:
	rm -rf ~/PythonProjects
	create python project-name
