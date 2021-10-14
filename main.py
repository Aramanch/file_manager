import os

request = ''

while request != 'end':
    request = input()



    if  request == "1":
        name = input()
        direct = "C:\\Users\\207791\\Desktop\\roott\\{name}".format(name=name)
        os.mkdir(direct)

    elif request == "2":
        name = input()
        direct = "C:\\Users\\207791\\Desktop\\roott\\{name}".format(name=name)
        os.rmdir(direct)

    elif request == "3":
        name = input()
        direct = "C:\\Users\\207791\\Desktop\\roott\\{name}".format(name=name)
        os.chdir(direct)
        print(os.getcwd())

    elif request == "4":
        direct = "C:\\Users\\207791\\Desktop\\roott"
        os.chdir(direct)
        print(os.getcwd())

    elif request == "5":
        name = input()
        open(name,'w')
        print(os.getcwd())

'''
    elif request == "6":
        name = input()
        f = open(name,'w')
        f.write(input())
'''



