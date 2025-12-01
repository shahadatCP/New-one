# try exception things
try:
    result = 45/0
except:
    print('error happend')
finally:
    print('we got an error so we are here')
print('done')

# the way it work is, try give us some space to write a code and than if the code inside try don't work properly or get any error it doesn't effect in other line
