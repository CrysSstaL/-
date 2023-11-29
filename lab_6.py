class Control:
    def __init__(self):
        self.x = 0
        self.y = 0

    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def getPosition(self):
        print(f"Вызван метод getPosition из контролла {type(self).__name__}")
        return "(" + str(self.x) + ", " + str(self.y) + ")"


# Класс формы
class Form(Control):
    def __init__(self):
        super().__init__()
        self.controls = []
        print("Создана форма!")

    def addControl(self, control):
        self.controls.append(control)

    def getControls(self):
        return self.controls

    def getInfo(self):
        print("-----------form-----------")
        print("Cоздали форму с координатами" + self.getPosition())


        for i in self.getControls():
            if type(i).__name__ != "ComboBox":
                print()
                print(f"{type(i).__name__} = " + i.getText())
                print(f"{type(i).__name__} Coords = " + i.getPosition())
            else:
                print()
                print(f"{type(i).__name__} : ")
                for j in i.getItems():
                    print("   - " + j)
                print(f"{type(i).__name__} Coords = " + i.getPosition())

        print("---------------------------")


class Label(Control):
    def __init__(self):
        super().__init__()
        self.text = ""

    def setText(self, text):
        print("Вызван метод setText у контролла Label")
        self.text = text

    def getText(self):
        print("Вызван метод getText у контролла Label")
        return self.text


class TextBox(Control):
    def __init__(self):
        super().__init__()
        self.text = ""

    def setText(self, text):
        print("Вызван метод setText у контролла TextBox")
        self.text = text

    def getText(self):
        print("Вызван метод getText у контролла TextBox")
        return self.text

    def onValueChanged(self):
        print("Вызван метод onValueChanged у контролла TextBox")


class ComboBox(Control):
    def __init__(self):
        super().__init__()
        self.selectedIndex = -1
        self.items = []

    def setSelectedIndex(self, index):
        print("Вызван метод setSelectedIndex у контролла ComboBox")
        self.selectedIndex = index

    def getSelectedIndex(self):
        print("Вызван метод getSelectedIndex у контролла ComboBox")
        return self.selectedIndex

    def setItems(self, items):
        print("Вызван метод setItems у контролла ComboBox")
        self.items = items

    def getItems(self):
        print("Вызван метод getItems у контролла ComboBox")
        return self.items


class Button(Control):
    def __init__(self):
        super().__init__()
        self.text = ""

    def setText(self, text):
        print("Вызван метод setText у контролла Button")
        self.text = text

    def getText(self):
        print("Вызван метод getText у контролла Button")
        return self.text

    def click(self):
        print("Вызван метод click у контролла Button")


class AbstractFactory:
    def createForm(self):
        pass

    def createLabel(self):
        pass

    def createTextBox(self):
        pass

    def createComboBox(self):
        pass

    def createButton(self):
        pass


class WindowsFactory(AbstractFactory):
    def __init__(self):
        print("Создан обьект Windows приложения")

    def createForm(self):
        return Form()

    def createLabel(self):
        return Label()

    def createTextBox(self):
        return TextBox()

    def createComboBox(self):
        return ComboBox()

    def createButton(self):
        return Button()


class LinuxFactory(AbstractFactory):
    def __init__(self):
        print("Создан обьект Linux приложения")

    def createForm(self):
        return Form()

    def createLabel(self):
        return Label()

    def createTextBox(self):
        return TextBox()

    def createComboBox(self):
        return ComboBox()

    def createButton(self):
        return Button()


class MacOSFactory(AbstractFactory):
    def __init__(self):
        print("Создан обьект MacOS приложения")

    def createForm(self):
        return Form()

    def createLabel(self):
        return Label()

    def createTextBox(self):
        return TextBox()

    def createComboBox(self):
        return ComboBox()

    def createButton(self):
        return Button()


def main():
    # Создание фабрики для нужной операционной системы
    factory = MacOSFactory()

    # factory = LinuxFactory()

    # Создание формы
    form = factory.createForm()

    # Создание контроллов
    label = factory.createLabel()
    textbox = factory.createTextBox()
    combobox = factory.createComboBox()
    button = factory.createButton()

    # Задание параметров
    label.setText("Кинотеатр 'Люмен'!")
    label.setPosition(0, 1)

    textbox.setText("Выберите кино:")
    textbox.setPosition(1, 3)

    combobox.setItems(["Форсаж", "Лекция по ООП", "Голодные игры"])
    combobox.setSelectedIndex(1)
    combobox.setPosition(1, 5)

    button.setText("Подтвердить")
    button.setPosition(6, 6)

    # Добавление контролов на форму
    form.addControl(label)
    form.addControl(textbox)
    form.addControl(combobox)
    form.addControl(button)

    form.getInfo()


if __name__ == "__main__":
    main()
