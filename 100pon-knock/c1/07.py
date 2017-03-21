# -*- coding: utf-8 -*- 
#!/usr/bin/python


import sys

if __name__ == "__main__":
    '''
    print string with given parameter.
    '''
    x = sys.argv[1]
    y = sys.argv[2]
    z = sys.argv[3]
    result = "{0}時の{1}は{2}".format(x,y,z)
    print(result)
