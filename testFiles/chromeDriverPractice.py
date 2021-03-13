from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://youtube.com')

searchBox = driver.find_element_by_xpath('//input[@id="search"]')
searchBox.send_keys("1967 Jeepster")

searchButton = driver.find_element_by_xpath('//button[@id="search-icon-legacy"]')
searchButton.click()

searched = driver.find_elements_by_xpath('//a[@id="video-title"]')

searchResultsArray = [0]
searchResultsArray = searched.append(searched)

print(searchResultsArray)

# giant wip