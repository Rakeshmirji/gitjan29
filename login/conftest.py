import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.opera import OperaDriverManager
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browsername", action="store", default="chrome"

    )

    parser.addoption(
        "--url", action="store", default="prod"

    )


@pytest.fixture(scope="class")
def setup(request):
    browsername=request.config.getoption("browsername")
    url=request.config.getoption("url")
    if browsername=="chrome":
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
    if browsername=="firefox":
        driver = webdriver.Chrome(executable_path=OperaDriverManager().install())
    if url=="prod":
        driver.get("https://demo.insuredmine.com/agent/session/loginone")
    if url == "test":
        driver.get("https://www.insuredmine.info/agent-portal4/dist/session/loginone")

    request.cls.driver=driver
    yield
    driver.close()