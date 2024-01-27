from selenium import webdriver

class music():
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path:'C:\Users\Dell\Downloads\chromedriver_win32\chromedriver.exe')
    
    def play(self, query):
        self.query=query
        self.driver.get(URL="https://www.youtube.com/results?search_query=" + query)
        search=self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()