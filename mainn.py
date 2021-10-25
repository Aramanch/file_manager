import os
import shutil
from sets import *





print("Файловый менеджер: \n" 
      "1.Создать папку \n"
      "2.Удалить папку \n"
      "3.Переместиться \n"
      "4.Вернуться в рабочую директорию \n"
      "5.Создать текстовый файл \n"
      "6.Записать текст в файл \n"
      "7.Посмотреть содержимое файла \n"
      "8.Удалить файл \n"
      "9.Скопировать файл в другую папку \n"
      "10.Переместить файл \n"
      "11.Переименовать файл \n"
      "12.Содержимое папки")

request = ''






def create():
        name = input()
        nerka = os.getcwd()
        new_path = f"{nerka} + os.sep + {name}".format(name=name)
        os.mkdir(new_path)



def deleting():
        try:
            name = input()
            dirrr = f"{direct} + os.sep + {name}"
            os.rmdir(dirrr)
        except OSError:
            askk = input("Вы уверены, что хотите удалить непустую папку?: ")
            if askk == 'да':
                shutil.rmtree(dirrr)
                print("Готово!")
            else:
                os.chdir(direct)
                print(os.getcwd())




def walking():
      global directionnn
      namme = input()
      directionnn = os.getcwd()
      new_dir = f"{directionnn} + os.sep + {namme}"
      os.chdir(new_dir)
      print(os.getcwd())



def changing():
        os.chdir(direct)
        print(os.getcwd())




def spisok():
        print(os.listdir(f"{os.getcwd()}"))




def sozdat():
        name = input('Имя файла:')
        open(name,'w')
        print(os.getcwd())




def writing():
        name = str(input('Файл: '))
        f = open(name,'w')
        f.write(input())
        f.close()



def reading():
        name = str(input())
        f = open(name)
        print(f.read())





def udaling():
        name = input()
        os.remove(name)
        print("Готово!")

def backwk():
      global directionnn
      os.chdir(directionnn)
      




def copying():
        papka = input("Папка, из которой копируем: ")
        name = input('Файл: ')
        ppapka = input("Папка, в которую копируем: ")
        shutil.copy(f"{direct} + os.sep + {papka} + os.sep + {name}",f"{direct} + os.sep + {ppapka}")



def replacing():
        cur_kat = os.getcwd()
        naming = input('Файл: ')
        ppapkka = input("Папка, в которую перемещаем: ")
        os.replace(f"{cur_kat} + os.sep + {naming}", f"{direct} + os.sep + {ppapkka} + os.sep + {naming}")



def renaming():
        naming = input('Файл: ')
        new_name = input('Новое название: ')
        direction = os.getcwd()
        os.rename(f"{direction} + os.sep + {naming}", f"{direction} + os.sep + {new_name}")


while request != 'end':
    request = input()


    if request == "1":
        create()

    elif request == "2":
        deleting()

    elif request == "3":
        walking()

    elif request == "4":
        changing()

    elif request == "5":
        sozdat()

    elif request == "6":
        writing()

    elif request == "7":
        reading()

    elif request == "8":
        udaling()

    elif request == "9":
        copying()

    elif request == "10":
        replacing()

    elif request == "11":
        renaming()

    elif request == "12":
        spisok()

    
