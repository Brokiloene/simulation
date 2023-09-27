import os
import functools


print = functools.partial(print, flush=True)

class SimulationConsoleRenderer:
    ANSI_RESET     = "\033[0m"
    ANSI_BG        = "\033[01;48;05;185m"
    ANSI_BLINK     = "\033[5m"

    ANSI_GRASS     = "\033[01;38;05;70m"
    ANSI_GREY      = "\033[01;38;05;138m"
    ANSI_BROWN     = "\033[01;38;05;94m"

    ANSI_RED       = "\033[38;05;196m"
    ANSI_WHITE     = "\033[37m"

    def __init__(self, simulation) -> None:
        self.simulation = simulation
        self.clear = lambda: os.system('clear')

    def render(self, turns_cnt):
        self.clear()
        

        all_crd = self.simulation.all_possible_coordinates
        col_cnt = 0
        row_cnt = 0

        print(f"TURN {turns_cnt}")
        print(' ',  *[' ' + str(x) + ' ' for x in range(self.simulation.board_size_y)], sep='')
        
        print(row_cnt, end='')
        for crd in all_crd:
            if crd in self.simulation.animal_graph:
                # print(self.simulation.animal_graph[crd], end='')
                obj = self.simulation.animal_graph[crd] 

            elif crd in self.simulation.terrain_graph:
                # print(self.simulation.terrain_graph[crd], end='')
                obj = self.simulation.terrain_graph[crd]
            else:
                obj = None

            match obj.__class__.__name__:
                case 'Herbivore':
                    print(self.ANSI_WHITE + obj.sprite + self.ANSI_RESET, end='')
                case 'Predator':
                    print(self.ANSI_RED + obj.sprite + self.ANSI_RESET, end='')
                case 'Grass':
                    print(self.ANSI_GRASS + obj.sprite + self.ANSI_RESET, end='')
                case 'Rock':
                    print(self.ANSI_GREY + obj.sprite + self.ANSI_RESET, end='')
                case 'Tree':
                    print(self.ANSI_BROWN + obj.sprite + self.ANSI_RESET, end='')
                case _:
                    print('   ', end='')
            
            col_cnt += 1
            if col_cnt == self.simulation.board_size_y:
                col_cnt = 0
                row_cnt += 1
                print()

                if row_cnt < self.simulation.board_size_x:
                    print(row_cnt, end='')
