from Entities import Campo

class Posicion:

    def moverN (self):
        return [self.x % Campo.tamX, self.y+1 % Campo.tamY]

    def moverNE (self):
        return [self.x+1 % Campo.tamX, self.y+1 % Campo.tamY]

    def moverE (self):
        return [self.x+1 % Campo.tamX, self.y % Campo.tamY]

    def moverES (self):
        return [self.x+1 % Campo.tamX, self.y-1 % Campo.tamY]

    def moverS (self):
        return [self.x % Campo.tamX, self.y-1 % Campo.tamY]

    def moverSO (self):
        return [self.x-1 % Campo.tamX, self.y-1 % Campo.tamY]

    def moverO (self):
        return [self.x-1 % Campo.tamX, self.y % Campo.tamY]

    def moverON (self):
        return [self.x-1 % Campo.tamX, self.y+1 % Campo.tamY]
