import json
import serial

def read_from_json(filename):
    with open(filename) as f:
        result = json.load(f)
        return result

#TODO: (Cert) Начать делать дизайн для каждой кнопки оставить свободным выбор функции. Все функции пиши одним блоком. Делай ООП только если знаешь что делаешь
#TODO: (Alex) реализовать ввод данных с Serial порта

def main():
    keys = read_from_json("config.json") #Считываем номера клавиш из дсон хранилища
                                         #TODO: (Alex) Добавить в жсон все клавиши как в картикне пульта
    print(keys)
                                         # TODO: (Alex) Сделать считывание с сериал порта


if __name__ == '__main__':
    main()