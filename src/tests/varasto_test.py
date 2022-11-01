import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def test_konstruktori_luo_tyhjan_varaston(self):
        self.varasto = Varasto(10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.varasto = Varasto(10)
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto = Varasto(10)
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto = Varasto(10)
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto = Varasto(10)
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto = Varasto(10)
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_uudella_varastolla_oikea_tilavuus_negatiivinen(self):
        self.varasto = Varasto(-10)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_lisays_lisaa_saldoa_negatiivinen(self):
        self.varasto = Varasto(10)
        self.varasto.lisaa_varastoon(-8)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa_negatiivinen(self):
        self.varasto = Varasto(10)
        self.varasto.lisaa_varastoon(-8)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_negatiivinen_alku_saldo_on_nolla(self):
        self.varasto = Varasto(0, -10)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_saldo_on_tilavuus(self):
        self.varasto = Varasto(10)
        self.varasto.lisaa_varastoon(15)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_negatiivisen_ottaminen_palauttaa_nollan(self):
        self.varasto = Varasto(10)
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(-2)

        self.assertAlmostEqual(saatu_maara, 0)

    def test_liikaa_ottaminen_palauttaa_olemassa_olevat(self):
        self.varasto = Varasto(10)
        self.varasto.lisaa_varastoon(5)

        saatu_maara = self.varasto.ota_varastosta(8)

        self.assertAlmostEqual(saatu_maara, 5)

    def test_oikea_str_palautus(self):
        self.assertEqual(str(Varasto(10, 7)), "saldo = 7, vielä tilaa 3")
