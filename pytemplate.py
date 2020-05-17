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

def choose_type(project, type_):
    if x == :
        return tree
    elif x == 
        return tree
    elif x ==xx
        return tree


def create_directories_for_single_package(project):
    tree = {f'{project}': ['__init__.py', f'{project}.py', 'helpers.py',],
            'tests': [f'{project}_tests.py', 'helpers_tests.py',],
            'root': ['.gitignore', 'LICENSE', 'README.md', 'requirements.txt', 'setup.py',],
            }
    directories = [key for key in tree.keys()]
    for directory in directories:
        if directory == 'root':
            pass
        else:
            try:
                os.mkdir(directory)
            except OSError:
                return False
    return True

def create_files_for_single_package(project):
    tree = {f'{project}': ['__init__.py', f'{project}.py', 'helpers.py',],
            'tests': [f'{project}_tests.py', 'helpers_tests.py',],
            'root': ['.gitignore', 'LICENSE', 'README.md', 'requirements.txt', 'setup.py',],
            }
    for directory, files in tree.items():
        for file_ in files:
            if directory == 'root':
                with open(file_, 'w') as fp:
                    pass
            else:
                with open(f'{directory}/{file_}', 'w') as fp:
                    pass

    return True




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


    



