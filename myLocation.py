class Location:
    def __init__(self, name, country) -> None:
        self.name = name
        self.country = country
    
    def myLocation(self):
        print("Hi, my name is " + self.name + " and I live in " + self.country + ".")

loc1 = Location("Paredes", "Argentina")
loc2 = Location("Locatelli", "Italy")
loc3 = Location("Vlahovic", "Serbia")
loc1.myLocation()
loc2.myLocation()
loc3.myLocation()
your_loc = Location("Widad", "Indonesia")
your_loc.myLocation()
        


