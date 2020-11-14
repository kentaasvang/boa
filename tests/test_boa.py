import pytest
from os import path
from boa.boa import *


class TestTemplateEngine:
    
    def test_template_engine_basic(self):
        before = "hello, (( key ))"
        expected = "hello, world"
        content = { 
            "key": "world" 
        }
        assert template_engine(before, content) == expected
    
    def test_template_engine_wo_whitespace(self):
        before = "hello, ((key))"
        expected = "hello, world"
        content = { 
            "key": "world" 
        }
        assert template_engine(before, content) == expected


class TestCreateFile:

    def test_creating_file(self, tmpdir):
        temp_dir = tmpdir.mkdir("root")
        create_file(temp_dir, "filename", "filecontent")
        assert len(temp_dir.listdir()) == 1

    def test_file_content(self, tmpdir):
        temp_dir = tmpdir.mkdir("root")
        create_file(temp_dir, "filename", "filecontent")
        
        with open(temp_dir / "filename", "r") as file_handler:
            content = file_handler.read()

        assert content == "filecontent"


def test_create_project_folder(tmpdir):
    temp_dir = tmpdir.mkdir("root")
    create_project_folder(temp_dir / "my_folder")
    assert len(temp_dir.listdir()) == 1
    assert path.isdir(temp_dir / "my_folder")


def test_create_project_files_and_folders(tmpdir):
    temp_dir = tmpdir.mkdir("root")

    files: Dict[str, str] = {
        "file1": "content1",
        "file2": "content2"
    }

    create_project_files_and_folders(temp_dir, files)
    assert len(temp_dir.listdir()) == 4
    assert path.isfile(temp_dir / "file1")
    assert path.isfile(temp_dir / "file2")

    with open(temp_dir / "file1", "r") as file_handler:
        assert file_handler.read() == "content1"
    
    with open(temp_dir / "file2", "r") as file_handler:
        assert file_handler.read() == "content2"


def test_git_init(tmpdir):
    temp_dir = tmpdir.mkdir("root")
    git_init(temp_dir)

    assert path.isdir(temp_dir / ".git")


def test_boa(tmpdir):
    temp_dir = tmpdir.mkdir("root")
    boa("my_project", True, temp_dir)

    # check that all files and folders are produced
    assert len(temp_dir.listdir()) == 1
    assert path.isdir(temp_dir / "my_project")
    assert path.isdir(temp_dir / "my_project" / ".git")
    assert path.isfile(temp_dir / "my_project" / "LICENSE")
    assert path.isfile(temp_dir / "my_project" / "my_project.py")
    assert path.isfile(temp_dir / "my_project" / "Makefile")
    assert path.isfile(temp_dir / "my_project" / "tests.py")
    assert path.isfile(temp_dir / "my_project" / "setup.py")
    assert path.isfile(temp_dir / "my_project" / "settings.py")
    assert path.isfile(temp_dir / "my_project" / ".gitignore")





























