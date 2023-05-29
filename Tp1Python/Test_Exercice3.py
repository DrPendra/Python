import unittest
import Algorithmique_exo1C

class Test_Exercice(unittest.TestCase):

    def test_promotion(self):
        self.promo = Algorithmique_exo1C.promotion(['billy', 'bob'], 2)
        assert type(self.promo) == type([])

    def test_moyenne_etudiant(self):
        self.promo = Algorithmique_exo1C.promotion(['billy', 'bob'], 2)
        for i in range(1, len(self.promo)):
            for j in range(1, len(self.promo[0])):
                self.promo[i][j] = 10
        self.assertEqual(Algorithmique_exo1C.moyenneetudiant(self.promo, 'billy'), 10)

    def test_moyenne_discipline(self):
        self.promo = Algorithmique_exo1C.promotion(['billy', 'bob'], 2)
        for i in range(1, len(self.promo)):
            for j in range(1, len(self.promo[0])):
                self.promo[i][j] = 10
        self.assertEqual(Algorithmique_exo1C.moyennedispline(self.promo, 'discipline1'), 10)

    def test_max(self):
        self.promo = Algorithmique_exo1C.promotion(['billy', 'bob'], 2)
        for i in range(1, len(self.promo)):
            for j in range(1, len(self.promo[0])):
                self.promo[i][j] = 10
        self.assertEqual(Algorithmique_exo1C.maxetudiant(self.promo), ('billy',10))

    def test_min(self):
        self.promo = Algorithmique_exo1C.promotion(['billy', 'bob'], 2)
        for i in range(1, len(self.promo)):
            for j in range(1, len(self.promo[0])):
                self.promo[i][j] = 10
        self.assertEqual(Algorithmique_exo1C.minetudiant(self.promo), ('billy',10))


