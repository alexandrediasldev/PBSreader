import csv


def file_csv_tolist(filename):
    with open(filename, encoding="utf-8-sig") as csvfile:
        csv_output = csv.reader(csvfile, delimiter=",")
        csv_output = [x for x in csv_output if not x[0].startswith("#")]
        return csv_output


def file_equal_to_list(filename):
    with open(filename, encoding="utf-8-sig") as equalfile:
        equal_output = csv.reader(equalfile, delimiter="=")
        equal_output = [x for x in equal_output if not x[0][0].startswith("#")]
        return equal_output
