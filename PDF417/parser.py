import sys
from dateutil.relativedelta import relativedelta
import datetime


def main(filename):
    writer = open('OUT.txt', 'w')
    codes = ["DAC", "DAD", "DCS", "DBB", "DAG", "DAI", "DAJ", "DAK"]

    with open(filename) as f:
        for line in f:
            code = line[0:3]
            if code in codes:
                writer.write(line[3:])
            elif code == 'DBC':
                if line[3] == '1':
                    writer.write("MALE\n")
                else:
                    writer.write("FEMALE\n")
            elif code == 'DDJ':
                dateT = datetime.date(int(line[7:]), 
                        int(line[3:5]), int(line[5:7]))
                writer.write(
                        (dateT - relativedelta(years=3)).strftime('%m%d%Y'))
    writer.close()
