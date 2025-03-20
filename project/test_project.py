from unittest.mock import patch, MagicMock
from main import fetch_package_info, install_package, uninstall_package
import subprocess


def test_fetch_package_info():
    with patch('requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "info": {
                "name": "test-package",
                "version": "1.0.0",
                "summary": "A test package",
                "author": "Test Author",
                "project_urls": {
                    "Documentation": "https://test-package.org/docs"
                }
            }
        }
        mock_get.return_value = mock_response

        with patch('builtins.input', return_value='test-package'):
            fetch_package_info()

        mock_get.assert_called_once_with("https://pypi.org/pypi/test-package/json", timeout=5)

def test_install_package():
    with patch('subprocess.check_output') as mock_check_output, \
         patch('subprocess.check_call') as mock_check_call:
        mock_check_output.side_effect = subprocess.CalledProcessError(1, 'pip show')
        mock_check_call.return_value = 0

        with patch('builtins.input', return_value='test-package'):
            install_package()

        mock_check_output.assert_called_once_with(["pip", "show", "test-package"])
        mock_check_call.assert_called_once_with(["pip", "install", "test-package"])

def test_uninstall_package():
    with patch('subprocess.check_output') as mock_check_output, \
         patch('subprocess.check_call') as mock_check_call:
        mock_check_output.return_value = b"Name: test-package\nVersion: 1.0.0\n"
        mock_check_call.return_value = 0

        with patch('builtins.input', return_value='test-package'):
            uninstall_package()

        mock_check_output.assert_called_once_with(["pip", "show", "test-package"])
        mock_check_call.assert_called_once_with(["pip", "uninstall", "test-package", "-y"])

if __name__ == "__main__":
    test_fetch_package_info()
    test_install_package()
    test_uninstall_package()
    print("everything looks good!")
