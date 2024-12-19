from .constants import SQUARE_SIZE

class Candle:
    def __init__(self, row, col, stage, lit):
        self.row = row
        self.col = col
        self.stage = stage
        self.lit = lit

        self.x = 0
        self.y = 0
        self.calculate_position()

        def calculate_position(self):
            self.x = self.col * SQUARE_SIZE
            self.y = self.row * SQUARE_SIZE
        
        def lit_candle(self):
            self.lit = True
        
        def extinguish_candle(self):
            self.lit = False