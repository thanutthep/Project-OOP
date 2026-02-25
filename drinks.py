from pyscript import document, when
from js import window


class Drink:
    def __init__(self, name, price, sugar_level):
        self.name = name
        self.price = price
        self.sugar_level = sugar_level

    def get_description(self):
        return f"{self.name} ราคา {self.price} บาท ระดับความหวาน {self.sugar_level}"


class Coffee(Drink):
    def __init__(self):
        super().__init__("กาแฟเย็น", 45, "หวานน้อย")


class MilkTea(Drink):
    def __init__(self):
        super().__init__("ชานมไข่มุก", 55, "หวานปานกลาง")


class Smoothie(Drink):
    def __init__(self):
        super().__init__("สมูทตี้ผลไม้รวม", 65, "หวานน้อย-ปานกลาง")


@when("click", "#btn_show")
def show_drink(event):
    choice = document.getElementById("drink_selector").value
    drink = None

    if choice == "coffee":
        drink = Coffee()
    elif choice == "milktea":
        drink = MilkTea()
    elif choice == "smoothie":
        drink = Smoothie()

    if drink:
        text = drink.get_description()
        window.alert(f"คุณเลือก {drink.name}")
        document.getElementById("output").innerText = text