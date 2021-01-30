

if __name__ == "__main__":
    from selenium import webdriver

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)  # 今は chrome_options= ではなく options=

    driver.get('https://www.google.com/')
    print(driver.title)

    search_box = driver.find_element_by_name("q")
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    print(driver.title)

    els = driver.find_elements_by_class_name("g")
    print(len(els))
    print(els[0])

    els = driver.find_elements_by_class_name("tF2Cxc")
    for e in els:
        print('*'*10)
        # print(e.find_element_by_xpath("//*[contains(@class, 'LC20lb')]").text)
        print(e.find_element_by_class_name('LC20lb').text)
        print(e.find_element_by_tag_name('a').get_attribute('href'))

    # driver.save_screenshot('search_results.png')
    driver.quit()