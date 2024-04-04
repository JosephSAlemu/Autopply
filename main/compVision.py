#from datasets import load_dataset, Image
import os
import cv2
import easyocr
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time


class findText:
    def detectLogin(url:str):
        load_dotenv()
        chrome_options = Options()
        #Prevent GPU Stall issue
        chrome_options.add_argument("--disable-3d-apis")
        #store the webdriver with the headless config
        driver = webdriver.Chrome(options=chrome_options)
        #fetch the website
        test = driver.page_source
        print(test)
        driver.get(url)
        username = os.environ["USERLOGN"]
        password = os.environ["USERPASSW"]
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        #Got to fix this so it can press the submit button
        driver.find_element(By.XPATH, '//button[text()="Sign in"]').click
        #Can't keep the driver open forever
        driver.quit()
    
    #Computer Vision stuff for later use
    #def compVision():
        #domain = url.split('.', 2)[1] + '.png'
        #save the image
        #driver.save_screenshot('./images/'+ domain)        
        #read the image
        #image_path = './images/'+ domain
        #img = cv2.imread(image_path)
        #Set the reader language to english. Set the default for CPU unless you have CUDA or MPS
        #reader = easyocr.Reader(['en'], gpu=False)
        #Gives text coordinates, the text, and the score (probably to detect confidence)
        #text = reader.readtext(img)
        #looping through all the text information (coordinates, text, the score)
        #for i in text:
            #Destructures the tuple
            #box, txt, score = i
            #converts any float values in the box (A list of lists for coordinates) from any possible floats to integers
            #box_int = [[int(point) for point in cords] for cords in box]
            #This creates the bounding box for the text
            #cv2.rectangle(img, box_int[0], box_int[2], (0,255,0), 5)
        #cv2 (part of opencv) defaults to BGR (ew) so we convert it to RGB
        #plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        #plt.show()
        
        
        
    if __name__ == "__main__":
        #Pass through the url and driver screenshots image and uses easyOCR to detect the text
        imageText = detectLogin('https://www.linkedin.com/login')
        
        
