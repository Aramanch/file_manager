import os

global working_path

working_path = input('введите полный путь рабочей директории: ')

try:
    os.chdir(working_path)

except FileNotFoundError:
    os.mkdir(working_path)
    os.chdir(working_path)


def backwk():
    lastdir = os.path.dirname(os.getcwd())
    if os.getcwd() != working_path:
        os.chdir(lastdir)
        print(os.getcwd())
    else:
        print('Не смей выходить за рабочую директорию!!!')
