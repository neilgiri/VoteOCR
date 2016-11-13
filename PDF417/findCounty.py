import re
import mechanize
import parser

#def main(zipcode):
br = mechanize.Browser()
url = "http://www.getzips.com/zip.htm"

br.open(url)

br.form = list(br.forms())[0]

zipControl = br.find_control("Zip")
zipControl.value = "90274"

br.submit()

county = 

#controls = list(br.form1.controls)
    
#for control in controls:
 #   print(control1)

