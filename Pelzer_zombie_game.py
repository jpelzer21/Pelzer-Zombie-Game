from enum import Enum

# Enum for agent states
# class State(Enum):
#     ALIVE = "ALIVE"
#     INFECTED = "INFECTED"
#     DEAD = "DEAD"

# Base class for all agents
class Agent:
    def __init__(self, energy):
        self.state = "ALIVE"
        self.energy = energy
        self.neighbors = []

    def change_energy(self, amount):
        self.energy += amount

        if self.energy < 0:
            self.energy = 0

        if self.energy == 0:
            self.state = "DEAD"


    def add_neighbor(self, agent):
        self.neighbors.append(agent)

    def remove_neighbor(self, agent):
        self.neighbors.remove(agent)

    def __repr__(self):
        return f"{self.__class__.__name__}(State: {self.state}, Energy: {self.energy})"






class Human(Agent):
    def __init__(self, energy):
        super().__init__(energy)
        self.state = "ALIVE"

    def infect(self):
        if self.state == "ALIVE":
            self.state = "INFECTED"

    def heal(self):
        if self.state == "INFECTED":
            self.state = "ALIVE"





class Doctor(Human):
    def heal_other(self, human):
        if isinstance(human, Human) and human.state == "INFECTED":
            human.heal()






class Zombie(Agent):
    def __init__(self, energy):
        super().__init__(energy)
        self.state = "ALIVE"

    def bite(self, human):
        if isinstance(human, Human) and human.state == "ALIVE":
            human.infect()







if __name__ == "__main__":

    human1 = Human(energy=100)
    human2 = Human(energy=90)
    doctor = Doctor(energy=80)
    zombie = Zombie(energy=70)

    human1.add_neighbor(doctor)
    doctor.add_neighbor(human1)
    zombie.add_neighbor(human2)

    print(human1)
    print(doctor)
    print(zombie)

    zombie.bite(human2)
    print(human2)

    doctor.heal_other(human2)
    print(human2)

    zombie.change_energy(-70)
    print(zombie)
