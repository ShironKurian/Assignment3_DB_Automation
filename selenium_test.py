from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from db_config import get_db_connection
from webdriver_manager.chrome import ChromeDriverManager

# Set up WebDriver
service = Service(ChromeDriverManager().install())  # Automatically installs the chromedriver
driver = webdriver.Chrome(service=service)
driver.get("http://127.0.0.1:5000")

# Fill out the form
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")
username_input.send_keys("testuser")
password_input.send_keys("testpassword")
password_input.send_keys(Keys.RETURN)

# Wait for form processing
time.sleep(2)  # Adjust the time based on how long the form takes to process

# Verify data in MySQL
conn = get_db_connection()
cursor = conn.cursor()

# Fetch all results (even though we're just checking for one row)
cursor.execute("SELECT * FROM users WHERE username = 'testuser'")
results = cursor.fetchall()  # Get all results

# Check if any result exists
if results:
    print("Test Passed: User found in database")
else:
    print("Test Failed: User not found in database")

# Close the cursor and connection
cursor.close()
conn.close()

# Keep the browser open for a few seconds or until user closes it manually
time.sleep(5)  # Adjust this time to keep the browser open long enough for you to inspect

# Or alternatively, use input() to keep the browser open until manually closed
# input("Press Enter to exit and close the browser...")

# Close WebDriver
driver.quit()