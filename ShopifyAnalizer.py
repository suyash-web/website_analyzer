from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

def analyze_website(url : str):
    driver = webdriver.Chrome()
    w = WebDriverWait(driver, 200)
    driver.get("https://analyze.speedboostr.com/")
    input_element = driver.find_element_by_id("analyze-url")
    input_element.clear()
    input_element.send_keys(url)
    sleep(2)
    driver.find_element_by_xpath("//button[text() = 'Accept']").click()
    input_element.send_keys(Keys.ENTER)
    w.until(EC.visibility_of_element_located((By.XPATH, "//td[text() = 'Oversized images']")))#.click()
    sleep(3)
    num = driver.find_elements_by_xpath("//td[@class = 'td-score']")[8].text
    if num == '0':
        return 0
    else:
        hrefs = []
        driver.find_element_by_xpath("//td[text() = 'Oversized images']").click()
        items = driver.find_elements_by_tag_name("a")
        for item in items:
            href = item.get_attribute('href')
            hrefs.append(href)
        li2 = hrefs[13:]
        li3 = li2[::-1]
        req_li = li3[20:]
        count = 1
        if len(req_li) == 1:
            a = req_li[0]
            response = requests.get(a)
            f = open("output/oversized_images/image1.jpeg", "wb")
            f.write(response.content)
            f.close()

        else:
            for i in req_li:
                i1 = i[::-1]
                i2 = i1[13:]
                url = i2[::-1]
                response = requests.get(url)
                file = open("output/oversized_images/image"+str(count)+".jpeg", "wb")
                file.write(response.content)
                file.close()
                count += 1
            driver.close()
            sleep(2)
        return 1
if __name__ == "__main__":
    print(analyze_website("https://www.propero.in/"))