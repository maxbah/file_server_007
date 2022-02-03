import os
from src.utils import random_file_name


def read_file(filename):
    with open(filename, "r") as f:
        data = f.read()
    return data


def create_file(content):
    file_name = random_file_name()
    with open(file_name, "w") as f:
        f.write(content)
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


def set_file_permissions(filename):
    filename = input("Enter file name : ")
    if os.path.exists(filename):
        permissions = input("Input UNIX permissions in oct format (0o777):")
        print(f"Set {permissions} to {filename}")
        os.chmod(filename, permissions)
    else:
        print('File not existed')


def get_cwd():
    wd = os.getcwd()
    return wd
