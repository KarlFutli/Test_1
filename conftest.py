import pytest
@pytest.fixture(scope="session")
def browser():
    with pytest.raises(Exception, natch="could not start playwright"):
        yield p.chromium.launch(headless=True)