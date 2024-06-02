import unittest

from utils.PorteSpy import PorteSpy
from utils.LecteurFake import LecteurFake
from MoteurOuverture import MoteurOuverture
from utils.badge import Badge
from utils.access_rules import RegleAccesParDefaut, RegleAccesTemps
from datetime import datetime, time


class ControlAccess(unittest.TestCase):
    def test_nominal(self):
        # ETANT DONNE une Porte reliée à un Lecteur, ayant détecté un Badge
        porte: PorteSpy = PorteSpy()
        lecteur: LecteurFake = LecteurFake()
        badge = Badge()

        lecteur.simuler_detection_badge(badge)

        moteurOuverture = MoteurOuverture()
        moteurOuverture.associer(lecteur, porte)
        moteurOuverture.ajouter_regle(badge.numero, RegleAccesParDefaut())

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
        moteurOuverture.ajouter_regle(badge.numero, RegleAccesParDefaut())

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
        moteurOuverture.ajouter_regle(badge.numero, RegleAccesParDefaut())

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
        moteurOuverture.ajouter_regle(badge.numero, RegleAccesParDefaut())

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
        moteurOuverture.ajouter_regle(badge.numero, RegleAccesParDefaut())

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
        moteurOuverture.ajouter_regle(badge.numero, RegleAccesParDefaut())

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
        moteurOuverture.ajouter_regle(badge.numero, RegleAccesParDefaut())

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteurOuverture.interroger()

        # ALORS aucun signal d'ouverture n'est envoyé à la Porte
        self.assertEqual(0, porte.nombre_ouverture_demandees)

    def test_badge_passe_partout(self):
        # ETANT DONNE une Porte reliée à un Lecteur, ayant détecté un Badge passe-partout
        porte = PorteSpy()
        lecteur = LecteurFake()
        master_badge = Badge(pass_all=True)

        lecteur.simuler_detection_badge(master_badge)

        moteurOuverture = MoteurOuverture()
        moteurOuverture.associer(lecteur, porte)

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteurOuverture.interroger()

        # ALORS le signal d'ouverture est envoyé à la porte
        self.assertTrue(porte.nombre_ouverture_demandees > 0)

    def test_badge_normal_sans_regles_acces(self):
        # ETANT DONNE une Porte reliée à un Lecteur, ayant détecté un Badge normal sans régles d'accès
        porte = PorteSpy()
        lecteur = LecteurFake()
        non_master_badge = Badge()

        lecteur.simuler_detection_badge(non_master_badge)

        moteurOuverture = MoteurOuverture()
        moteurOuverture.associer(lecteur, porte)

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteurOuverture.interroger()

        # ALORS le signal d'ouverture n'est pas envoyé à la porte
        self.assertFalse(porte.nombre_ouverture_demandees > 0)

    def test_badge_passe_partout_bloque(self):
        # ETANT DONNE une Porte reliée à un Lecteur, ayant détecté un Badge passe-partout bloqué
        porte = PorteSpy()
        lecteur = LecteurFake()
        master_badge = Badge(pass_all=True)

        lecteur.simuler_detection_badge(master_badge)

        moteurOuverture = MoteurOuverture()
        moteurOuverture.associer(lecteur, porte)
        moteurOuverture.bloquer_badge(master_badge)

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteurOuverture.interroger()

        # ALORS le signal d'ouverture n'est pas envoyé à la porte
        self.assertFalse(porte.nombre_ouverture_demandees > 0)

    def test_badge_passe_partout_ouvre_plusieurs(self):
        # ETANT DONNE deux Portes reliées à un Lecteur, ayant détecté un Badge passe-partout
        # ET deux Portes reliées chacune à un Lecteur
        porte1 = PorteSpy()
        porte2 = PorteSpy()
        lecteur = LecteurFake()
        master_badge = Badge(pass_all=True)

        lecteur.simuler_detection_badge(master_badge)

        moteurOuverture = MoteurOuverture()
        moteurOuverture.associer(lecteur, porte1)
        moteurOuverture.associer(lecteur, porte2)

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteurOuverture.interroger()

        # ALORS le signal d'ouverture est envoyé aux deux portes
        self.assertTrue(porte1.nombre_ouverture_demandees > 0)
        self.assertTrue(porte2.nombre_ouverture_demandees > 0)

    def test_badge_avec_restriction_temps(self):
        # ETANT DONNE une Porte reliée à un Lecteur, ayant détecté un Badge avec une restriction de temps
        # ET une règle de temps vérifiée
        porte = PorteSpy()
        lecteur = LecteurFake()
        badge = Badge()
        current_time = time(12, 00)

        lecteur.simuler_detection_badge(badge)

        moteurOuverture = MoteurOuverture()
        moteurOuverture.associer(lecteur, porte)
        moteurOuverture.ajouter_regle(badge.numero, RegleAccesTemps(time(9, 00), time(17, 00), current_time))

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteurOuverture.interroger()

        # ALORS le signal d'ouverture est envoyé à la porte
        self.assertTrue(porte.nombre_ouverture_demandees > 0)

    def test_acces_refuse_badge_restrictions_temps(self):
        # ETANT DONNE une Porte reliée à un Lecteur, ayant détecté un Badge avec une restriction de temps
        # ET une règle de temps non vérifiée
        porte = PorteSpy()
        lecteur = LecteurFake()
        badge = Badge()
        current_time = time(8, 0)

        lecteur.simuler_detection_badge(badge)

        moteurOuverture = MoteurOuverture()
        moteurOuverture.associer(lecteur, porte)
        moteurOuverture.ajouter_regle(badge.numero, RegleAccesTemps(time(9, 0), time(17, 0), current_time))

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteurOuverture.interroger()

        # ALORS le signal d'ouverture n'est pas envoyé à la porte
        self.assertFalse(porte.nombre_ouverture_demandees > 0)

    def test_access_au_debut_de_restriction_temps(self):
        # ETANT DONNE une Porte reliée à un Lecteur, ayant détecté un Badge avec une restriction de temps
        # ET une règle de temps défini au début de l'intervalle de restriction
        porte = PorteSpy()
        lecteur = LecteurFake()
        badge = Badge()
        current_time = time(9,0)

        lecteur.simuler_detection_badge(badge)

        moteurOuverture = MoteurOuverture()
        moteurOuverture.associer(lecteur, porte)
        moteurOuverture.ajouter_regle(badge.numero, RegleAccesTemps(time(9, 0), time(17, 0), current_time))

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteurOuverture.interroger()

        # ALORS le signal d'ouverture est envoyé à la porte
        self.assertTrue(porte.nombre_ouverture_demandees > 0)

    def test_access_a_la_fin_de_restriction_temps(self):
        # ETANT DONNE une Porte reliée à un Lecteur, ayant détecté un Badge avec une restriction de temps
        # ET une règle de temps défini à la fin de l'intervalle de restriction
        porte = PorteSpy()
        lecteur = LecteurFake()
        badge = Badge()
        current_time = time(17, 0)

        lecteur.simuler_detection_badge(badge)

        moteurOuverture = MoteurOuverture()
        moteurOuverture.associer(lecteur, porte)
        moteurOuverture.ajouter_regle(badge.numero, RegleAccesTemps(time(9, 0), time(17, 0), current_time))

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteurOuverture.interroger()

        # ALORS le signal d'ouverture est envoyé à la porte
        self.assertTrue(porte.nombre_ouverture_demandees > 0)

    def test_plusieurs_regles_de_restrctions_temps(self):
        # ETANT DONNE une Porte reliée à un Lecteur, ayant détecté un Badge avec une restriction de temps
        # ET une règle de temps de restriction de temps non respectée
        # ET une règle de temps de restriction de temps respectée
        porte = PorteSpy()
        lecteur = LecteurFake()
        badge = Badge()
        current_time = time(12, 0)

        lecteur.simuler_detection_badge(badge)

        moteurOuverture = MoteurOuverture()
        moteurOuverture.associer(lecteur, porte)
        moteurOuverture.ajouter_regle(badge.numero, RegleAccesTemps(time(9,0), time(11,0), current_time))
        moteurOuverture.ajouter_regle(badge.numero, RegleAccesTemps(time(12, 0), time(14,0), current_time))

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteurOuverture.interroger()

        # ALORS le signal d'ouverture est envoyé à la porte
        self.assertTrue(porte.nombre_ouverture_demandees > 0)

    def test_badge_passe_partout_ignore_restriction_temps(self):
        # ETANT DONNE une Porte reliée à un Lecteur, ayant détecté un Badge passe-partout
        # ET une règle d'accès en dehors des heures autorisées
        porte = PorteSpy()
        lecteur = LecteurFake()
        badge = Badge(pass_all=True)

        lecteur.simuler_detection_badge(badge)

        current_time = time(8, 0)
        moteurOuverture = MoteurOuverture()
        moteurOuverture.associer(lecteur, porte)
        moteurOuverture.ajouter_regle(badge.numero, RegleAccesTemps(time(9, 0), time(17, 0), current_time))

        # QUAND le Moteur d'Ouverture effectue une interrogation des lecteurs
        moteurOuverture.interroger()

        # ALORS le signal d'ouverture est envoyé à la porte
        self.assertTrue(porte.nombre_ouverture_demandees > 0)