import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Load the feature file
scenarios('../features/chatbot.feature')

# 2. Setup the browser fixture
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

# 3. Step Definitions mapping to the Gherkin text
@given("the user is on the healthcare portal")
def navigate_to_portal(driver):
    driver.get("https://www.wikipedia.org/")

@when(parsers.parse('the user sends the prompt "{prompt}"'))
def send_prompt(driver, prompt):
    chat_input = (By.ID, "searchInput")
    send_button = (By.CSS_SELECTOR, "button[type='submit']")
    
    driver.find_element(*chat_input).send_keys(prompt)
    driver.find_element(*send_button).click()

@then(parsers.parse('the AI response should contain "{expected_text}"'))
def verify_response(driver, expected_text):
    response_header = (By.ID, "firstHeading")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(response_header))
    
    bot_response_text = driver.find_element(*response_header).text
    assert expected_text in bot_response_text