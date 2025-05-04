class Turtle(object):

    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = abs(s)

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s > 1:
            self.s -= 1
        return "Шаг не может быть меньше 1"
    
    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        
        moves_x = round(dx / self.s)
        moves_y = round(dy / self.s)

        return moves_x + moves_y

turtle = Turtle(s=-1)
print(turtle.count_moves(-9,10))

