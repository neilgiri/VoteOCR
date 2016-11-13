import re
import mechanize
import parser
#import views
from BeautifulSoup import BeautifulSoup
from datetime import date

def classification_selection(num):
    class_dict = {'1': 'A001', '2': 'B002', '3': 'C003', '4': 'D004',
            '5': 'E005', '6': 'F006', '7': 'G007'}
    return class_dict[num]


def fill_registeration(dictionary):
    br = mechanize.Browser()
    url_name = "https://covr.sos.ca.gov/"

    br.open(url_name)

    for i in range(4):
        br.form = list(br.forms())[0]
        if i == 0:
            br.form.set_value([classification_selection('1')], name='VoterType')
        elif i == 1:
            is_us_citizen = True
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

            br.form.set_value([dictionary['citizen']], type='checkbox', name='VoterInformation.IsUsCitizen')
            br.form.set_value(['true'], type='checkbox', name='VoterInformation.IsEighteenYear')
            br.form.set_value(dictionary['fname'], name='VoterInformation.NameFirst')
            br.form.set_value(dictionary['lname'], name='VoterInformation.NameLast')
            br.form.set_value([dictionary['DOBM']], name='VoterInformation.Month')
            br.form.set_value([dictionary['DOBD']], name='VoterInformation.Day')
            br.form.set_value(dictionary['DOBY'], name='VoterInformation.Year')

            br.form.set_value(dictionary['numDL'], name='VoterInformation.CaIdentification')
            br.form.set_value(dictionary['ssn'], name='VoterInformation.SsnLastFour')
            br.form.set_value(dictionary['aStreet'], name='VoterInformation.AddressStreet1')
            br.form.set_value(dictionary['aCity'], name='VoterInformation.AddressCity')
            br.form.set_value(dictionary['aZip'], name='VoterInformation.AddressZip')
            br.form.set_value([dictionary['county']], name='VoterInformation.CountyIdKey')
            br.form.set_value(['True'], name='VoterInformation.isPoliticalPrefSelected')
            br.form.set_value([dictionary['ppp']], name='VoterInformation.PoliticalPartyIdKey')
        elif i == 2:
            vote_mail = 'false'
            poll_worker = None
            polling_place = None

            dmv_signature = 'true'
            affirmation = 'true'

            br.form.set_value([dictionary['bbm']], name='VoterInformation.IsVoteByMail')
            br.form.set_value([poll_worker], type='checkbox', name='VoterInformation.IsAPollWorker')
            br.form.set_value([polling_place], type='checkbox', name='VoterInformation.IsPollingPlaceProvided')
            br.form.set_value([dmv_signature], name="VoterInformation.IsDmvSignatureConsent")
            br.form.set_value([affirmation], type='checkbox', name="VoterInformation.isAffirmationSelected")

        for control in br.form.controls:
            print(control)

        if i < 1:
            br.submit()
        elif i < 3:
            req = br.submit(nr=1)
            resp = br.open(req.geturl())
            soup = BeautifulSoup(resp.get_data())
            resp.set_data(soup.prettify())
            br.set_response(resp)
        else:
            print(br.form)
