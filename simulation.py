import time

from console_renderer import SimulationConsoleRenderer
from simulation_map import SimulationMap
from actions import SpawnGrass, SpawnHerbivore, SpawnPredator, SpawnRock, SpawnTree


class Simulation:
    def __init__(self, board_size_row=10, board_size_col=10, search_algorithm="A*"):
        self.map = SimulationMap(board_size_row, board_size_col, search_algorithm)
        
        self.turns_cnt = 0
        self.renderer = SimulationConsoleRenderer(self.map)

        self.init_actions = [SpawnRock, SpawnGrass, SpawnTree, SpawnHerbivore, SpawnPredator]
        self.turn_actions = [SpawnGrass, SpawnHerbivore]
    

    def start(self, debug=False):
        if debug:
            self.map.init_map_manual()
        else:
            msg = "Generating: "
            
            for action in self.init_actions:
                cur_action = action(self.map)

                self.render(msg, cur_action.msg)
                cur_action.perform()

                time.sleep(1.5)

        while True:
            try:
                self.next_turn()
            except KeyboardInterrupt:
                print("\nStopping simulation...")
                break


    def render(self, msg="", action_msg=""):
        self.renderer.render(msg, action_msg)


    def next_turn(self):
        self.turns_cnt += 1
        msg = f"TURN: {self.turns_cnt}"

        for action in self.turn_actions:
            cur_action = action(self.map)

            if cur_action.need_to_perform():
                self.render(msg, cur_action.msg)
                time.sleep(0.75)
                cur_action.perform()
                self.render(msg, cur_action.msg)

        self.render(msg)
        for animal in self.map.get_animals:
            if self.map.is_object_exists(animal):
                animal.make_move()
                self.render(msg)
                time.sleep(0.75)
