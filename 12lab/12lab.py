# 12.1)	На основе ранее созданного класса Restaurant из прошлого задания создайте разновидность ресторана – «Кафе-мороженое».
# Напишите класс IceCreamStand, наследующий от класса Restaurant. Добавьте атрибут с именем flavors для хранения списка сортов мороженого.
# Напишите метод, который выводит этот список. Создайте экземпляр IceCreamStand и вызовите этот метод.
def first():
    class restaurant:
        def __init__(self, restaurant_name, cuisine_type, restaurant_rating):
            self.restaurant_rating = restaurant_rating
            self.restuarant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            description = f"ресторан '{self.restuarant_name}' кухня '{self.cuisine_type}, рейтинг '{self.restaurant_rating}'. доступный"
            return description

    class IceCreamStand(restaurant):
        def __init__(self, flavors, restaurant_name, cuisine_type, restaurant_rating):
            super().__init__(restaurant_name, cuisine_type, restaurant_rating)
            self.flavors = flavors
        def describe_icecream(self, typesss):
            typesss = f"список сортов '{self.flavors}'"
            return typesss

    typesss = ["клубничное", "шоколадное", "ванильное", "вкусное"]

    newflawors = IceCreamStand(typesss, "круто", "мороженщица", 5)
    message1 = newflawors.describe_restaurant()
    message = newflawors.describe_icecream(typesss)
    print(message1, message)

# 12.2)	Модифицировать ранее созданный класс IceCreamStand:
# 1.	Добавить атрибуты для описания локации и времени работы кафе-мороженого.+
# 2.	Реализовать методы для добавления и удаления сортов мороженого из списка flavors.+
# 3.	Реализовать метод для проверки наличия определенного сорта мороженого в списке flavors.+
# 4.	Добавить методы для разных типов мороженого (например, мороженое на палочке, мягкое мороженое, и т.д.) и реализовать методы для работы с каждым типом.
def third():
    class restaurant:
        def __init__(self, restaurant_name, cuisine_type, restaurant_rating, restaurant_location, restaurant_schedule):
            self.restaurant_rating = restaurant_rating
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.restaurant_location = restaurant_location
            self.restaurant_schedule = restaurant_schedule
        def describe_restaurant(self):
            description = f"ресторан '{self.restaurant_name}' кухня '{self.cuisine_type}, рейтинг '{self.restaurant_rating}', местоположение '{self.restaurant_location}', рабочие часы '{self.restaurant_schedule}'"
            return description
    class IceCreamStand(restaurant):
        def __init__(self, restaurant_name, flavors, type_icecream, cuisine_type, restaurant_rating, restaurant_location, restaurant_schedule):
            super().__init__(restaurant_name, cuisine_type, restaurant_rating, restaurant_location, restaurant_schedule)
            self.flavors = flavors
            self.type_icecream = type_icecream

        def display_flavors(self):
            print("cписок сортов мороженого:")
            for flavor in self.flavors:
                print(flavor)
        def display_types(self):
            print("cписок типов мороженого:")
            for type_icecream in self.type_icecream:
                print(type_icecream)

        def add_flavor(self, new_flavor):
            self.flavors.append(new_flavor)
        def add_type(self, new_type):
            self.type_icecream.append(new_type)

        def remove_flavor(self, flavor):
            if flavor in self.flavors:
                self.flavors.remove(flavor)
            else:
                print(f"сорт мороженого '{flavor}' есть в наличии")
        def remove_type(self, type_icecream):
            if type_icecream in self.type_icecream:
                self.type_icecream.remove(type_icecream)
            else:
                print(f"тип мороженого '{flavor}' нет в наличии")


        def check_flavor(self, flavor):
            if flavor in self.flavors:
                print(f"сорт мороженого '{flavor}' есть в наличии")
            else:
                print(f"сорт мороженого '{flavor}' нет в наличии")
        def check_type(self, type_icecream):
            if type_icecream in self.type_icecream:
                print(f"тип мороженого '{type_icecream}' есть в наличии")
            else:
                print(f"сорт мороженого '{type_icecream}' нет в наличии")

    newflavors = IceCreamStand("круто", ["клубничное", "шоколадное", "ванильное", "вкусное"], ["фруктовый лёд", "щербет", "на палочке", "жареное"], "мороженщица", 5, "ул. некрасова 6", "9:00-23:00")
    print(newflavors.describe_restaurant())
    print(f"локация: '{newflavors.restaurant_location}'")
    print(f"время работы: {newflavors.restaurant_schedule}")
    ask1 = input("добавить морожку ")
    ask1a = input("добавить тип мороженого ")
    ask2 = input("убрать морожку ")
    ask2a = input("убрать тип мороженого ")
    ask3 = input("проверка морожки ")
    ask3a = input("проверка типа мороженого ")
    newflavors.add_flavor(ask1)
    newflavors.add_type(ask1a)
    newflavors.remove_flavor(ask2)
    newflavors.remove_type(ask2a)
    newflavors.check_flavor(ask3)
    newflavors.check_type(ask3a)
    newflavors.display_flavors()
    newflavors.display_types()

# 12.3)	Создать класс IceCreamStand для кафе мороженого и используя библиотеку tkinter построить простой графический интерфейс, показанный на рисунке, приложенном к задаче.
def interrr():
    class IceCreamStand:
            def __init__(self, flavors):
                self.flavors = flavors
            def describe_icecream(self, typesss):
                typesss = f"список сортов '{self.flavors}'"
                return typesss
    typesss = ["клубничное", "шоколадное", "ванильное", "вкусное"]
    newflawors = IceCreamStand(typesss)
    message = newflawors.describe_icecream(typesss)
    import tkinter as tk
    from PIL import Image, ImageTk
    root = tk.Tk()
    root.title("графический интерфейс")
    image = Image.open("12lab.png")
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo)
    label.pack()
    text = "\n".join(typesss)
    text1_label = tk.Label(root, text="Список мороженого:", justify="left", font=("Helvetica", 15))
    text1_label.place(relx=0.125, rely=0.2, anchor="nw")
    text_label = tk.Label(root, text=text, justify="left", font=("Helvetica", 12))
    text_label.place(relx=0.125, rely=0.25, anchor="nw")
    root.mainloop()

first(), third(), interrr()