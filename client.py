from calc import Matematica

Mat = Matematica()
change_choise = input('выбери чем будем заниматься:\n 1 - сложение \n 2 - вычитание \n ответ - ')
def change(num):

    while True:
        if num == "1":
            Mat.slozhenie()
        elif num == '2':
            Mat.vychitanie()
        else:
            print('эх лентяюшка....')
            break


change(change_choise)


