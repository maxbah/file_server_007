import string
import random
from time import time


def random_file_name():
    rand = string.ascii_uppercase + string.digits
    name = ''.join(random.sample(rand*6, 6))
    file_name = f"{name}_{time()}"
    return file_name
