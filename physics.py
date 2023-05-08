class Physics:
    def __init__(self) -> None:
        self.gravity = 9.8

    def calc_speed(self, d, t):
        self.speed = d / t
        return self.speed
    
    def calc_PE(self, m, h):
        pe = m * self.gravity * h
        return pe
    
    def calc_force(self, m, a):
        force = m * a
        return force
