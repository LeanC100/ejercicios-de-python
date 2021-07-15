import os 
import pathlib

class Note:

    NAMES_FILE = []

    def add_note(self):
        os.system('cls')
        print('     AND NOTE')
        name = input('Enter the name file: ')
        self.NAMES_FILE.append(name)

        with open('./notes/' + name + '.txt', 'w') as file:
            content = input ('Enter the content: ')
            file.write(content)
            input('GREAT!!! the file was created correctly')

    def view_note(self):
        x = 0
        os.system('cls')
        for i in self.NAMES_FILE:
            print(f'{self.NAMES_FILE[x]}')
            x += 1
        
        ENTER_NAME =input('\n\n     Enter the file name: ')
        for i in self.NAMES_FILE:
            if ENTER_NAME == i:
                with open('./notes/' + ENTER_NAME + '.txt', 'r') as file:
                    os.system('cls')
                    print(file.read())

                    input('\n\n     Back')
            else:
                pass

    def delete_note(self):
        x = 0
        os.system('cls')
        for i in self.NAMES_FILE:
            print(f'{self.NAMES_FILE[x]}')
            x += 1
        ENTER_NAME = input('\n\n     Enter the file name: ')
        for i in self.NAMES_FILE:
            if ENTER_NAME == i:
                op = input('Delete this file \n     1- Yes | 2-No \n')
                if op == '1':
                    os.remove('./notes/' + ENTER_NAME + '.txt')
                    self.NAMES_FILE.remove(ENTER_NAME)
                    input('     File deleted')
                elif op == '2':
                    input('     File not deleted')
                else:
                    input('invalid option')
            else:
                pass
        print('     Back')
    def load_name(self):
        LIST = os.listdir('./notes')
        os.system('cls')
        x = 0
        for i in LIST:
            self.NAMES_FILE.append(i[0:-4])
            x += 1


    def menu(self):
        CONTINUE = True
        ADD = 1
        VIEW = 2
        DELETE = 3
        EXIT = 0

        self.load_name()

        while CONTINUE:
            os.system('cls')
            print('     Mys notes')
            print(f'{ADD}- Add note')
            print(f'{VIEW}- View note')
            print(f'{DELETE}- Delete Note')
            print(f'{EXIT}- Exit')
            op = input('select a option:')
            try:
                op = int(op)
            except:
                op = -1

            if op == ADD:
                self.add_note()
            elif op == VIEW:
                self.view_note()
            elif op == DELETE:
                self.delete_note()
            elif op == EXIT:
                CONTINUE = False
            else:
                input('Value invalid!! \n press Enter')
        input('Bye!!!!!')      

    def __str__ ():
        return 1
