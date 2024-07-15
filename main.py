# class Device:
#     def __init__(self, name, year, manufacturer, price):
#         self.name = name
#         self.year = year
#         self.manufacturer = manufacturer
#         self.price = price

#     def information(self):
#         return f"Name: {self.name}\nYear: {self.year}\nManufacturer: from {self.manufacturer}\nPrice: {self.price}million $"

# class CoffeMachine(Device):
#     def __init__(self,name,year, manufacturer, price, num_of_type_coffe):
#         super().__init__(name,year, manufacturer, price)
#         self.coffe = num_of_type_coffe

#     def information(self):
#         main_info = super().information()
#         return f"{main_info}\nNumber of coffe: {self.coffe} tasty type\n"
    
# class Blender(Device):
#     def __init__(self,name,year, manufacturer, price, rotational_speed):
#         super().__init__(name,year, manufacturer, price)
#         self.speed = rotational_speed

#     def information(self):
#         main_info = super().information()
#         return f"{main_info}\nRotational speed: {self.speed} rotate/sec\n"
    
# class MeatGrinder(Device):
#     def __init__(self,name,year, manufacturer, price, rotational_power):
#         super().__init__(name,year, manufacturer, price)
#         self.power = rotational_power

#     def information(self):
#         main_info = super().information()
#         return f"{main_info}\nRotational power: {self.power}W"
    


# global_coffe = CoffeMachine('Global coffe machine',2015, 'England', 105, 10)
# print(global_coffe.information())

# huawei_blender = Blender('Huawei blender',2010, 'China', 39.5, 27)
# print(huawei_blender.information())

# teffal = MeatGrinder('Teffal meat grinder',2023, 'Poland', 48, 120)
# print(teffal.information())





# class Ship:
#     def __init__(self, name, year, manufacturer, price, speed):
#         self.name = name
#         self.year = year
#         self.manufacturer = manufacturer
#         self.price = price
#         self.speed = speed

#     def information(self):
#         return f"Name: {self.name}\nYear: {self.year}\nManufacturer: from {self.manufacturer}\nPrice: {self.price} million $\nSpeed: {self.speed}km/h\n"

# class Frigate(Ship):
#     def __init__(self,name,year, manufacturer, price, speed, weapon_capacity):
#         super().__init__(name,year, manufacturer, price, speed)
#         self.frigate = weapon_capacity

#     def information(self):
#         main_info = super().information()
#         return f"{main_info}Weapon capacity: {self.frigate} tons\n"
    
# class Destroyer(Ship):
#     def __init__(self,name,year, manufacturer, price, speed, num_of_destroyed_ships):
#         super().__init__(name,year, manufacturer, price, speed)
#         self.dest = num_of_destroyed_ships

#     def information(self):
#         main_info = super().information()
#         return f"{main_info}Number of destroyed ships: {self.dest}\n"
    
# class Cruiser(Ship):
#     def __init__(self,name,year, manufacturer, price, speed, people_capacity):
#         super().__init__(name,year, manufacturer, price, speed)
#         self.people_capacity = people_capacity

#     def information(self):
#         main_info = super().information()
#         return f"{main_info}Capacity: {self.people_capacity} people"
    


# ship_1 = Frigate('Frigate MZ-12',1945, 'USA', 5, 80, 10)
# print(ship_1.information())

# ship_2 = Destroyer('Destroyer JkS-700',1988, 'Russia', 12, 110, 19)
# print(ship_2.information())

# ship_3 = Cruiser('Titanik',1934, 'USA', 100, 70, 10000)
# print(ship_3.information())










# import math

# class Square:
#     def __init__(self, side):
#         self.side = side
    
#     def area(self):
#         return f"Square area: {self.side ** 2}"
    
#     def perimeter(self):
#         return f"Square perimetr: {4 * self.side}"
    
#     def display_info(self):
#         return f"Square side length: {self.side}\n"


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         return f"Circle area: {math.pi * self.radius ** 2}"
    
#     def circumference(self):
#         return f"Circle circumference: {2 * math.pi * self.radius}"
    
#     def display_info(self):
#         return f"Circle radius: {self.radius}"
    

# class Circle_in_square(Square, Circle):
#     def __init__(self, side):
#         Square.__init__(self, side)
#         Circle.__init__(self, side / 2)
    
#     def display_info(self):
#         square_info = Square.display_info(self)
#         circle_info = Circle.display_info(self)
#         return f"{square_info}\n{circle_info}"


# square = Square(10)
# print(square.area())
# print(square.perimeter())
# print(square.display_info())

# circle = Circle(23)
# print(circle.area())
# print(circle.circumference())
# print(circle.display_info())

# result = Circle_in_square(18)
# print(result.display_info())








# class Wheels:
#     def __init__(self, size, season):
#         self.size = size
#         self.season = season
    
#     def describe_wheels(self):
#         return f"Колеса размером {self.size} дюйма, предназначенных для {self.season} дороги"

# class Motor:
#     def __init__(self, fuel_consumption, power):
#         self.fuel_consumption = fuel_consumption
#         self.power = power
    
#     def describe_engine(self):
#         return f"Расход топлива машины - {self.fuel_consumption}л, а мощность мотора {self.power} лошадинных сил."

# class Doors:
#     def __init__(self, color, material):
#         self.color = color
#         self.material = material
    
#     def describe_doors(self):
#         return f"Двери высокого качества, сделанных из {self.material} ,и имеют {self.color} цвет."

# class Car(Wheels, Motor, Doors):
#     def __init__(self, size, season, fuel_consumption, power,color, material):
#         Wheels.__init__(self, size, season)
#         Motor.__init__(self, fuel_consumption, power)
#         Doors.__init__(self, color, material)
    
#     def describe(self):
#         return (f"{self.describe_wheels()}\n"
#                 f"{self.describe_engine()}\n"
#                 f"{self.describe_doors()}")


# bmw_m5_competition_f90 = Car(22, 'летней', 10.8, 625, 'черный', 'железа и кожи')
# print(bmw_m5_competition_f90.describe())








import json

class Shape:
    def show(self):
        raise NotImplementedError("Метод show() должен быть реализован в подклассе")
    
    def save(self, filename):
        with open(filename, 'w') as file:
            data = {
                'type': self.__class__.__name__,
                'attributes': self.__dict__
            }
            json.dump(data, file)
    
    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        shape_class = globals()[data['type']]
        return shape_class(**data['attributes'])

class Square(Shape):
    def __init__(self, x, y, side_length):
        self.x = x
        self.y = y
        self.side_length = side_length
    
    def show(self):
        return f"Square: Top-left corner ({self.x}, {self.y}), Side length {self.side_length}"

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def show(self):
        return f"Rectangle: Top-left corner ({self.x}, {self.y}), Width {self.width}, Height {self.height}"

class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    
    def show(self):
        return f"Circle: Center ({self.x}, {self.y}), Radius {self.radius}"

class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def show(self):
        return f"Ellipse: Top-left corner ({self.x}, {self.y}), Width {self.width}, Height {self.height}"

shapes = [
    Square(0, 0, 10),
    Rectangle(1, 1, 20, 10),
    Circle(2, 2, 5),
    Ellipse(3, 3, 15, 10)
]

for i, shape in enumerate(shapes):
    shape.save(f'shape_{i}.json')

loaded_shapes = [Shape.load(f'shape_{i}.json') for i in range(len(shapes))]

for shape in loaded_shapes:
    print(shape.show())
