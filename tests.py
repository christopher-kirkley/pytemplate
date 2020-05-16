import pytest
import os
import shutil

import pytemplate as app

@pytest.fixture
def project():
    path = os.getcwd()
    project_name = 'app'
    app.create_project_directory(project_name)
    yield project_name
    os.chdir(path)
    shutil.rmtree(project_name)

def test_can_create_project_directory():
    path = os.getcwd()
    project = 'app'
    result = app.create_project_directory(project)
    assert result == True
    os.chdir(path)
    shutil.rmtree(project)

def test_can_create_files_for_one_off(project):
    assert len(app.create_files(project)) == len(os.listdir())

def test_can_create_directories_for_single_package(project):
    assert len(app.create_directories_for_single_package(project)) == len(os.listdir())

def test_can_create_files_for_single_package(project):
    path = os.getcwd()
    app.create_directories_for_single_package(project)
    app_files, test_files, files_ = app.create_files_for_single_package(project)
    os.chdir(project)
    assert len(app_files) == len(os.listdir())
    os.chdir(f'{path}/tests')
    assert len(test_files) == len(os.listdir())
    os.chdir(path)
    current_files = [f for f in os.listdir() if os.path.isfile(f)]
    assert len(files_) == len(current_files)

