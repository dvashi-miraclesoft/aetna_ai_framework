import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # Setup: Initialize Chrome in headless mode for faster CI/CD execution
    options = webdriver.ChromeOptions()
    options.add_argument("--headless") # Runs silently in the background
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    
    # Teardown: Always close the browser after the test
    driver.quit()

def test_chatbot_input_and_response_delay(driver):
    # 1. ARRANGE: Go to the portal
    driver.get("https://www.wikipedia.org/")
    
    # Define our locators (Simulating a Chatbot UI)
    chat_input = (By.ID, "searchInput")
    send_button = (By.CSS_SELECTOR, "button[type='submit']")
    
    # 2. ACT: Type the prompt and send
    prompt = "HIPAA"
    driver.find_element(*chat_input).send_keys(prompt)
    driver.find_element(*send_button).click()
    
    # AI responses take time to generate. We CANNOT use time.sleep(5).
    # We must use an Explicit Wait to wait specifically for the response element.
    response_header = (By.ID, "firstHeading")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(response_header)
    )
    
    # 3. ASSERT: Verify the AI's visual response contains the right subject
    bot_response_text = driver.find_element(*response_header).text
    assert "Health Insurance Portability and Accountability Act" in bot_response_text