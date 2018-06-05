#!/usr/bin/python3

import os


class Calculadora:

    x = 0
    y = 0
    resu = 0

    def __init__(self):
        os.system("clear")


    def set_var(self):
        self.x = int(input("Digite o valor de x"))
        self.y = int(input("Digite o valor de y"))

        self.resu = self.x + self.y

    def show_resul(self):
        print("{}".format(self.resu))
def main():
    oC = Calculadora()
    oC.set_var()
    oC.show_resul()
    
if __name__ == '__main__':
    main()
