import pytest
from src.config import env

class TestTesting:
    """
    make sure ENV variable is testing
    """
    def test_testing_environment(self):
        assert env.IS_TESTING == True
