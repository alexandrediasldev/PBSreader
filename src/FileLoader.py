import csv


def file_csv_tolist(filename):
    with open(filename, encoding="utf-8-sig") as csvfile:
        csv_output = csv.reader(csvfile, delimiter=",")
        csv_output = [x for x in csv_output if not x[0].startswith("#")]
    # need to separate text from comment
    return csv_output


def file_equal_to_list(filename):
    with open(filename, encoding="utf-8-sig") as equalfile:
        equal_output = csv.reader(equalfile, delimiter="=")
        equal_output = [x for x in equal_output if x and x[0] and not x[0][0].startswith("#")]
        for x in equal_output:
            for i in range(len(x)):
                x[i] = x[i].rstrip("#")
                x[i] = x[i].strip()
        return equal_output


def file_equal_coma_to_list(filename):
    equal_output = file_equal_to_list(filename)
    for line in equal_output:
        coma_line = line[1].split(",")
        line.remove(line[1])
        line.extend(coma_line)
    return equal_output
