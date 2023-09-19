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

    def get_neighbours_coordinates(self):
        """
        Вернёт список кортежей -- координаты клеток-соседей self
        """
        neighbours_coordinates = []
        for shift in ((1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1)):
            if (
                self.pos_x + shift[0] < self.board_size_x and
                self.pos_y + shift[1] < self.board_size_y and
                self.pos_x + shift[0] >= 0 and
                self.pos_y + shift[1] >= 0
            ):   
               neighbours_coordinates.append((self.pos_x + shift[0], self.pos_y + shift[1]))
        return neighbours_coordinates
    
    def __str__(self) -> str:
        return f"Entity: ({self.pos_x}, {self.pos_y})"
    
    def __repr__(self) -> str:
        return f"Entity({self.pos_x}, {self.pos_y}, {self.board_size_x}, {self.board_size_y})"
    

class StaticMapObject(Entity):
    def __init__(self, x, y, board_size_x, board_size_y) -> None:
        super().__init__(x, y, board_size_x, board_size_y)
        self.creatures_on_this_terrain = []
    
    def get_creatures_on_this_terrain(self):
        return self.creatures_on_this_terrain
    
    def add_creature_on_this_terrain(self, creature):
        self.creatures_on_this_terrain.append(creature)


class Grass(Entity):
    def __init__(self, x, y, board_size_x, board_size_y) -> None:
        super().__init__(x, y, board_size_x, board_size_y)
        self.creatures_on_grass = []
    
    def on_it(self):
        return self.creatures_on_grass
    
    def add_creature_on

class Creature(Entity):
    pass
    

class BFS:
    def __init__(self, graph) -> None:
        self.graph = graph
        self.visited = set()
        self.queue = []

    def search(self, start_cord):
        self.queue.append(start_cord)

        while self.queue:
            cur = self.queue.pop(0)
            print(cur)
            self.visited.add(cur)

            for new_cords in self.graph[cur].get_neighbours_coordinates():
                if new_cords not in self.visited and new_cords not in self.queue:
                    self.queue.append(new_cords)
        
    
    


if __name__ == '__main__':


    d = {}
    for i in range(3):
        for j in range(4):
            d[(i, j)] = Entity(i, j, 3, 4)
    for i in range(3):
        for j in range(4):
            print(d[(i, j)], end=' ')
        print()
    # print(d[(1, 1)].get_neighbours_coordinates())
    bfs = BFS(d)
    bfs.search((0, 0))