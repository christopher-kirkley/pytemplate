"""Script to generate template structure for common py apps."""

import argparse
import os
import sys



if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='pytemplate',
                                    description="Generate python app structure",
                                    usage='%(prog)s [options] project_name',)
    parser.add_argument('-t',
                        dest='type',
                        type=str,
                        help='type of project',
                        action='store',
                        choices=['oneoff', 'single', 'complex', 'flask'],
                        required=True)
    parser.add_argument('project_name', type=str, help='project name')
    args = parser.parse_args()

    print(f'Creating project {args.project_name}...')
    
    project_name = args.project_name

    if args.type == 'oneoff':
        try:
            os.mkdir(project_name)
        except OSError:
            print('Creation of project failed.')
        else:
            print('Directory created...')

        """Make files.
        Files are empty, but this could create custom files."""

        os.chdir(project_name)
        file_list = [f'{project_name}.py', '.gitignore', 'LICENSE', 'README.md', 'requirements.txt',
                    'requirements.txt', 'setup.py', 'tests.py',
                    ]
        for file_ in file_list:
            with open(file_, 'w') as fp:
                pass
        print('Created one-off.')
    else:
        print('Nothing created.')

    



