

import sys

filename = str(sys.argv[1])

#print('The file is ', filename)

string = '>' + '\n' + '<'

f = open(filename,"r+")
file = f.readlines()

for line in file:
    words_array = line.split()
    for i in words_array:
        print (i)
        if '><' not in i:
            string2 = i + ' '
            #print(i)
            f.write(string2)
        else:
            w = i.replace('><',string)
            final = w + ' '
            #print(w)
            f.write(final)

f.close()
