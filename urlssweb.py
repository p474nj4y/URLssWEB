from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import time
from art import *

ascii_art = text2art("urlSSweb", font='rectangles')
print(ascii_art)
ascii_art1 = text2art("made w/ <3 by @p474nj4y", font='bubble')
print(ascii_art1)

def capture_screenshot(url, output_file):
    # Set up Chrome WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
    chrome_options.add_argument("--disable-gpu")  # Disable GPU for headless mode
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Navigate to the URL
        driver.get(url)

        # Wait for the page to load (you can adjust the wait time as needed)
        time.sleep(5)

        # Capture the screenshot
        driver.save_screenshot(output_file)

        # Close the WebDriver
        driver.quit()

        print(f"Screenshot saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        driver.quit()

if __name__ == "__main__":
    url = input("Enter the URL of the webpage: ")
    output_file = input("Enter the output file name (e.g., screenshot.png): ")

    capture_screenshot(url, output_file)
