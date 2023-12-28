import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options



@pytest.fixture()
def dc():

    desired_cap = {
        "appium:automationName": "UIAutomator2",
        "platformName": "Android",
        "appium:appPackage": "com.sling",
        "appium:appActivity": "com.sling.MainActivity"
    }
    appium_s = "http://0.0.0.0:4723/wd/hub"
    # Converts capabilities to AppiumOptions instance
    capabilities_options = UiAutomator2Options().load_capabilities(desired_cap)
    driver = webdriver.Remote(appium_s, options=capabilities_options)
    return driver
