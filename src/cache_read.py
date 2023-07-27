import os
import datetime


FILENAME = 'src/version_last.txt'

def version_last_read():
    with open(FILENAME, "r") as file:
        return file.read()

#def version_last_write():
#    with open(FILENAME, 'w') as file:
#        file.write('100.2')


def version_last_write():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime('%H:%M:%S')
    with open(FILENAME, "w") as file:
        file.write(formatted_time)


if __name__ == '__main__':
    
    version = version_last_read()
    print(f'LAST VERSION: {version}')
    

