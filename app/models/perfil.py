class Personaje:
    def __init__(self,id, name, status, species, type, gender, origin, location, image,firstSeen):
        self.id=id
        self.name=name
        self.status=status
        self.species=species
        self.type=type
        self.gender=gender
        self.origin=origin
        self.location=location
        self.image=image
        self.firstSeen=firstSeen
        
    def to_json(self):
            return {
            "id":self.id,
            "name":self.name,
            "status":self.status,
            "species":self.species,
            "type":self.type,
            "gender":self.gender,
            "origin":self.origin,
            "location":self.location,
            "image":self.image,
            "firstSeen": self.firstSeen
            }