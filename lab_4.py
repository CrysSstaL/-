import time


class Key:
    def __init__(self, keyName, control):
        self.__keyName = keyName
        self.__control = control

    def getName(self):
        return self.__keyName

    @property
    def control(self):
        return self.__control

    def setName(self, newKey):
        self.__keyName = newKey

    def press_key(self):
        print(f'Нажата кнопка: {self.__keyName}')
        time.sleep(0.5)  # Задержка между нажатиями клавиш

    def reassign_key(self, newKey):
        print(f'Переназначаем: {self.__keyName} -> {newKey.getName()}')
        self.__control = newKey.control


class Controls:
    def open(self):
        print("Open app")

    def close(self):
        print("Close app")


class Actions:
    def __init__(self):
        self.__actions = []

    def getActions(self):
        return self.__actions

    def addAction(self, key):
        self.__actions.append(key)
        key.control.open()
        time.sleep(0.5)

    def CancelLastAction(self):
        if len(self.__actions) > 0:
            last_action = self.__actions.pop()
            print(f'Последние нажатие - {last_action.getName()}')
            time.sleep(0.5)
            last_action.control.close()
        else:
            print('Нет событий нажатия')

    def printActions(self):
        for i in self.__actions:
            print(i.getName())


if __name__ == '__main__':
    actions = Actions()
    app = Key("Telegram", Controls())
    actions.addAction(app)
    actions.printActions()
    print("----------")

    actions.CancelLastAction()
    actions.printActions()
    print("----------")

    # Пример демонстрации нажатия комбинаций клавиш
    key1 = Key('Ctrl+C', Controls())
    actions.addAction(key1)
    key2 = Key('Ctrl+V', Controls())
    actions.addAction(key2)

    key3 = Key('X', Controls())
    key4 = Key('Y', Controls())
    actions.addAction(key3)
    actions.addAction(key4)
    actions.printActions()
    print("----------")
    actions.CancelLastAction()
    actions.printActions()

    print("----------")
    key3 = Key('Ctrl+Q', Controls)
    key2.reassign_key(key3)
    actions.printActions()
    print("----------")
