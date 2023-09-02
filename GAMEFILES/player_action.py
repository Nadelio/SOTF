from abc import ABC, abstractmethod


# Dictionary that contains all actions
all_actions = {}

class PlayerAction(ABC):
    def __init__(self, name):
        self.name = name
        all_actions[self.name] = self
    
    @abstractmethod
    def action(self):
        pass
    

class City(PlayerAction):
    
    def __init__(self):
        super().__init__("city")
        
    def action(self):
        # Action code here
        pass #Not necessary, implement your own code and remove this
    
    