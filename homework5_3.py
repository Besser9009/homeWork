
class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors or self.buildingType == other.buildingType

    def __lt__(self, other):
        return self.numberOfFloors < other.numberOfFloors

    def __gt__(self, other):
        return self.numberOfFloors > other.numberOfFloors

build1 = Building(14, "Дом")
build2 = Building(13, "Отель")

print(build1 == build2)
print(build1 > build2)

