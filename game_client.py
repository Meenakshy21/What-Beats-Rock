Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from selenium import webdriver
from selenium.webdriver.common.by import By
from dataclasses import dataclass
... from typing import Optional
... 
... @dataclass
... class GameResponse:
...     is_valid: bool
...     error_message: Optional[str]
... 
... class GameClient:
...     def __init__(self, headless: bool = True):
...         options = webdriver.ChromeOptions()
...         if headless:
...             options.add_argument("--headless=new")
...         self.driver = webdriver.Chrome(options=options)
...         self.driver.get("https://www.whatbeatsrock.com/")
... 
...     def validate_guess(self, current: str, guess: str) -> GameResponse:
...         """Check if current → guess is a valid move"""
...         try:
...             input_box = self.driver.find_element(By.TAG_NAME, "input")
...             input_box.clear()
...             input_box.send_keys(guess)
...             
...             self.driver.find_element(
...                 By.XPATH, "//button[contains(text(), 'GO')]"
...             ).click()
...             
...             # Wait for game response
...             time.sleep(2)
...             
...             if "next" in self.driver.page_source:
...                 return GameResponse(is_valid=True, error_message=None)
...             else:
...                 error = self.driver.find_element(By.XPATH, "//h2").text
...                 return GameResponse(is_valid=False, error_message=error)
...                 
...         except Exception as e:
...             return GameResponse(is_valid=False, error_message=str(e))
...     
...     def close(self):
