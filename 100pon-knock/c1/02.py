# -*- coding: utf-8 -*- 
#!/usr/bin/python


import sys

def merge_string(string,string2):
    mergestring = ''
    for i  in range(len(string)):
        mergestring += string[i]
        mergestring += string2[i]
    return mergestring

if __name__ == "__main__":
    '''
    print result of merge  char from  string given as a arguments
    this only support 1 arguments
    original param should be "パトカー" + "タクシー"
    '''
    string = sys.argv[1]
    string2 = sys.argv[2]
    mergestring = merge_string(string,string2)
    print(mergestring)
