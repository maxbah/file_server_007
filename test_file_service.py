import pytest

from src import file_service
from mock import mock_open
import mock


def test_create_file_success(mocker):
    mocked_open = mock_open()
    mocker.patch("builtins.open", mocked_open, create=True)
    test_file_name = "test_random_string"
    mocker.patch("src.utils.random_file_name").return_value = test_file_name

    file_service.create_file("blabla")

    mocked_open.assert_called_with(test_file_name, "w")
    mocked_open().write.assert_called_with("blabla")


def test_create_file_duplicate(mocker):
    mocked_open = mock_open()
    mocker.patch("builtins.open", mocked_open, create=True)
    test_filename = 'test_rand_string'
    second_test_filename = 'second_test_rand_string'

    path_exist_mock = mocker.patch('os.path.exists')

    path_exist_call_count = 0

    def on_path_exist_call(filename):
        nonlocal path_exist_call_count
        path_exist_call_count += 1
        if path_exist_call_count == 1:
            assert filename == test_filename
            return True

        assert filename == second_test_filename
        return False

    path_exist_mock.side_effect = on_path_exist_call
    rand_string_mock = mocker.patch('src.utils.random_file_name')

    def random_string_side_effect():
        if len(rand_string_mock.mock_calls) == 1:
            return test_filename
        return second_test_filename
    rand_string_mock.side_effect = random_string_side_effect

    file_service.create_file("blabla")
    assert path_exist_mock.mock_calls == [mock.call(test_filename), mock.call(second_test_filename)]
    mocked_open.assert_called_with(second_test_filename, 'w')
    mocked_open().write.assert_called_with("blabla")


def test_delete_file(mocker):
    del_file_mock = mocker.patch("os.remove")
    test_filename = 'test_rand_string'
    file_service.delete_file(test_filename)
    del_file_mock.assert_called_with(test_filename)


def test_list_dir(mocker):
    list_dir_mock = mocker.patch("os.listdir")
    list_dir_mock.return_value = ["a"]
    res = file_service.list_dir('./')
    list_dir_mock.assert_called_once()
    assert res == ["a"]


def test_change_dir_success_flow(mocker):
    ch_dir_mock = mocker.patch("os.chdir")
    targ_dir = './'
    file_service.change_dir(targ_dir)
    ch_dir_mock.assert_called_with(targ_dir)


def test_change_dir_not_exist(mocker):
    ch_dir_mock = mocker.patch("os.chdir")
    targ_dir = 'test_dir'
    ch_dir_mock.return_value = 'FileNotFoundError'
    with pytest.raises(Exception):
        raise file_service.change_dir(targ_dir)

