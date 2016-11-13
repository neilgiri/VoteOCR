import re
import mechanize
import parser

def classification_selection(num):
    class_dict = {'1': 'A001', '2': 'B002', '3': 'C003', '4': 'D004', 
            '5': 'E005', '6': 'F006', '7': 'G007'}
    return class_dict[num]



br = mechanize.Browser()
url_name = "https://covr.sos.ca.gov/Home/MainForm"

br.open(url_name)

for i in range(2):
    br.form = list(br.forms())[0]
    if i == 0:
        br.form.set_value([classification_selection('1')], name='VoterType')
    elif i == 1:
        is_us_citizen = True
        is_18 = True
        first_name = 'Titan'
        last_name = 'Yuan'
        month_birth = '5'
        day_birth = '19'
        year_birth = '1985'

        drivers_license = '1243532124'
        ssn = '4321'
        address_street1 = '2345 Cara Ln'

        city = 'barack'
        zipcode = '77557'

        br.find_control(name='VoterInformation.IsUsCitizen', type='checkbox').selected = is_us_citizen
        br.find_control(name='VoterInformation.IsEighteenYear', type='checkbox').selected = is_18
        br.form.set_value(first_name, name='VoterInformation.NameFirst')
        br.form.set_value(last_name, name='VoterInformation.NameLast')
        br.form.set_value([month_birth], name='VoterInformation.Month')
        br.form.set_value([day_birth], name='VoterInformation.Day')
        br.form.set_value(year_birth, name='VoterInformation.Year')

        br.form.set_value(drivers_license, name='VoterInformation.CaIdentification')
        br.form.set_value(ssn, name='VoterInformation.SsnLastFour')
        br.form.set_value(address_street1, name='VoterInformation.MailingAddressStreet1')
        br.form.set_value(city, name='VoterInformation.MailingAddressCity')
        br.form.set_value(zipcode, name='VoterInformation.MailingAddressZip')



    for control in br.form.controls:
        print(control)

    br.submit()


