"""Script to generate template structure for common py apps."""

import argparse
import os
import sys


def create_project_directory(project):
    try:
        os.mkdir(project)
        os.chdir(project)
        return True
    except OSError:
        print('Creation of initial directory failed. Check if directory exists.')
        return False
    return None

def create_files(project):
    """Make files.
    Files are empty, but this could create custom files."""

    file_list = [f'{project}.py', '.gitignore', 'LICENSE', 'README.md', 'requirements.txt',
                'setup.py', 'tests.py',
                ]
    for file_ in file_list:
        with open(file_, 'w') as fp:
            pass
    return file_list

def create_directories_for_single_package(project):
    directories = [project, 'tests']
    for directory in directories:
        os.mkdir(directory)
    return directories

def create_files_for_single_package(project):
    path = os.getcwd()
    app_files = ['__init__.py', f'{project}.py', 'helpers.py',]
    test_files = [f'{project}_tests.py', 'helpers_tests.py',]
    files_ = ['.gitignore', 'LICENSE', 'README.md', 'requirements.txt', 'setup.py',]
    for file_ in app_files:
        with open(f'{project}/{file_}', 'w') as fp:
            pass
    for file_ in test_files:
        with open(f'tests/{file_}', 'w') as fp:
            pass
    for file_ in files_:
        with open(file_, 'w') as fp:
            pass
    return app_files, test_files, files_




if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='pytemplate',
                                    description="Generate python app structure",
                                    usage='%(prog)s [options] project',)
    parser.add_argument('-t',
                        dest='type',
                        type=str,
                        help='type of project',
                        action='store',
                        choices=['oneoff', 'single', 'complex', 'flask'],
                        required=True)
    parser.add_argument('project', type=str, help='project')
    args = parser.parse_args()

    print(f'Creating project {args.project}...')
    
    create_project_directory(args.project)
    if args.type == 'oneoff':
        create_files(args.project)
    if args.type == 'single':
        create_directories_for_single_package(args.project)
        create_files_for_single_package(args.project)


    



