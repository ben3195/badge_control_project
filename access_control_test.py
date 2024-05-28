import unittest

from utils.PorteSpy import PorteSpy
from utils.LecteurFake import LecteurFake
from MoteurOuverture import MoteurOuverture


class ControlAccess(unittest.TestCase):
    def test_nominal(self):
        # ETANT DONNE une Porte reliée à un Lecteur, ayant détecté un Badge
        moteur_ouverture = MoteurOuverture()
        porte = PorteSpy()
        lecteur = LecteurFake()

        lecteur.simuler_detection_badge()

        moteur_ouverture.associer(lecteur, porte)

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteur_ouverture.interroger()

        # ALORS le signal d'ouverture est envoyé à la porte
        self.assertTrue(porte.ouverture_demandee)

    def test_aucune_interogation(self):
        # ETANT DONNE une Porte reliée à un Lecteur, ayant détecté un Badge
        porte = PorteSpy()
        lecteur = LecteurFake()

        lecteur.simuler_detection_badge()

        moteur_ouverture = MoteurOuverture()
        moteur_ouverture.associer(lecteur, porte)

        # ALORS le signal d'ouverture n'est pas envoyé à la porte
        self.assertFalse(porte.ouverture_demandee)

    def test_non_badge(self):
        # ETANT DONNE une Porte reliée à un Lecteur, n'ayant pas détecté un Badge
        porte = PorteSpy()
        lecteur = LecteurFake()

        moteur_ouverture = MoteurOuverture()
        moteur_ouverture.associer(lecteur, porte)

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteur_ouverture.interroger()

        # ALORS le signal d'ouverture n'est pas envoyé à la porte
        self.assertFalse(porte.ouverture_demandee)

    def test_cas_2_portes(self):
        # ETANT DONNE deux Portes reliées à un Lecteur, ayant détecté un Badge
        porte1 = PorteSpy()
        porte2 = PorteSpy()
        lecteur = LecteurFake()

        lecteur.simuler_detection_badge()

        moteur_ouverture = MoteurOuverture()
        moteur_ouverture.associer(lecteur, porte1)
        moteur_ouverture.associer(lecteur, porte2)

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteur_ouverture.interroger()

        # ALORS le signal d'ouverture est envoyé aux deux portes
        self.assertTrue(porte1.ouverture_demandee)
        self.assertTrue(porte2.ouverture_demandee)

    def test_deux_portes(self):
        # ETANT DONNE un Lecteur ayant détecté un Badge
        lecteurAyantDetecte = LecteurFake()
        lecteurAyantDetecte.simuler_detection_badge()

        # ET un autre Lecteur n'ayant rien détecté
        lecteurNAyantPasDetecte = LecteurFake()

        # ET une Porte reliée chacune à un Lecteur
        porteDevantSOuvrir = PorteSpy()
        porteDevantResterFermee = PorteSpy()

        # Associer chaque lecteur à sa porte respective
        moteur_ouverture = MoteurOuverture()
        moteur_ouverture.associer(lecteurAyantDetecte, porteDevantSOuvrir)
        moteur_ouverture.associer(lecteurNAyantPasDetecte, porteDevantResterFermee)

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteur_ouverture.interroger()

        # ALORS seule la Porte reliée au Lecteur ayant détecté un badge reçoit le signal d'ouverture
        self.assertFalse(porteDevantResterFermee.ouverture_demandee)
        self.assertTrue(porteDevantSOuvrir.ouverture_demandee)

    def test_deux_portes_inverse(self):
        # ETANT DONNE un Lecteur ayant détecté un Badge
        # ET un autre Lecteur n'ayant rien détecté
        # ET une Porte reliée chacune à un Lecteur
        porteDevantSOuvrir = PorteSpy()
        porteDevantResterFermee = PorteSpy()

        lecteurAyantDetecte = LecteurFake()
        lecteurAyantDetecte.simuler_detection_badge()

        lecteurNAyantPasDetecte = LecteurFake()

        moteur_ouverture = MoteurOuverture()
        moteur_ouverture.associer(lecteurNAyantPasDetecte, porteDevantResterFermee)
        moteur_ouverture.associer(lecteurAyantDetecte, porteDevantSOuvrir)

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteur_ouverture.interroger()

        # ALORS seule la Porte reliée au Lecteur reçoit le signal d'ouverture
        self.assertFalse(porteDevantResterFermee.ouverture_demandee)
        self.assertTrue(porteDevantSOuvrir.ouverture_demandee)

    def test_2_lecteurs(self):
        # ETANT DONNE une Porte reliée à deux Lecteurs, ayant tous les deux détecté un Badge
        porte = PorteSpy()

        lecteur1 = LecteurFake()
        lecteur1.simuler_detection_badge()

        lecteur2 = LecteurFake()
        lecteur2.simuler_detection_badge()

        moteur_ouverture = MoteurOuverture()
        moteur_ouverture.associer(lecteur1, porte)
        moteur_ouverture.associer(lecteur2, porte)

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteur_ouverture.interroger()

        # ALORS un seul signal d'ouverture est envoyé à la Porte
        self.assertEqual(1, porte.nombre_ouverture_demandees)

    # def test_badge_bloque(self):
    #     # ETANT DONNE une Porte reliée à un lecteur, ayant détécté un badge bloqué
    #     porte = PorteSpy()
    #     lecteur = LecteurFake()

    #     moteur_ouverture = MoteurOuverture()
    #     moteur_ouverture.bloquer_badge()
    #     moteur_ouverture.associer(lecteur, porte)

    #     lecteur.simuler_detection_badge()

    #     # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
    #     moteur_ouverture.interroger()

    #     # ALORS aucun signal d'ouverture n'est envoyé à la Porte
    #     self.assertFalse(porte.ouverture_demandee)
    #     self.assertEqual(0, porte.nombre_ouverture_demandees)

if __name__ == '__main__':
    unittest.main()
