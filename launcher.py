from simulation import Simulation


def main():
    sim = Simulation(11, 11, search_algorithm="A*")
    sim.start()


if __name__ == '__main__':
    main()
