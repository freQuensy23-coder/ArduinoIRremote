import json
import serial
import serial
import sys
import time
import pyautogui

SPEED = 9600  #Serial port speed

def read_from_json(filename):
    with open(filename) as f:
        result = json.load(f)
        return result

#TODO: (Seny) Начать делать дизайн для каждой кнопки оставить свободным выбор функции. Все функции пиши одним блоком. Делай ООП только если знаешь что делаешь
#TODO: (Alex) реализовать ввод данных с Serial порта

def main():
    keys = read_from_json("config.json") #Считываем номера клавиш из дсон хранилища
                         #TODO: (Alex) Добавить в жсон все клавиши как в картикне пульта

                                             # TODO: (Alex) Сделать считывание с сериал порта
    ser = serial.Serial('COM8', SPEED)
    while True:
        str = ser.readline().decode("utf-8")

        print(str.replace("\n", ""))
        print(type(str))




def get_function(keys, hex):
    """Возвращает кортеж тип функции и номер. Например цфра 5 - вернёт (Numbers, 5). Громскость вверх верёт (Sound_+, 0) (0 т.к. в Sound_+ только ё-на функция, увеличение громкости)"""
    for key in keys:
        if (type(keys[key]) == str):
            if keys[key] == str:
                if (hex == str):
                    return (key, 0)

        if (type(keys[key]) == list):
            for i, k in enumerate(keys[key]):
                if  (k == hex):
                    return (key, i)

def get_c



if __name__ == '__main__':
    main()