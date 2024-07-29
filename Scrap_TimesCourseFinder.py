from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

URL = 'https://timescoursefinder.com/discover-course'

# set up the Chromium driver using Selenium
service = Service()
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(service=service, options=options)

# navigate to the target webpage
driver.get(URL)

# Wait for the product grid to load (adjust selector as needed)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".discoverTagFlex"))
)

# Get the page source (assuming elements are loaded)
html_content = driver.page_source
soup = BeautifulSoup(html_content, 'html.parser')




# for bachelors
# bachelor_courses = driver.find_elements(By.CSS_SELECTOR, ".discoverTagFlex:not(.purple)")
bachelor_courses = soup.find("div", class_="discoverTagFlex").findAll("a")

for course in bachelor_courses:
    
    course_title = course.text
    link_name = course_title.strip().lower().replace("&", "").replace(" ", "%20")
    course_link = f'https://timescoursefinder.com/search?degreelevel=bachelors&search={link_name}'
    
    
    
    # print("*******************")


# for masters

# Extract course details from soup or directly from driver elements

# ...
# print(soup.prettify())

# Close the browser window
driver.quit()
