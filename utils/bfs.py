class Bfs:
    @staticmethod
    def _is_coordinate_bfs_valid(crd, queue, visited, start_crd):
        return (crd not in queue and 
                crd not in visited and
                crd != start_crd) 


    @staticmethod
    def search(calling_obj, target_type, target_class, board_map):
        queue = [calling_obj.crd]
        visited = set()
        crd_connections = {calling_obj.crd: calling_obj.crd} # условие выхода при воссоздании пути от старта до цели
        
        target_crd = None

        while queue:
            cur_crd = queue.pop(0)
            visited.add(cur_crd)

            try:
                cur_obj = board_map.get_object(target_type, cur_crd)
            except KeyError:
                cur_obj = object()
            
            if isinstance(cur_obj, target_class):
                target_crd = cur_crd
                break
            
            for next_crd in board_map.get_neighbor_coordinates_of(cur_crd):
                if Bfs._is_coordinate_bfs_valid(next_crd, queue, visited, calling_obj.crd) and calling_obj.is_coordinate_free_to_move(next_crd):
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
