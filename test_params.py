import pytest


@pytest.mark.usefixtures('param_loader')
class TestParamLoader:
    def test_param_loader(self, param_loader):
        print(param_loader)