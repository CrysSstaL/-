import time


class Key:
    def __init__(self, keyName):
        self.__keyName = keyName

    def getName(self):
        return self.__keyName

    def setName(self, newKey):
        self.__keyName = newKey

    def press_key(self):
        print(f'Нажата кнопка: {self.__keyName}')
        time.sleep(0.5)  # Задержка между нажатиями клавиш
        actions.addAction(self)

    def reassign_key(self, newKey, actions):
        print(f'Переназначаем: {self.__keyName} -> {newKey.getName()}')
        for i in range(len(actions.getActions())):
            if actions.getActions()[i].getName() == self.__keyName:
                actions.getActions()[i] = newKey


class Actions:
    def __init__(self):
        self.__actions = []

    def getActions(self):
        return self.__actions

    def addAction(self, key):
        self.__actions.append(key)

    def canselLastAction(self):
        if len(self.__actions) > 0:
            last_action = self.__actions.pop()
            print(f'Последние нажатие - {last_action.getName()}')
        else:
            print('Нет событий нажатия')

    def printActions(self):
        for i in self.__actions:
            print(i.getName())


if __name__ == '__main__':
    actions = Actions()
    # Пример демонстрации нажатия комбинаций клавиш
    key1 = Key('Ctrl+C')
    key1.press_key()
    key2 = Key('Ctrl+V')
    key2.press_key()
    actions.printActions()
    print("----------")
    # Пример отката последнего действия
    actions.canselLastAction()
    actions.printActions()
    print("----------")
    key2.press_key()
    actions.printActions()
    print("----------")
    # Пример переназначения клавиши
    key3 = Key('Ctrl+P')
    key2.reassign_key(key3, actions)
    actions.printActions()
    print("----------")
