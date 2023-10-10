



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

import scvear
array = scvear.mnog()
print(scvear.mnog())

scvear.summ(array)
print(scvear.summ(array))