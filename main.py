import json
import serial
import serial
import sys
import time
import pyautogui
import asyncio

SPEED = 9600  #Serial port speed
USB_PORT = 'COM8'
KEYS_CONFIG_FILENAME = "config.json"
TRANSLATION_CONFIG_FILENAME = "text.json"

scrol = 0 #-1 - down +1  up

def switch(bool):
    if bool == True:
        return False
    if bool == False:
        return False


def read_from_json(filename):
    with open(filename) as f:
        result = json.load(f)
        return result

#TODO: (Seny) Начать делать дизайн для каждой кнопки оставить свободным выбор функции. Все функции пиши одним блоком. Делай ООП только если знаешь что делаешь

def get_keys_hex():
    return read_from_json(KEYS_CONFIG_FILENAME)


def get_translation(LANG):
    try:
        return read_from_json(KEYS_CONFIG_FILENAME[LANG])
    except Exception as e:
        if (e == KeyError):
            return read_from_json(KEYS_CONFIG_FILENAME["EN"])
    except:
        print("Language is not supported")
        return (None, None)

def get_function(keys, hex):
    """Возвращает кортеж тип функции и номер. Например цфра 5 - вернёт (Numbers, 5). Громскость вверх верёт (Sound_+, 0) (0 т.к. в Sound_+ только ё-на функция, увеличение громкости)."""
    for key in keys:

        if (type(keys[key]) == str):
            if keys[key] == str:
                if (hex == str):
                    return (key, 0)
        if (type(keys[key]) == list):
            # print(key)
            for i, k in enumerate(keys[key]):
                if  (k.strip() == hex.strip()):
                    return (key, i)
    return None

def press_enter():
    pyautogui.typewrite('\n')


def click_mouse():
    pyautogui.leftClick()

def change_scroll(up):
    global scrol
    print ("up", up)
    if (up == True):
        if (scrol == 1) or (scrol == -1):
            scrol = 0
        else:
            scrol = 1
    else:
        if (scrol == 1) or (scrol == -1):
            scrol = 0
        else:
            scrol = -1

def main():
    hexs =  get_keys_hex() # Считываем номера клавиш из дсон хранилища
                         #TODO: (Alex) Добавить в жсон все клавиши как в картикне пульта

    ser = serial.Serial(USB_PORT, SPEED)
    while True:
        str = ser.readline().decode("utf-8")
        str = (str.replace("\n", ""))
        try:
            func, num = get_function(hexs, str)
        except:
            func, num = None, None
        if (func != None):
            if func == "up/down":
                print("up/down")
                change_scroll(-num*2+1)

        if (scrol > 0):
            pyautogui.scroll(200)
            print("scrol up")
        elif (scrol < 0):
            pyautogui.scroll(-200)
            print("scrol down")
        print(scrol)




if __name__ == '__main__':
    main()