import time


class Key:
    def __init__(self, keyName):
        self.keyName = keyName

    def getName(self):
        return self.keyName

    def setName(self, newKey):
        self.keyName = newKey

    def press_key(self):
        print(f'Нажата кнопка: {self.keyName}')
        time.sleep(0.5)  # Задержка между нажатиями клавиш
        actions.append(self)

    def reassign_key(self, newKey, actions):
        print(f'Переназначаем: {self.keyName} -> {newKey}')
        for action in actions:
            if action.getName() == self.keyName:
                action.setName(newKey)
        return actions


def undo_last_action(actions):
    if len(actions) > 0:
        last_action = actions.pop()
        print(f'Последнее нажатие - {last_action.getName()}')
    else:
        print('Нет последних нажатий')


def printActions(actions):
    for action in actions:
        print(action.getName())


if __name__ == '__main__':
    actions = []
    # Пример демонстрации нажатия комбинаций клавиш
    key1 = Key('Ctrl+C')
    key1.press_key()
    key2 = Key('Ctrl+V')
    key2.press_key()
    printActions(actions)
    print("----------")
    # Пример отката последнего действия
    undo_last_action(actions)
    printActions(actions)
    print("----------")
    key2.press_key()
    printActions(actions)
    print("----------")
    # Пример переназначения клавиши
    actions = key2.reassign_key('Ctrl+P', actions)
    printActions(actions)
    print("----------")
