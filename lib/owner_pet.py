class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    
    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.add_pet(self)
        
    @property
    def pet_type(self):
        return self._pet_type
        
    @pet_type.setter
    def pet_type(self, value):
        if value not in Pet.PET_TYPES:
            raise ValueError("Not")
        else:
            self._pet_type = value
            
    @classmethod
    def add_pet(cls, self):
        cls.all.append(self)
    

class Owner:
    def __init__(self, name):
        self.name = name
        
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise ValueError("Not")
        pet.owner = self        
        
    def get_sorted_pets(self):
        return sorted([pet for pet in Pet.all if pet.owner == self], key=lambda pet:pet.name)

                    
                