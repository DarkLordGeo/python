from bs4 import BeautifulSoup
import requests
import json

def webInfo():
        url = input("Enter website url: ")
        html = requests.get(url.replace(" ",""))
        soup = BeautifulSoup(html.text, 'html.parser')
        
        imgArr = soup.find_all('img')
        imgSrc = []
        for img in imgArr:
            imgSrc.append(img['src'])
        
        hrefArr = soup.find_all('a')
        hrefs = []
        for href in hrefArr:
            hrefs.append(href['href'])
        
        inputArr = soup.find_all('input')
        inputs = []
        for inputTag in inputArr:
            inputs.append(inputTag['type'])
        
        webData = {
            "data":{
                "img_tags": [len(imgSrc),imgSrc],
                "a_tags": [len(hrefs),hrefs],
                "input_tags":len(inputs)
            }

        }
  
        jsonData = json.dumps(webData, indent=4)
        
        with open('webData.json',  mode='w', encoding='utf-8') as write_file:
            write_file.write(jsonData)


webInfo()
