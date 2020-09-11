
.PHONY: install, uninstall, build, clean, test, run, help


help:
	@echo "there is no help yet"

install:
	cp create.sh ~/.my_binaries/bin/create
	chmod +x ~/.my_binaries/bin/create

uninstall:
	rm ~/.my_binaries/bin/create

build: clean
	cp src/create.py dist/create
	chmod +x dist/create
	
clean:
	rm -rf dist/*

run: build
	@printf "\nProgram output: \n___________\n\n"
	@./dist/create new somethingelse

