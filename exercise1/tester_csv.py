import re

f = open('data/iris.csv')
list = []

for x in f:
    x = x.strip('\n')
    regex = re.findall('^%', x)
    if not regex:
        if not x == '\n':
            list.append(x)

list.pop(0)
f.close()

w = open('data/result_csv.arff', 'w')
i = 0
new_list = []
for x in list:
    # x = x + '\n'
    # w.write(x)
    if x[-1]=='1':
        x = x[:-1] + 'Iris-setosa'
    elif x[-1]=='2':
        x = x[:-1] + 'Iris-versicolor'
    elif x[-1]=='3':
        x = x[:-1] + 'Iris-virginica'
    new_list.append(x)
    i = i + 1
w.close()
for x in new_list:
    print(x)
print(len(new_list))