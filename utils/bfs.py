# class Bfs:
#     def __init__(self, animal_graph, terrain_graph) -> None:
#         self.animal_graph = animal_graph
#         self.terrain_graph = terrain_graph
#         self.visited = set()
#         self.queue = []

#     def is_passable(self, obj):
        
#         if isinstance(obj, (Rock, )):
#             return False
#         return True

#     def search(self, calling_obj.crd, target, calling_obj.bd_size):
#         self.queue.append(calling_obj.crd)

#         parents = {calling_obj.crd: calling_obj.crd}
#         start_path = None

#         while self.queue:
#             cur = self.queue.pop(0)
#             self.visited.add(cur)

#             if isinstance(target, Grass): # вызвал herbivore
#                 cur_obj = self.terrain_graph.get(cur, Entity(Coordinates(*cur.values), calling_obj.bd_size))
#             else: # вызвал predator
#                 cur_obj = self.animal_graph.get(cur, Entity(Coordinates(*cur.values), calling_obj.bd_size))
            
#             if isinstance(cur_obj, target):
#                 start_path = cur
#                 break
    
#             for new_crd in cur_obj.coordinates.neighbor_coordinates(calling_obj.bd_size):
#                 obj = self.terrain_graph.get(cur, Entity(Coordinates(*cur.values), calling_obj.bd_size))
#                 if new_crd not in self.visited and new_crd not in self.queue and self.is_passable(obj):
#                     self.queue.append(new_crd)
#                     parents[new_crd] = cur
#         else:
#             return None
        
#         path = []
#         while parents[start_path] != start_path:
#             path.append(start_path)
#             start_path = parents[start_path]
#         if not path and start_path is not None:
#             path.append(start_path)
#         return path


class Bfs:
    @staticmethod
    def __is_coordinate_bfs_valid(crd, queue, visited, start_crd):
        return (crd not in queue and 
                crd not in visited and
                crd != start_crd) 


    @staticmethod
    def search(calling_obj, target_class, graph):
        queue = [calling_obj.crd]
        visited = set()
        crd_connections = {calling_obj.crd: calling_obj.crd} # условие выхода при воссоздании пути от старта до цели
        
        target_crd = None

        while queue:
            cur_crd = queue.pop(0)
            visited.add(cur_crd)

            cur_obj = graph.get(cur_crd, cur_crd)
            if isinstance(cur_obj, target_class):
                target_crd = cur_crd
                break

            for next_crd in cur_crd.neighbor_coordinates(calling_obj.bd_size):
                if Bfs.__is_coordinate_bfs_valid(next_crd, queue, visited, calling_obj.crd) and calling_obj.is_coordinate_free_to_move(next_crd):
                    queue.append(next_crd)
                    crd_connections[next_crd] = cur_crd
            
        else:
            # проверены все пути, но цель не найдена
            return []
        
        path_to_target = []
        while crd_connections[target_crd] != target_crd:
            path_to_target.append(target_crd)
            target_crd = crd_connections[target_crd]
        
        # цель изначально была на той же клетке (травоядное уже стоит на траве)
        if not path_to_target and target_crd is not None:
            path_to_target.append(target_crd)
        
        return path_to_target[::-1]


