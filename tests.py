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
    create_dir = app.create_directories_for_single_package('app')
    directories = [d for d in os.listdir() if os.path.isdir(d)]
    assert create_dir == True
    assert directories == ['app', 'tests']

def test_can_create_files_for_single_package(project):
    path = os.getcwd()
    app.create_directories_for_single_package(project)
    create_files = app.create_files_for_single_package(project)
    assert create_files == True
    os.chdir(project)
    assert len(os.listdir()) == 3
    os.chdir(f'{path}/tests')
    assert len(os.listdir()) == 2
    os.chdir(path)
    current_files = [f for f in os.listdir() if os.path.isfile(f)]
    assert len(current_files) == 5

