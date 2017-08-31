from __future__ import print_function
import csv

with open('examples.csv', 'rb') as f:
    reader = csv.reader(f)
    answers = list(reader)

answers.pop(0)

with open('answers.md', 'w+') as o:
    for a in answers:
        print(a[1] + '  \n', file=o)
        print('* [' + a[2] + '](' + a[2] + ')  ', file=o)
        print('* [' + a[3] + '](' + a[3] + ')  ', file=o)
        print('* [' + a[4] + '](' + a[4] + ')  ', file=o)
        print('* [' + a[5] + '](' + a[5] + ')  ', file=o)
        print('\n', file=o)
