import re
import mechanize

br = mechanize.Browser()
response = br.open("http://www.datasymbol.com/barcode-recognition-sdk/barcode-reader/online-barcode-decoder.html")

br.form = list(br.forms())[0]

type_control = br.form.find_control("sr")
# set output to be text instead of image
type_control.value = ['0']

pdf417_control = br.find_control("c12")
pdf417_control.items[0].selected = True

br.form.add_file(open("bar.jpeg"), "text/plain", "bar.jpeg")
control = br.form.find_control("fupload1")

submit_control = None
for controls in br.form.controls:
    if controls.type == 'submit':
        submit_control = controls

submit_control.readonly = False

response = br.submit()
print(response.read())
