import unittest
import Algorithmique_exo1D

class Test_Exercice(unittest.TestCase):

    def test_ind_min(self):
        self.list= [2,1,5,3,4]
        self.assertEqual(Algorithmique_exo1D.index_minimum(self.list, 0, 4), 1)

    def test_tri_a_bulle(self):
        self.list= [2,1,5,3,4]
        self.assertEqual(Algorithmique_exo1D.tri_a_bulle(self.list), [1,2,3,4,5])

    def test_recherche(self):
        self.list= [2,1,5,3,4]
        self.assertEqual(Algorithmique_exo1D.recherche(self.list, 4), 4)

    def test_dichotomie(self):
        self.list= [2,1,5,3,4]
        self.assertEqual(Algorithmique_exo1D.dichotomie(self.list, 4), 4)

    def test_insertion(self):
        self.list = [2, 1, 5, 3, 4]
        self.assertEqual(Algorithmique_exo1D.insertion(3, self.list, 5), [2,1,3,5,3,4])

    def test_tri_extraction(self):
        self.list = [2, 1, 5, 3, 4]
        self.assertEqual(Algorithmique_exo1D.tri_extraction(self.list), [1,2,3,4,5])

    def test_tri_insertion(self):
        self.list = [2, 1, 5, 3, 4,6,7,9,8]
        self.assertEqual(Algorithmique_exo1D.tri_insertion(self.list), [1,2,3,4,5,6,7,8,9])
