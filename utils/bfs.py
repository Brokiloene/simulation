class Bfs:
    @staticmethod
    def is_coordinate_bfs_valid(crd, queue, visited, start_crd):
        return (crd not in queue and 
                crd not in visited and
                crd != start_crd) 


    @staticmethod
    def get_neigbors(coordinate, board_map):
        return board_map.get_neighbor_coordinates_of(coordinate)
    

    @staticmethod
    def restore_path(start_crd, target_crd, connections):
        path = []
        while connections[target_crd] != start_crd:
            path.append(target_crd)
            
            target_crd = connections[target_crd]

        path.append(target_crd)
        
        return path[::-1]


    @staticmethod
    def search(start_crd, target_crd, board_map):
        queue = [start_crd]
        visited = set()
        connections = {start_crd: start_crd} # условие выхода при воссоздании пути от старта до цели

        while queue:
            cur_crd = queue.pop(0)
            visited.add(cur_crd)
            
            if cur_crd == target_crd:
                break
            
            for next_crd in Bfs.get_neigbors(cur_crd, board_map):
                if Bfs.is_coordinate_bfs_valid(next_crd, queue, visited, start_crd):
                    queue.append(next_crd)
                    connections[next_crd] = cur_crd
        else:
            # проверены все пути, но цель не найдена
            return []
        
        return Bfs.restore_path(start_crd, target_crd, connections)
