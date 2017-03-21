# -*- coding: utf-8 -*- 
#!/usr/bin/python


import sys

def pickup_string(string):
    return string[1]+string[3]+string[5]+string[7]

if __name__ == "__main__":
    '''
    print result of picking up of 1,3,5,7 char from  string given as a arguments
    this only support 1 arguments
    original param should be "パタトクカシーー"
    '''
    string = sys.argv[1]
    pustring = pickup_string(string)
    print(pustring)
