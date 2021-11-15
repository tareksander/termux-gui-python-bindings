
class Event:
    
    def __init__(self, ev):
        self.type = ev["type"]
        try:
            self.value = ev["value"]
            if type(self.value) is dict:
                self.aid = self.value["aid"]
                self.id = self.value["id"]
        except KeyError:
            pass
        
    
