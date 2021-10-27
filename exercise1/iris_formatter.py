import sys
import re


def arff_reader(file):
    arff_file = open(file, 'r')
    list = []

    for x in arff_file:
        x = x.strip('\n')
        regex = re.findall('^%', x)
        if not regex:
            if not x == '\n':
                list.append(x)

    arff_file.close()

    return list

def csvReader(f):
    list = []

    for x in f:
        x = x.strip('\n')
        regex = re.findall('^%', x)
        if not regex:
            if not x == '\n':
                list.append(x)

    f.close()

    i = 0
    csv_to_list = ['@RELATION iris',
                   '\n'
                   '@ATTRIBUTE sepallength	REAL',
                   '@ATTRIBUTE sepalwidth 	REAL',
                   '@ATTRIBUTE petallength 	REAL',
                   '@ATTRIBUTE petalwidth	REAL',
                   '@ATTRIBUTE class 	{Iris-setosa,Iris-versicolor,Iris-virginica}',
                   '',
                   '@DATA']
    for x in list:
        if x[-1] == '1':
            x = x[:-1] + 'Iris-setosa'
        elif x[-1] == '2':
            x = x[:-1] + 'Iris-versicolor'
        elif x[-1] == '3':
            x = x[:-1] + 'Iris-virginica'
        csv_to_list.append(x)
        i = i + 1

    return csv_to_list

fileName = sys.argv[1]
outputFile = sys.argv[2]
# fileName = 'data/iris.arff'
# outputFile = 'data/new_iris_csv.arff'
# outputFile = 'data/new_iris_arff.arff'

f = open(fileName, 'r')

def write_data(lists, outFile):

    outFile = open(outFile, 'w')

    last_line = 1

    for x in lists:
        if last_line == 159:
            outFile.write(x)
        else:
            x = x + '\n'
            outFile.write(x)
        last_line = last_line + 1

    outFile.close

    print('Data was written to: ' + outputFile + '.' )

csvMatch = re.findall('.csv$', f.name)
arffMatch = re.findall('.arff$', f.name)

if csvMatch:
    final_list = csvReader(f)
    write_data(final_list, outputFile)
    f.close()
elif arffMatch:
    final_list = arff_reader(fileName)
    write_data(final_list, outputFile)
    f.close()
else:
    print("The file you've entered is unavailable")


