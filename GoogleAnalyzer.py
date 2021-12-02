from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def analyze_my_website(url : str):
    driver = webdriver.Chrome()
    hold = WebDriverWait(driver, 200)
    driver.get("https://developers.google.com/speed/pagespeed/insights/")
    hold.until(EC.visibility_of_element_located((By.XPATH, "//span[text() = 'Ok, Got it.']"))).click()
    input_element = driver.find_element_by_name("url")
    input_element.clear()
    input_element.send_keys(url)
    input_element.send_keys(Keys.ENTER)
    hold.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='lh-gauge__svg-wrapper']"))).screenshot("output/Mobile/score.png")
    sleep(1)
    driver.find_element_by_xpath("//div[@class='lh-audit-group lh-audit-group--metrics']").screenshot("output/Mobile/webvitals.png")
    sleep(1)
    driver.find_element_by_xpath("//div[@class='lh-audit-group lh-audit-group--load-opportunities']").screenshot("output/Mobile/opportunities.png")
    sleep(2)
    driver.find_element_by_xpath("//div[@class='tab-title tab-desktop']").click()
    driver.find_element_by_xpath("//div[@class='lh-gauge__svg-wrapper']").screenshot("output/Desktop/score.png")
    sleep(1)
    driver.find_element_by_xpath("//div[@class='lh-audit-group lh-audit-group--metrics']").screenshot("output/Desktop/webvitals.png")
    sleep(1)
    driver.find_element_by_xpath("//div[@class='lh-audit-group lh-audit-group--load-opportunities']").screenshot("output/Desktop/opportunities.png")
    sleep(2)

if __name__ == "__main__":
    analyze_my_website("https://ggbexhaust.com/")