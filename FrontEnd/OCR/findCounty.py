import re
import mechanize
import parser
from bs4 import BeautifulSoup

def getCounty(zipcode):
    br = mechanize.Browser()
    url = "https://www.melinda.com/lookups/zipcityphone.asp"

    br.open(url)
    br.form = list(br.forms())[0]

    zipControl = br.find_control("InData")
    zipControl.value = zipcode

    response = br.submit()
    soup = BeautifulSoup(response, 'html.parser')

    stringPage = soup.get_text()
    stringPage = stringPage.split("County Seat", 1)[1]
    stringPage = stringPage.split("(", 1)[0]

    return stringPage
