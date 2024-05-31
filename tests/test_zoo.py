import unittest
from unittest import TestCase
from src.zoo import Zoo, ZooKeepers, Animal, Fence

class TestZoo(TestCase):

    def setUp(self):
        
        self.zoo_1: Zoo = Zoo()
        self.zookeeper_1: ZooKeepers = ZooKeepers(name="Gianni", surname="Rossi", id=1)
        self.fence_1: Fence = Fence(area=100, temperature=25.0, habitat="savana")
        self.animal_1: Animal = Animal(name="Pluto", species="Canide", age=5, height=300.0, width=1.0, preferred_habitat="savana")

    def test_1(self):
        '''
        Questo test controlla che animali troppo grandi non vengano aggiunti alla Fence
        '''

        self.zookeeper_1.add_animal(self.animal_1, self.fence_1)
        result: int = len(self.fence_1.list_of_animal)
        message: str = f"Error: the function add_animal should not add self.animal_1 into self.fence_1"
        self.assertEqual(result, 0, message)

    def test_2(self):
        '''
        Questo test controlla che animali con area minore della fence vengano aggiunti alla Fence
        '''

        animal_2: Animal = Animal(name="Pluto", species="Canide", age=5, height=30.0, width=1.0, preferred_habitat="savana")
        self.zookeeper_1.add_animal(animal_2, self.fence_1)
        result: int = len(self.fence_1.list_of_animal)
        message: str = f"Error: the function add_animal should not add self.animal_1 into self.fence_1"
        self.assertEqual(result, 1, message)


    def test_3(self):
        pass

if __name__ == "__main__":

    unittest.main()