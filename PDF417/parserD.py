from dateutil.relativedelta import relativedelta
import datetime

def main(filename):
    codes = {'DAC': 'fName', 'DAD': 'mName', 'DCS': 'lName', 'DBB': 'DOB', 
            'DAG': 'aStreet', 'DAI': 'aCity', 'DAJ': 'aState', 'DAK': 'aZip', 
            'DAQ': 'numDL'}
    data = {'lName': "NONE", 'fName': "NONE", 'mName': "NONE", 'DOB': "NONE", 
            'lDOB': "NONE", 'SEX': "NONE", 'aStreet': "NONE", 'aCity': "NONE", 
            'aState': "NONE", 'aZip': "NONE", 'numDL': "NONE"}
    with open(filename) as f:
        for line in f:
            code = line[0:3]
            if code in codes:
                data[codes[code]] = line[3:]
            elif code == 'DBC':
                if line[3] == '1':
                    data['SEX'] = "MALE"
                else:
                    data['SEX'] = "FEMALE"
            elif code == 'DDJ':
                dateT = datetime.date(int(line[7:]),
                        int(line[3:5]), int(line[5:7]))
                data['lDOB'] = (dateT - relativedelta(years=3)).strftime('%m%d%Y')
    return data
