import os
import datetime


FILENAME = 'src/version_last.txt'

def version_last_read():
    with open(FILENAME, "r") as file:
        return file.read()

#def version_last_write():
#    with open(FILENAME, 'w') as file:
#        file.write('100.2')

def current_time():
    current_time = datetime.datetime.now()
    return current_time.strftime('%H:%M:%S')


def version_last_write():
    with open(FILENAME, "w") as file:
        file.write(formatted_time)

def is_different(vers_a, vers_b):
    return (vers_a != vers_b)

if __name__ == '__main__':
    
    version_a = version_last_read()
    print(f'LAST VERSION (from file): {version_a}')
    version_b = current_time()
    print(f'CURRENT TIME: {version_b}')
    diff = is_different(version_a, version_b)
    print(f'IS_DIFFERENT: {diff}')
    

