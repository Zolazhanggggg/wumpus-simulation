from world import World
from agent import Agent

def main():
    world = World(size=5)
    agent = Agent(world)
    world.display()
    print("Simulation placeholder")

    if __name__ == "__main__":
        main()
