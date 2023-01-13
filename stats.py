class Stats():
    """following statistics"""

    def __init__(self):
        """initialisation statistics"""
        self.reset_stats()
        self.run_game = True
        with open('high_score.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        """statistics changes in the game"""
        self.guns_left = 2
        self.score = 0
