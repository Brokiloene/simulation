from simulation import Simulation


def main():
    sim = Simulation(10, 10, search_algorithm="A*") # area >= 66
    sim.start()


if __name__ == '__main__':
    main()
