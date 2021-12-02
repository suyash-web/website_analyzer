from selenium import webdriver
from PIL import Image
from time import sleep
import os

def upload_and_show_saved_bits():
    cwd = os.getcwd()
    path_list = []
    d = cwd+"/output/oversized_images"
    for path in os.listdir(d):
        full_path = os.path.join(d, path)
        if os.path.isfile(full_path):
            path_list.append(full_path)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://compressor.io/")
    driver.implicitly_wait(15)
    driver.find_elements_by_xpath("//label[@class='ant-radio-button-wrapper']")[0].click()
    driver.implicitly_wait(15)
    driver.find_element_by_id("imageupload").send_keys(path_list[0])
    driver.find_element_by_xpath("//span[text()='Clear list']").click()
    for i in range(1, len(path_list)):
        driver.find_element_by_id("imageupload").send_keys(path_list[i])
        driver.implicitly_wait(4)
    sleep(5)
    driver.implicitly_wait(15)
    element = driver.find_element_by_xpath("//div[text()='Saved: ']")
    sleep(5)
    driver.implicitly_wait(5)
    # click screenshot 
    element.screenshot(cwd+"/output/Compressed_images/total_bits_saved.png")
    driver.close()