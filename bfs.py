from coordinates import Coordinates
from terrain import Terrain

class BFS:
    def __init__(self, graph) -> None:
        self.graph = graph
        self.visited = set()
        self.queue = []

    def search(self, start_cord, target, board_size):
        self.queue.append(start_cord)

        parents = {start_cord: start_cord}
        start_path = None

        while self.queue:
            cur = self.queue.pop(0)
            self.visited.add(cur)

            cur_obj = self.graph.get(cur, Terrain(Coordinates(*cur.values), board_size))
            if cur_obj.name == target:
                start_path = cur
                break
    
            for new_cords in cur_obj.coordinates.neighbor_coordinates(board_size):
                if new_cords not in self.visited and new_cords not in self.queue:
                    self.queue.append(new_cords)
                    parents[new_cords] = cur
        else:
            return None
        
        path = []
        while parents[start_path] != start_path:
            path.append(start_path)
            start_path = parents[start_path]
        if not path and start_path is not None:
            path.append(start_path)
        return path
