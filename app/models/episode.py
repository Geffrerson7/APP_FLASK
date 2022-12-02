class Episodio:
    def __init__(self,id, name, air_date, episode, characters, url, created):
        self.id=id
        self.name=name
        self.air_date=air_date
        self.episode=episode
        self.characters=characters
        self.url=url
        self.created=created
        
        
    def to_json(self):
            return {
            "id":self.id,
            "name":self.name,
            "air_date":self.air_date,
            "episode":self.episode,
            "characters":self.characters,
            "url":self.url,
            "created":self.created,
            
            }