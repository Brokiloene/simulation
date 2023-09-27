from entities.animals.animal import Animal
from entities.animals.herbivore import Herbivore
from utils.bfs import Bfs


class Predator(Animal):
    def __init__(self, coordinate, board_size, terrain_graph, animal_graph, speed=3) -> None:
        super().__init__(coordinate, board_size, terrain_graph, animal_graph, speed)
        
        self._sprite = ' P '

    def is_coordinate_free_to_move(self, coordinate):
        is_passable = super().is_coordinate_free_to_move(coordinate)
        if not is_passable or (coordinate in self.a_graph and isinstance(self.a_graph[coordinate], Predator)):
            return False
            
        return True
    
    
    def make_move(self):
        path_to_target = Bfs.search(self, Herbivore, self.a_graph)

        if path_to_target:
            move_to = self.find_optimal_coordinate_to_move(path_to_target)
            
            del self.a_graph[self.crd]
            self.a_graph[move_to] = self
            self.crd = move_to
            return
        else:
            self.make_random_move()
