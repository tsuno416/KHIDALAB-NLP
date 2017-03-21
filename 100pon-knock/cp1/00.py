# -*- coding: utf-8 -*- 
#!/usr/bin/python


import sys

def reverse_string(string):
    return string[::-1]

if __name__ == "__main__":
    '''
    print reversed string given as a arguments
    this only support 1 arguments
    original param should be "stressed"
    '''
    string = sys.argv[1]
    revstring = reverse_string(string)
    print(revstring)
