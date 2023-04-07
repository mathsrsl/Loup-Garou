import utils

class Client:
    def __init__(self,name,classe):
        self.name = name
        self.classe = classe
        self.statue = utils.game.PlayerStatue.AWAKE
        
            
            
    def getName(self):
        return self.name
    def getClass(self):
        return self.classe
    def getStatue(self):
        return self.statue
    def setStatue(self,statue):
        self.statue = statue

