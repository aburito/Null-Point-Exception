import re

f = open('data/iris.arff')
list = []

for x in f:
    x = x.strip('\n')
    regex = re.findall('^%', x)
    if not regex:
        if not x == '\n':
            list.append(x)

list.pop(0)
f.close()

w = open('data/result.arff', 'w')

for x in list:
    x = x + '\n'
    w.write(x)
    # print(x)
w.close()