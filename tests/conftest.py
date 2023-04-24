import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FireFoxService
from selenium.webdriver.ie.service import Service as IeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser",
                     action='store',
                     default='ch',
                     help="""choose browser: default Chrome.
                          Choose:ch-Chrome, ff-FireFox, ie-InternetExplorer""")
    parser.addoption("--url",
                     action='store',
                     default='https://google.com.ua',
                     help='udd url address')


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture
def url_address(request):
    url = request.config.getoption("--url")
    return f"http://{url}/opencart/"


@pytest.fixture(scope='function')
def driver(request, browser):
    if browser == 'ch':
        service_manager = ChromeService(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument('--start-fullscreen')
        # options.add_argument('--headless')
        br = webdriver.Chrome(service=service_manager,
                              options=options)
        br.implicitly_wait(20)
    elif browser == 'ff':
        service_manager = FireFoxService(GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        options.add_argument('--start-fullscreen')
        options.add_argument('--headless')
        br = webdriver.Firefox(
            service=service_manager,
            options=options)
        br.implicitly_wait(20)
    elif browser == 'ie':
        # service_manager = IeService(IEDriverManager().install())
        options = webdriver.IeOptions()
        options.add_argument('--start-fullscreen')
        options.add_argument('--headless')
        br = webdriver.Ie(
            # service=service_manager,
            options=options)
        br.implicitly_wait(20)
    else:
        raise KeyError('safwekewkweoe')
    request.addfinalizer(br.quit)
    return br
