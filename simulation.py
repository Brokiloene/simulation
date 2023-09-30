import time

from console_renderer import SimulationConsoleRenderer
from simulation_map import SimulationMap

class Simulation:
    def __init__(self, board_size_row=10, board_size_col=10):
        self.map = SimulationMap(board_size_row, board_size_col)
        
        self.turns_cnt = 0
        self.renderer = SimulationConsoleRenderer(self.map)

        self.map.init_map_random()
    

    def render(self):
        self.renderer.render(self.turns_cnt)


    def next_turn(self):
        self.render()
        self.turns_cnt += 1

        for animal in self.map.get_animals:
            if self.map.is_object_exists(animal):
                animal.make_move()
                self.render()
                time.sleep(0.8)

        

if __name__ == '__main__':
    
    sim = Simulation(10, 10)
    # sim.init_map_random()

    while True:
        # time.sleep(1)
        sim.next_turn()
