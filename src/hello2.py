'''
Created on Nov 18, 2013

@author: Iddo
'''

print "hello3"


def hello_world():
    """returns hello world string"""
    return "hello world"


def hello_you(name):
    return "hello " + name


def bottles(num):
    return [(str(x) + " bottles of beer on the wall, "+str(x)+" bottles of beer.\nTake one down, pass it around, ") for x in range(num, 0, -1)]


def show_bottles(num):
    for x in bottles(num):
        print x
    print "No more bottles of beer on the wall"


def is_palindrome(s):
    if len(s) <= 1
        retrun True
    if (s[0]!=s[len(s)-1]
        return False
    return is_palindrome(s.substr(1,len(s)-1)))


print "OK"

