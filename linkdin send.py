from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configure your LinkedIn credentials and recipient URL
USERNAME = "sidhbabulal70@gmail.com"
PASSWORD = "@2005"
RECIPIENT_PROFILE_URL = "https://www.linkedin.com/posts/babulal-sidh-ba1067296_cloned-customized-pushed-to-a-new-github-activity-7349882291214557185-63mU/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEeOO-kBGqCVycCpV4mOGOj6cQD3689WPVI"
MESSAGE_TEXT = "Hello from Python using Selenium "

# Start Chrome browser
driver = webdriver.Chrome()

# Step 1: Login to LinkedIn
driver.get("https://storage.googleapis.com/chrome-for-testing-public/140.0.7297.0/win32/chrome-win32.zip")
time.sleep(2)

driver.find_element(By.ID, "babulal sidh").send_keys(USERNAME)
driver.find_element(By.ID, "babulalsidh@2005").send_keys(PASSWORD)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)

# Step 2: Open the recipient's profile
driver.get(RECIPIENT_PROFILE_URL)
time.sleep(3)

message_button = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Message')]")
message_button.click()
time.sleep(3)

# Step 4: Type and send the message
message_box = driver.find_element(By.XPATH, "//div[contains(@role,'textbox')]")
message_box.send_keys(MESSAGE_TEXT)
message_box.send_keys(Keys.RETURN)

time.sleep(2)
driver.quit()
print("✅ Message sent successfully")
