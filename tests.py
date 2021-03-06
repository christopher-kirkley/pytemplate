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
    tree = app.create_tree('app', 'oneoff')
    create_dir = app.create_directories('app', tree)
    create_files = app.create_files(project, tree)
    assert create_files == True
    current_files = [f for f in os.listdir() if os.path.isfile(f)]
    assert len(current_files) == 7

def test_can_create_directories_for_single(project):
    tree = app.create_tree('app', 'single')
    create_dir = app.create_directories('app', tree)
    directories = [d for d in os.listdir() if os.path.isdir(d)]
    assert create_dir == True
    assert directories == ['app', 'tests']

def test_can_create_files_for_single(project):
    path = os.getcwd()
    tree = app.create_tree('app', 'single')
    app.create_directories(project, tree)
    create_files = app.create_files(project, tree)
    assert create_files == True
    os.chdir(project)
    assert len(os.listdir()) == 3
    os.chdir(f'{path}/tests')
    assert len(os.listdir()) == 2
    os.chdir(path)
    current_files = [f for f in os.listdir() if os.path.isfile(f)]
    assert len(current_files) == 5

def test_can_create_tree():
    tree = app.create_tree('app', 'single')
    assert len(tree) == 3
    tree = app.create_tree('app', 'oneoff')
    assert len(tree) == 1
    
    

