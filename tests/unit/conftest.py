from unittest.mock import create_autospec
import pytest
from tests.lib import mockMagic
from cvprac.cvp_client import CvpClient, CvpApi


@pytest.fixture
def apply_mock(mocker):
    """
    apply_mock - factory function to return a method to apply mocker.patch() on paths

    """
    def _apply_mock_factory(paths: list):
        return [mocker.patch(path) for path in paths]

    return _apply_mock_factory

@pytest.fixture
def mock_cvpClient():
    """
    mock_cvprac - mocks cvprac classes/objects
    """
    # mocked cvpClient object
    mock_cvpClient = create_autospec(CvpClient)
    mock_cvpClient.api = create_autospec(spec=CvpApi)
    mock_cvpClient.api.validate_config_for_device.side_effect = mockMagic.validate_config_for_device
    mock_cvpClient.api.move_device_to_container.side_effect = mockMagic.move_device_to_container
    return mock_cvpClient
