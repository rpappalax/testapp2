import os


FILENAME = 'version_last.txt'

def version_last_read():
    with open(FILENAME, "r") as file:
        return file.read()


def version_last_write():
    with open(FILENAME, "w") as file:
        file.write("100.1")


if __name__ == '__main__':
    
    version = version_last_read()
    print(f'LAST VERSION: {version}')
    version = version_last_write()
    

