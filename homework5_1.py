
class House:
    def __init__(self, name, number_of_floors):
        self.name =name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        self.new_floor = new_floor
        if 0 < self.new_floor < self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print("Такого этажа не существует.")

house1 = House("ЖК Эльбрус", 30)
house2 = House("ЖК Европейский", 27)

house1.go_to(15)
house2.go_to(29)
