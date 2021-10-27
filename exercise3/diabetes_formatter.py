import re

def arff_reader(file):
    arff_file = open(file, 'r')
    list = []

    for x in arff_file:
        x = x.strip('\n')
        regex = re.findall('^%', x)
        regex1 = re.findall('^@', x)
        if not regex and not regex1:
            if not x == '\n':
                list.append(x)

    arff_file.close()

    return list
def arff_writer(lists):
    outfile = open('diabetes_disc.arff', 'w')
    for i in lists:
        print(i[0])
        i = str(i) + '\n'
        i = re.sub(r'[^a-zA-Z0-9,_]', '', i)
        # i = re.sub('[(){}<>, " "]', '', i)
        # i.strip()
        # i.strip("[]")
        # print(i[0])
        print(i)
        outfile.write(str(i) + '\n')
    # dad = 0
    outfile.close()


list = arff_reader('diabetes.arff')
disc_list = []
for i in list:
    new_list = i.split(',')
    new_list[2] = int(new_list[2])
    new_list[5] = float(new_list[5])
    new_list[7] = int(new_list[7])
    if new_list[2] < 90:
        new_list[2] = 'low'
    elif new_list[2] >= 90 and new_list[2] <= 120:
        new_list[2] = 'ideal'
    elif new_list[2] > 120 and new_list[2] <= 140:
        new_list[2] = 'prehigh'
    elif new_list[2] > 140:
        new_list[2] = 'high'

    if new_list[5] < 18.5:
        new_list[5] = 'underweight'
    elif new_list[5] >= 18.5 and new_list[5] <= 25:
        new_list[5] = 'normal'
    elif new_list[5] > 25:
        new_list[5] = 'overweight'

    if new_list[7] < 40:
        new_list[7] = 'young'
    elif new_list[7] >= 40 and new_list[7] <= 60:
        new_list[7] = 'middle'
    elif new_list[7] > 60:
        new_list[7] = 'elderly'
    # print(f'The blood pressure is {new_list[2]}, the mass is {new_list[5]} and the age is {new_list[7]}')
    # print(new_list)
    # print(len(new_list))
    disc_list.append(new_list)

arff_writer(disc_list)