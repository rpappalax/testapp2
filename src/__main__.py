import os
import datetime


FILENAME = 'src/version_last.txt'

def version_last_read():
    with open(FILENAME, "r") as file:
        return file.read()


def BAK_version_last_write():
    with open(FILENAME, "w") as file:
        file.write("100.2")


def version_last_write():
    import datetime import datetime  

    date_time = datetime.fromtimestamp(time_stamp)
    with open(FILENAME, "w") as file:
        file.write(date_time)


if __name__ == '__main__':
    
    version = version_last_read()
    print(f'LAST VERSION: {version}')
    version = version_last_write()
    

