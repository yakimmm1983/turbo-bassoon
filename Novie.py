# class Animal:
#
#     def __init__(self,type,location,age):
#         self.type = type
#         self.location = location
#         self.age = age
#
#     def getInfo(self):
#         return{"Тип": self.type,
#                "Ареал обитания": self.location,
#                "Возраст":self.age}
#
#     def setLocation(self):
#         location = input("введите среду обитания животного")
#         self.location = location

# class Animal:
#
#     def __init__(self,type,speed):
#         self.type = type
#         self.speed = speed
#     def getType(self):
#         return self.type
#     def getSpeed(self):
#         return self.speed

class car:
    def __init__(self,avto,color,motor,body):
        self.avto = avto
        self.color = color
        self.motor = motor
        self.body = body

    def getCar(self):
        return {"модель": self.avto,
                "цвет":self.color,
                "мотор": self.motor,
                "кузов": self.body}
