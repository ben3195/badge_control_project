import unittest

from utils.PorteSpy import PorteSpy
from utils.LecteurFake import LecteurFake
from MoteurOuverture import MoteurOuverture
from utils.badge import Badge


class ControlAccess(unittest.TestCase):
    def test_nominal(self):
        # ETANT DONNE une Porte reliée à un Lecteur, ayant détecté un Badge
        porte: PorteSpy = PorteSpy()
        lecteur: LecteurFake = LecteurFake()
        badge = Badge()

        lecteur.simuler_detection_badge(badge)

        moteurOuverture = MoteurOuverture()
        moteurOuverture.associer(lecteur, porte)

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteurOuverture.interroger()

        # ALORS le signal d'ouverture est envoyé à la porte
        self.assertTrue(porte.nombre_ouverture_demandees > 0)

    def test_aucune_interogation(self):
        # ETANT DONNE une Porte reliée à un Lecteur, ayant détecté un Badge
        porte = PorteSpy()
        lecteur = LecteurFake()
        badge = Badge()

        lecteur.simuler_detection_badge(badge)

        moteurOuverture = MoteurOuverture()
        moteurOuverture.associer(lecteur, porte)

        # ALORS le signal d'ouverture n'est pas envoyé à la porte
        self.assertFalse(porte.nombre_ouverture_demandees > 0)

    def test_non_badge(self):
        # ETANT DONNE une Porte reliée à un Lecteur, n'ayant pas détecté un Badge
        porte = PorteSpy()
        lecteur = LecteurFake()

        moteurOuverture = MoteurOuverture()
        moteurOuverture.associer(lecteur, porte)

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteurOuverture.interroger()

        # ALORS le signal d'ouverture n'est pas envoyé à la porte
        self.assertFalse(porte.nombre_ouverture_demandees > 0)

    def test_cas_2_portes(self):
        # ETANT DONNE deux Portes reliée à un Lecteur, ayant détecté un Badge
        porte1 = PorteSpy()
        porte2 = PorteSpy()
        lecteur = LecteurFake()
        badge = Badge()

        lecteur.simuler_detection_badge(badge)

        moteurOuverture = MoteurOuverture()
        moteurOuverture.associer(lecteur, porte1)
        moteurOuverture.associer(lecteur, porte2)

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteurOuverture.interroger()

        # ALORS le signal d'ouverture est envoyé aux deux portes
        self.assertTrue(porte1.nombre_ouverture_demandees > 0)
        self.assertTrue(porte2.nombre_ouverture_demandees > 0)

    def test_deux_portes(self):
        # ETANT DONNE un Lecteur ayant détecté un Badge
        # ET un autre Lecteur n'ayant rien détecté
        # ET une Porte reliée chacune à un Lecteur
        porteDevantSOuvrir = PorteSpy()
        porteDevantResterFermee = PorteSpy()
        badge = Badge()

        lecteurAyantDetecte = LecteurFake()
        lecteurAyantDetecte.simuler_detection_badge(badge)

        lecteurNAyantPasDetecte = LecteurFake()

        moteurOuverture = MoteurOuverture()
        moteurOuverture.associer(lecteurAyantDetecte, porteDevantSOuvrir)
        moteurOuverture.associer(lecteurNAyantPasDetecte, porteDevantResterFermee)

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteurOuverture.interroger()

        # ALORS seule la Porte reliée au Lecteur reçoit le signal d'ouverture
        self.assertFalse(porteDevantResterFermee.nombre_ouverture_demandees > 0)
        self.assertTrue(porteDevantSOuvrir.nombre_ouverture_demandees > 0)
    def test_deux_portes_inverse(self):
        # ETANT DONNE un Lecteur ayant détecté un Badge
        # ET un autre Lecteur n'ayant rien détecté
        # ET une Porte reliée chacune à un Lecteur
        porteDevantSOuvrir = PorteSpy()
        porteDevantResterFermee = PorteSpy()
        badge = Badge()

        lecteurAyantDetecte = LecteurFake()
        lecteurAyantDetecte.simuler_detection_badge(badge)

        lecteurNAyantPasDetecte = LecteurFake()

        moteurOuverture = MoteurOuverture()
        moteurOuverture.associer(lecteurNAyantPasDetecte, porteDevantResterFermee)
        moteurOuverture.associer(lecteurAyantDetecte, porteDevantSOuvrir)

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteurOuverture.interroger()

        # ALORS seule la Porte reliée au Lecteur reçoit le signal d'ouverture
        self.assertFalse(porteDevantResterFermee.nombre_ouverture_demandees > 0)
        self.assertTrue(porteDevantSOuvrir.nombre_ouverture_demandees > 0)

    def test_2_lecteurs(self):
        # ETANT DONNE une Porte reliée à deux Lecteurs, ayant tous les deux détecté un Badge
        porte = PorteSpy()
        badge = Badge()

        lecteur1 = LecteurFake()
        lecteur1.simuler_detection_badge(badge)

        lecteur2 = LecteurFake()
        lecteur2.simuler_detection_badge(badge)

        moteurOuverture = MoteurOuverture()
        moteurOuverture.associer(lecteur1, porte)
        moteurOuverture.associer(lecteur2, porte)

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteurOuverture.interroger()

        # ALORS un seul signal d'ouverture est envoyé à la Porte
        self.assertEqual(1, porte.nombre_ouverture_demandees)

    def test_badge_bloque(self):
        # ETANT DONNE une Porte reliée à un lecteur, ayant détécté un badge bloqué
        porte = PorteSpy()
        lecteur = LecteurFake()
        badge = Badge()

        moteurOuverture = MoteurOuverture()
        moteurOuverture.bloquer_badge(badge)
        moteurOuverture.associer(lecteur, porte)

        lecteur.simuler_detection_badge(badge)

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteurOuverture.interroger()

        # ALORS aucun signal d'ouverture n'est envoyé à la Porte
        self.assertEqual(0, porte.nombre_ouverture_demandees)
