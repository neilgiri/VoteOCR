import re
import mechanize
import parser
from BeautifulSoup import BeautifulSoup

def classification_selection(num):
    class_dict = {'1': 'A001', '2': 'B002', '3': 'C003', '4': 'D004', 
            '5': 'E005', '6': 'F006', '7': 'G007'}
    return class_dict[num]



br = mechanize.Browser()
url_name = "https://covr.sos.ca.gov/"
#br.set_handle_robots(False)
#br.addheaders = [('User-agent', 'Firefox')]
#br.addheaders.append( ['Accept-Encoding','gzip'] )
#br.set_debug_http(True)
#br.set_debug_responses(True)

br.open(url_name)

for i in range(3):
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

        drivers_license = 'F6913123'
        ssn = '4321'
        address_street1 = '2345 Cara Ln'

        city = 'barack'
        zipcode = '94720'
        county = 'Alameda01'

        select_party = True
        party = 'Democratic04'

        br.form.set_value(['true'], type='checkbox', name='VoterInformation.IsUsCitizen')
        br.form.set_value(['true'], type='checkbox', name='VoterInformation.IsEighteenYear')
        br.form.set_value(first_name, name='VoterInformation.NameFirst')
        br.form.set_value(last_name, name='VoterInformation.NameLast')
        br.form.set_value([month_birth], name='VoterInformation.Month')
        br.form.set_value([day_birth], name='VoterInformation.Day')
        br.form.set_value(year_birth, name='VoterInformation.Year')

        br.form.set_value(drivers_license, name='VoterInformation.CaIdentification')
        br.form.set_value(ssn, name='VoterInformation.SsnLastFour')
        br.form.set_value(address_street1, name='VoterInformation.AddressStreet1')
        br.form.set_value(city, name='VoterInformation.AddressCity')
        br.form.set_value(zipcode, name='VoterInformation.AddressZip')
        br.form.set_value([county], name='VoterInformation.CountyIdKey')
        br.form.set_value(['True'], name='VoterInformation.isPoliticalPrefSelected')
        br.form.set_value([party], name='VoterInformation.PoliticalPartyIdKey')
    elif i == 2:
        vote_mail = 'false'
        poll_worker = 'false'
        polling_place = 'false'

        dmv_signature = 'true'
        affirmation = 'true'

        br.form.set_value([vote_mail], name='VoterInformation.IsVoteByMail')
        br.form.set_value([poll_worker], name='VoterInformation.IsAPollWorker')
        br.form.set_value([polling_place], name='VoterInformation.IsPollingPlaceProvided')

    


    for control in br.form.controls:
        print(control)
    
    if i < 1:
        br.submit()
    else:
        req = br.submit(nr=1)
        resp = br.open(req.geturl())
        soup = BeautifulSoup(resp.get_data())
        resp.set_data(soup.prettify())
        br.set_response(resp)

