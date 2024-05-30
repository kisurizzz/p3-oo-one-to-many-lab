class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception ('Invalid pet type') 
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

class Owner:
    def __init__(self , name ):
        self.name = name
        self._pets = []
        
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance (pet, Pet):
            raise Exception ('The pet must be an instace of Pet')
        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        my_pets = self.pets()
        sorted_pets = sorted (my_pets, key = lambda each_pet: each_pet.name.lower())
        return sorted_pets 
    