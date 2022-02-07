import os
from src import utils


def read_file(filename):
    with open(filename, "r") as f:
        data = f.read()
    return data


def create_file(content):
    file_name = utils.random_file_name()
    if os.path.exists(file_name):
        create_file(content)
        return
    with open(file_name, "w") as f:
        f.write(content)
    print(f'File - {file_name} created. File content: {content}')
    return content


def delete_file(filename):
    return os.remove(filename)


def list_dir(path):
    return os.listdir(path)


def change_dir(directory):
    return os.chdir(directory)


def get_file_permissions(filename):
    if os.path.exists(filename):
        permissions = os.stat(filename).st_mode
        print(f"file permissions : {permissions}")
    else:
        print('File not existed')


def set_file_permissions(filename, perm):
    if os.path.exists(filename):
        print(f"Set {perm} to {filename}")
        os.chmod(filename, perm)
    else:
        print('File not existed')


def get_cwd():
    wd = os.getcwd()
    return wd
