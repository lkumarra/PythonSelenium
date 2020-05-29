"""
Created on 27-Apr-2020
@author: Lavendra rajput
"""
import json
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from test_utils.log_mananger import LogManager
from webdrivermanager.webdrivermanager import IEDriverManager

fileName = "../config/Confing.json"
file = open(fileName)
data = json.load(file)
log = LogManager() 

def pytest_addoption(parser):
    """
    Get the browser name from cmd
    """
    parser.addoption(
        "--browser_name", action="store", default="Chrome"
    )

@pytest.fixture(scope="function")
def setup(request):
    """
    Initialize the webdriver !
    """
    global driver
    if(request.config.getoption("browser_name") == "Chrome"):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        log.getLogger().debug("Chrome is launched")
    elif(request.config.getoption("browser_name") == "firefox"):
        driver = webdriver.Firefox(GeckoDriverManager().install())
        log.getLogger().debug("Firefox is launched")
    elif(request.config.getoption("browser_name")== "ie"):
        driver = webdriver.Ie(IEDriverManager().install())
        log.getLogger().debug("IE is launched")
    driver.get(data["url"])
    log.getLogger().debug("Enter the url" + data["url"])
    driver.maximize_window()
    log.getLogger().debug("Maximize the window")
    request.cls.driver = driver
    yield
    driver.quit()
    
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = "../test_report"+report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)
