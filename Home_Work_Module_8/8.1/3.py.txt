import itertools
import sys
c = input('Enter the file name: ')
if c == '1.txt':
    with open(c,'r') as fs:
        sys.stdout.writelines(itertools.islice(fs, 1, None, 2))

else:
    print('Error')
