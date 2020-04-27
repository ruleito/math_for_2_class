import random
from time import sleep
class Matematica:

    def slozhenie(self):
        count = 0
        congratulations = ['молодец!!!','красава!!', 'я начинаю тебя боятся....', 'что ж... я не сдаюсь!']
        variable_answer = ['Давай посмотрим сколько тут- ', 'посчитал????? - ', 'эх... 3 года жду ответа.... - ', 'ОГО РЕШИЛ??? - ']
        while True:
            it_con = random.randint(0, len(congratulations)-1)
            a = random.randint(1,999)
            b = random.randint(1, a)
            if (a + b) > 1000:
                a = random.randint(1, 999)
                b = random.randint(1, a)

            summa = a + b
            privet = 'сколько будет если сложить эти 2 числа?', a, b
            print(privet)
            otvet = input(variable_answer[it_con])
            if otvet == 'q':
                print(f'{count} столько правильных ответов =)')
                print('выходим......')
                sleep(3)
                exit()
            while True:
                if len(otvet) == 0:
                    otvet = input("ой а что тут пусто?")
                elif not otvet.isdigit():
                    otvet= input("нужно число =)  ")
                else:
                    otvet = int(otvet)
                    break

            if summa == otvet:
                print(congratulations[it_con])
                count += 1
            else:
                while True:
                    otvet = input('давай еще: ')

                    if summa == int(otvet):
                        count += 1
                        print(congratulations[it_con])
                        break

    def vychitanie(self):
        count = 0
        congratulations = ['молодец!!!','красава!!', 'я начинаю тебя боятся....', 'что ж... я не сдаюсь!']
        variable_answer = ['Давай посмотрим сколько тут- ', 'посчитал????? - ', 'эх... 3 года жду ответа.... - ', 'ОГО РЕШИЛ??? - ']
        while True:
            it_con = random.randint(0, len(congratulations)-1)
            a = random.randint(1,999)
            b = random.randint(1, a)
            if (a + b) > 1000:
                a = random.randint(1, 999)
                b = random.randint(1, a)

            raznitza = a - b
            privet = f'вычти из числа {a} число {b}?',
            print(privet)
            otvet = input(variable_answer[it_con])
            if otvet == 'q':
                print(f'{count} столько правильных ответов =)')
                print('выходим......')
                sleep(3)
                exit()
            while True:
                if len(otvet) == 0:
                    otvet = input("ой а что тут пусто?")
                elif not otvet.isdigit():
                    otvet= input("нужно число =)  ")
                else:
                    otvet = int(otvet)
                    break

            if raznitza == otvet:
                print(congratulations[it_con])
                count += 1
            else:
                while True:
                    otvet = input('давай еще: ')

                    if raznitza == int(otvet):
                        count += 1
                        print(congratulations[it_con])
                        break





