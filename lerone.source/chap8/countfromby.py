class CountFromBy:
    
    def __init__(self, v: int=0, i: int=1) -> None:
        self.val = v
        self.incr = i

    #This function defines how objs are represented
    def __repr__(self) -> str:
        return str(self.val)
    
    def increase(self) -> None:
        self.val += self.incr

    
