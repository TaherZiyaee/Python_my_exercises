class School():
    def __init__(self,name,capacity,city):
        self.name=name
        self.capacity=capacity
        self.city=city

    def __str__(self):
        return f"School Name: {self.name}\nCapacity: {self.capacity}\nCity: {self.city}\n\n"

rohollah_school = School("Rohollah",250,"Tehran")
peyvand_school = School("Peyvand",180,"Gorgan")

print(rohollah_school)
print(peyvand_school)

