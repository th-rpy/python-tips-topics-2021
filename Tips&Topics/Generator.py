class xyrange:
    
    def __init__(self, nx, ny, startx = 0, starty = 0, stepx = 1, stepy = 1):
        
        self.ix = startx
        self.iy = starty
        self.nx = nx 
        self.ny = ny
        self.stepx = stepx
        self.stepy = stepy 

    def __iter__(self):
        return self

    def __next__(self):
        
        if self.ix < self.nx and self.iy < self.ny:
            ix = self.ix
            iy = self.iy
            self.ix += self.stepx 
            self.iy += self.stepy
            return ix, iy
        
        elif self.ix == self.nx and self.iy < self.ny:
            iy = self.iy
            self.iy += self.stepy
            return self.ix - self.stepx, iy
        
        elif self.ix < self.nx and self.iy == self.ny:
            ix = self.ix
            self.ix += self.stepx
            return ix, self.iy - self.stepy
        
        else:
            raise StopIteration() 
   
print(list(zip(range(0, 8, 2),
               range(0, 8, 2)))) # [(0, 0), (2, 2), (4, 4), (6, 6)]

print(list(xyrange(nx = 8, ny = 8, 
                   startx = 0, starty = 0, 
                   stepx = 2, stepy = 2))) # [(0, 0), (2, 2), (4, 4), (6, 6)]

print(list(xyrange(nx = 8, ny = 6, 
                   startx = 0, starty = 0, 
                   stepx = 2, stepy = 2))) # [(0, 0), (2, 2), (4, 4), (6, 4)]

iter_ = list(xyrange(nx = 8, ny = 6, 
                     startx = 0, starty = 0, 
                     stepx = 2, stepy = 2)) 
print(next(iter_)) # (0, 0)
