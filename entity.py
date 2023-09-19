import random
import itertools


class Entity:
    """
    Базовый класс. Хранит свои координаты и размеры игровой доски.
    """
    def __init__(self, x, y, board_size_x, board_size_y) -> None:
        self.pos_x = x
        self.pos_y = y
        self.board_size_x = board_size_x
        self.board_size_y = board_size_y
    
    # def __hash__(self) -> int:
    #     return hash(self.pos_x, self.pos_y)
    
    # def __eq__(self, other):
    #     return (self.pos_x, self.pos_y) == (other.pos_x, other.pos_y) 

    def is_coordinate_valid(self, cord):
        return 0 <= cord[0] < self.board_size_x and \
               0 <= cord[1] < self.board_size_y
 

    @property
    def neighbor_coordinates(self):
        """
        Вернёт список кортежей -- координаты клеток-соседей self
        """
        neighbor_coordinates = []

        for shift in ((1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1)):
            cur = (self.pos_x + shift[0], self.pos_y + shift[1])
            if self.is_coordinate_valid(cur):   
               neighbor_coordinates.append((self.pos_x + shift[0], self.pos_y + shift[1]))

        return neighbor_coordinates
    
    @property
    def coordinates(self):
        return (self.pos_x, self.pos_y)
    
    def __str__(self) -> str:
        return f"Entity: ({self.pos_x}, {self.pos_y})"
    
    def __repr__(self) -> str:
        return f"Entity({self.pos_x}, {self.pos_y}, {self.board_size_x}, {self.board_size_y})"
    

class Terrain(Entity):
    def __init__(self, x, y, board_size_x, board_size_y) -> None:
        super().__init__(x, y, board_size_x, board_size_y)
    #     self.creatures_on_this_terrain = []
    
    # @property
    # def creatures_on_this_terrain(self):
    #     return self.creatures_on_this_terrain
    
    # def add_creature_on_this_terrain(self, creature):
    #     self.creatures_on_this_terrain.append(creature)

    # def rm_creature_on_this_terrain
    
    # Лучше будет создать отдельный словарь для объектов местности и животных
    # Чтобы местность не пропадала после того как по ним прошлось животное

    @property
    def name(self):
        return type(self).__name__


class Grass(Terrain):
    def __str__(self) -> str:
        return random.choice(['`', '"', "'", ','])


class Rock(Terrain):
    def __str__(self) -> str:
        return random.choice(['•', '.', '·'])


class Tree(Terrain):
    def __str__(self) -> str:
        return random.choice(['║', '│'])


class Creature(Entity):
    def __init__(self, x, y, board_size_x, board_size_y, speed, hp, graph) -> None:
        super().__init__(x, y, board_size_x, board_size_y)
        self.speed = speed
        self.hp
        self.graph = graph
# Сделать это абстрактным методом    
    def make_move(self, graph, dest):
        pass
    
    @property
    def possible_move_coordinates(self):
        """
        Лист кортежей всех координат, на которые может перейти данное существо
        """
        move_ranges = [x for x in range(-self.speed, self.speed + 1)]

        shifts = list(itertools.product(move_ranges, repeat=2))

        possible_moves = [(self.pos_x + x[0], self.pos_y + x[1]) for x in shifts]

        return filter(self.is_coordinate_valid, possible_moves)



class Herbivore(Creature):
    def make_move(self, dest):
        path_to_target = BFS(self.graph).search(self.coordinates, 'Grass')
        possible_moves = self.possible_move_coordinates

        if path_to_target is not None:
            for cord in path_to_target:
                pass



    # def get_neighbor_coordinates(self):
    #     moves = filter(lambda x: isinstance(self.graph[x], Terrain), super().get_neighbor_coordinates())



class BFS:
    def __init__(self, graph) -> None:
        self.graph = graph
        self.visited = set()
        self.queue = []

    def search(self, start_cord, target):
        self.queue.append(start_cord)

        parents = {start_cord: start_cord}
        start_path = None

        while self.queue:
            cur = self.queue.pop(0)
            self.visited.add(cur)

            if self.graph[cur].name == target:
                start_path = cur
                break
    
            for new_cords in self.graph[cur].get_neighbor_coordinates():
                if new_cords not in self.visited and new_cords not in self.queue:
                    self.queue.append(new_cords)
                    parents[new_cords] = cur
        else:
            return None
        
        path = []
        while parents[start_path] != start_path:
            path.append(start_path)
            start_path = parents[start_path]
        return path
    
    


if __name__ == '__main__':


    d = {}
    for i in range(3):
        for j in range(4):
            d[(i, j)] = Rock(i, j, 3, 4)
    d[(2,3)] = Grass(i, j, 3, 4)
    for i in range(3):
        for j in range(4):
            print(d[(i, j)], end=' ')
        print()

    # print(d[(1, 1)].get_neighbours_coordinates())
    bfs = BFS(d)
    print(bfs.search((0, 0), 'Grass'))

# bfs сделать поиск пути до цели