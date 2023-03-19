from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#path = "C:\Program Files (x86)\chromedriver.exe"
browse = webdriver.Chrome(options=options)

browse.get("https://spotify.com")
