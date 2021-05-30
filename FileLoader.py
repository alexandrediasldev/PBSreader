import csv

def FileCsvTolist(filename):
    with open(filename, encoding="utf8") as csvfile:
        csvOutput = csv.reader(csvfile, delimiter=',')
        csvOutput = [x for x in csvOutput if not x[0].startswith('#')]
        return csvOutput


def FileEqualToList(filename):
    with open(filename, encoding="utf8") as equalfile:
        equalOutput = csv.reader(equalfile, delimiter='=')
        equalOutput = [x for x in equalOutput if not x[0][0].startswith('#')]
        return equalOutput

