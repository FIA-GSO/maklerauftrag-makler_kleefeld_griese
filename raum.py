class Raum:
    def __init__(self, Name, Länge, Breite):
        self.Name = Name
        self.Länge = Länge
        self.Breite = Breite

    def getFläche(self):
        return self.Länge*self.Breite
    
    def getName(self):
        return self.Name
    
    def setName(self, Name):
        self.Name = Name

    