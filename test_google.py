from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup Chrome driver
driver = webdriver.Chrome()

try:
    # Test Case 1: Google Search
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("SRM University")
    search_box.submit()
    time.sleep(3)
    
    # Take screenshot as proof
    driver.save_screenshot("google_search_test.png")
    print("✅ Google search test completed successfully!")
    
    # Test Case 2: Click first result
    first_result = driver.find_element(By.XPATH, "//h3")
    first_result.click()
    time.sleep(3)
    
    driver.save_screenshot("click_result_test.png")
    print("✅ Click test completed successfully!")
    
finally:
    driver.quit()
