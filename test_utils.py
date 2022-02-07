from src import utils


def test_random_file_name(mocker):
    test_file_name = "test_random_string"
    test_f_name = mocker.patch("src.utils.random_file_name").return_value = test_file_name
    count = 0
    while count <= 1000:
        count += 1
        assert utils.random_file_name() == test_f_name


