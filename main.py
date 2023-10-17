



# def Vibor():
#     while True:
#         figura = input("Выберите фигуру: прямоугольник,круг,трапеция,треугольник  ")
#         raschet = input("Что вы хотите расчитать: площадь,периметр фигуры  ")
#         if raschet == "площадь":
#             print(ploshad(figura))
#         if raschet == "периметр":
#             print(perimetr(figura))
#
# def ploshad(figura):
#         if figura == "прямоугольник":
#             pr = int(input("введите сторону а: "))
#             pr1 = int(input("введите сторону b: "))
#             print(pr+pr+pr1+pr1)
#         if figura == "круг":
#             kr = int(input("введите радиус круга: "))
#             print(3.14*(kr**2))
#         if figura == "трапеция":
#             tr1 = int(input("введите сторону а: "))
#             tr2 = int(input("введите сторону b: "))
#             tr3 = int(input("введите сторону h: "))
#             print(((tr1+tr2)*tr3)/2)
#         if figura == "треугольник":
#             treug1 = int(input("введите сторону а: "))
#             treug2 = int(input("введите сторону b: "))
#             print((treug1*treug2)/2)
#
# def perimetr(figura):
#         if figura == "прямоугольник":
#             pr = int(input("введите сторону а: "))
#             pr1 = int(input("введите сторону b: "))
#             print(pr*pr1)
#         if figura == "круг":
#             kr = int(input("введите радиус круга: "))
#             print((2*3.14)*kr)
#         if figura == "трапеция":
#             tr1 = int(input("введите сторону а: "))
#             tr2 = int(input("введите сторону b: "))
#             tr3 = int(input("введите сторону c: "))
#             tr4 = int(input("введите сторону d: "))
#             print(tr1+tr2+tr3+tr4)
# Vibor()
#
# import scvear
# scvear.circle(10)
# from scvear import circle
# circle(10)

# import scvear
# array = scvear.mnog()
# print(scvear.mnog())
#
# scvear.summ(array)
# print(scvear.summ(array))



# from random import randint
# array = []
# for i in range(100):
#     array.append(randint(1,20))
#
# def mnog():
#     mno = set(array)
#     array1 = list(mno)
#     return array1
#
# def summ(array1):
#     summ = len(array1)
#     return summ

# from Novie import Animal
# wolf = Animal("волк","лес",12)
# pig = Animal("свинья","город",4)
# animals = [wolf,pig]
# for animal in animals:
#     print(animal.getInfo())
#     animal.setLocation()

# from Novie import Animal
# from random import randint
# animals = []
# animalName = ["Заяц","Черепаха","Утка","Гусь","Собака"]
# for name in animalName:
#     animals.append(Animal(name,randint(100,200)))
#
# road = int(input("введите длинну дороги"))
# for animal in animals:
#     if animal.getSpeed() >= road:
#         print(f"{animal.getType()} пробежал")
#     else:
#         print(f"{animal.getType()} сошел с дистанции")


# from Novie import car
#
# bmv = car("bmv","синий","мустанг","седан" )
# lada = car("lada","красный","большой","хечбек")
# china = car("china","черный","ломается","кабриолет")
# cars = [bmv,lada,china]
# for bibi in cars:
#     print(bibi.getCar())

# array = range(10)
# array = list(map(lambda x: x**2,array))
# print(array)
#
# array = range(10)
# array = list(filter(lambda x: x%2==0,array))
# print(array)
#
# from functools import reduce
# array = range(1,10)
# array = reduce(lambda x,y: x*y,array,1) #колличество повторений (1) в конце по умолчанию 1
# print(array)
#
# with open("text.txt","w",encoding="utf-8") as file:
#     file.write("hello world")
# with open("text.txt","r",encoding="utf-8") as file:
#     print(file.read())


with open("некийтекстовый файл.txt","r",encoding="utf-8") as file:
    print(file.read())   #c ним не работает
    file.seek(0)     #обнуляет чтение файла txt
    files = len(list(filter(lambda x: str.isdigit(x),file.read())))
    print(f"колличество: {files}")



