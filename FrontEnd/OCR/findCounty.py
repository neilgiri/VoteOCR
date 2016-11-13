import re
import mechanize
import parser
from bs4 import BeautifulSoup

def getCounty(zipcode):
    #zipcode = str(zipcode)
    br = mechanize.Browser()
    url = "https://www.melissadata.com/lookups/zipcityphone.asp"

    br.open(url)

    br.form = list(br.forms())[0]

    zipControl = br.find_control("InData")
    zipControl.value = zipcode

    response = br.submit()

    soup = BeautifulSoup(response, 'html.parser')
    
    stringPage = soup.get_text()
    print(stringPage)
    stringPage = stringPage.split("County Seat",1)[1]
    stringPage = stringPage.split('(',1)[0]
    stringPage = stringPage[:-1]

    return stringPage

