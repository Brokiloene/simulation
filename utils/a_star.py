from utils.coordinate import Coordinate

class AStar:
    @staticmethod
    def get_neigbors(coordinate, board_map):
        return board_map.get_neighbor_coordinates_of(coordinate)
    

    @staticmethod
    def set_connections(start_crd, ends, connections):
        for end in ends:
            connections[end] = start_crd


    @staticmethod
    def set_costs(start_crd, ends, costs):
        def is_diagonal_move(crd1, crd2):
            return abs(crd1.row - crd1.col) == abs(crd2.row - crd2.col)
        

        for end in ends:
            costs[end] = costs[start_crd] + 14 if is_diagonal_move(start_crd, end) else costs[start_crd] + 10

    
    @staticmethod
    def set_heuristic_costs(ends, target_crd, heuristic_costs):
        def calc_manhattan_distance(coordinate, target_crd):
            return 10 * (abs(coordinate.col - target_crd.col) + abs(coordinate.row - target_crd.row))


        for end in ends:
            heuristic_costs[end] = calc_manhattan_distance(end, target_crd)


    def find_min_weight_coordinate(arr, costs, heuristic_costs):
        min_weight = None
        min_crd = None

        for crd in arr:
            if min_weight is None or min_weight > costs[crd] + heuristic_costs[crd]:
                min_weight = costs[crd] + heuristic_costs[crd]
                min_crd = crd
        
        return min_crd
    

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
        open_list = [start_crd]
        closed_list = []

        connections = {}
        costs = {start_crd: 0}
        heuristic_costs = {start_crd: 0}

        while open_list:
            cur_crd = AStar.find_min_weight_coordinate(open_list, costs, heuristic_costs)
            open_list.remove(cur_crd)
            closed_list.append(cur_crd)

            if cur_crd == target_crd:
                break

            neigbors = [crd for crd in AStar.get_neigbors(cur_crd, board_map) if crd not in closed_list]

            AStar.set_connections(cur_crd, neigbors, connections)
            AStar.set_costs(cur_crd, neigbors, costs)
            AStar.set_heuristic_costs(neigbors, target_crd, heuristic_costs)

            open_list.extend([crd for crd in neigbors if crd not in open_list])
        else:
            return []

        return AStar.restore_path(start_crd, target_crd, connections)
