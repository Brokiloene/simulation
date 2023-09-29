import os

from entities import Animal, Terrain

# print = functools.partial(print, flush=True)

class SimulationConsoleRenderer:
    ANSI_RESET     = "\033[0m"
    ANSI_BG        = "\033[01;48;05;185m"
    ANSI_BLINK     = "\033[5m"

    ANSI_GRASS     = "\033[01;38;05;70m"
    ANSI_GREY      = "\033[01;38;05;138m"
    ANSI_BROWN     = "\033[01;38;05;94m"

    ANSI_RED       = "\033[38;05;196m"
    ANSI_WHITE     = "\033[37m"

    def __init__(self, board_map) -> None:
        self.map = board_map
        self.clear = lambda: os.system('clear')

    def render(self, turns_cnt):
        self.clear()
        

        all_crd = self.map.all_possible_coordinates
        col_cnt = 0
        row_cnt = 0

        print(f"TURN {turns_cnt}")
        print(' ',  *[' ' + str(x) + ' ' for x in range(self.map.bd_size_col)], sep='')
        
        print(row_cnt, end='')
        for crd in all_crd:
            if self.map.is_animal_exists_at(crd):
                obj = self.map.get_object(Animal, crd) 

            elif self.map.is_terrain_exists_at(crd):
                obj = self.map.get_object(Terrain, crd) 
            else:
                obj = None

            match obj.__class__.__name__:
                case 'Herbivore':
                    print(self.ANSI_WHITE + obj.sprite, end='')
                case 'Predator':
                    print(self.ANSI_RED   + obj.sprite, end='')
                case 'Grass':
                    print(self.ANSI_GRASS + obj.sprite, end='')
                case 'Rock':
                    print(self.ANSI_GREY  + obj.sprite, end='')
                case 'Tree':
                    print(self.ANSI_BROWN + obj.sprite, end='')
                case _:
                    print('   ', end='')
                
            print(self.ANSI_RESET, end='')
            
            col_cnt += 1
            if col_cnt == self.map.bd_size_col:
                col_cnt = 0
                row_cnt += 1
                print()

                if row_cnt < self.map.bd_size_row:
                    print(row_cnt, end='')
