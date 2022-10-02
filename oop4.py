class dog():
    species = 'mamal'
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
myDog = dog(breed = "Hasky",name = "my Dog")
print(myDog.breed)
print(myDog.name)
print(myDog.species)

