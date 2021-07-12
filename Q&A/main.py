import os
import json

started = 1
quited = 0


point = 0


date_json = ''

with open('Q&A.json','r') as file:
    date_json = json.load(file)
    
def start():

    point = 0
    for line in date_json:
        os.system('cls')
        ok = False

        op_correct = None
        print(f'{date_json[line]["question"]}\n')
        for op in date_json[line]['aswers']:
            print(f'{op}')
            if op == date_json[line]['aswerCorrect']:
                op_correct = int(op[0])
        print()
        op_selected = input('Select a option: ')

        # El bucle While seguira hasta que el usuario coloque una de las 4 optiones validas
        while not ok:
            try:
                op_selected = int(op_selected)
            except ValueError:
                op_selected = -1

            if op_selected == 1 or op_selected == 2 or op_selected == 3 or op_selected == 4:
                ok = True
                if op_correct == op_selected:
                    print('Very Good!!!')
                    point += 1
                else:
                    print('Hoooo you chose the wrong option ')
                    print('Select a option valid')
                input('Press a botton for continues :)')
            else:
                print('You a option valid,plase')
                op_selected = input('Select a option: ')

        os.system('cls')
    print('     Congratulations!!!!!')
    print(f'    You got {point} points')
    input('     Press for return menu')


def menu():
    continues = True
    while continues:
        print('HI!!! Wecome to Q&A')
        print(f'''
    {started}- Start
    {quited}- Quit    
        ''')
        op = input('Select a option: ')
        try:
            op = int(op)
        except ValueError:
            op = -1
        if op == started:
            start()
        elif op == quited:
            continues = False
        else:
            print('Option no valid')
            print('Please, Select other option')
        print('')


def main():
    os.system('cls')

    menu()


if __name__ == '__main__':
    main()
