# Is Python pass by value or pass by reference language.
# It is both depending on the situation

def double(arg):
    print('Before: ', arg)
    arg = arg * 2
    print('After: ', arg)
    
def change(arg):
    print('Before: ', arg)
    arg.appent('More data')
    print('After: ', arg)