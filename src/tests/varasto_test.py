import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        
    def test_lisaa_varastoon_yli(self):
        self.varasto.lisaa_varastoon(12)  
        self.assertAlmostEqual(self.varasto.saldo, 10)  

    def test_ota_varastosta_yli(self):
        self.varasto.lisaa_varastoon(5)
        otettu = self.varasto.ota_varastosta(7) 
        self.assertAlmostEqual(otettu, 5)  
        self.assertAlmostEqual(self.varasto.saldo, 0)  

    def test_lisaa_negatiivinen(self):
        self.varasto.lisaa_varastoon(-5)  
        self.assertAlmostEqual(self.varasto.saldo, 0)  

    def test_ota_negatiivinen(self):
        self.varasto.ota_varastosta(-3)  
        self.assertAlmostEqual(self.varasto.saldo, 0) 
    
    def test_nolla_kapasiteetti(self):
        varasto_zero = Varasto(0)
        self.assertAlmostEqual(varasto_zero.tilavuus, 0)
        self.assertAlmostEqual(varasto_zero.saldo, 0)
    
    def test_poista_nolla(self):
        initial_saldo = self.varasto.saldo
        self.varasto.ota_varastosta(0)
        self.assertAlmostEqual(self.varasto.saldo, initial_saldo)

    def test_lisaa_tayteen(self):
        self.varasto.lisaa_varastoon(10)
        self.varasto.lisaa_varastoon(1) 
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ota_tyhjasta(self):
        self.varasto.ota_varastosta(1)
        self.assertAlmostEqual(self.varasto.saldo, 0)  
        
    def test_init_ali(self):
        varasto_negative_saldo = Varasto(10, -5)
        self.assertAlmostEqual(varasto_negative_saldo.saldo, 0)  

    def test_init_yli(self):
        varasto_exceeding_saldo = Varasto(10, 15)
        self.assertAlmostEqual(varasto_exceeding_saldo.saldo, 10) 

    def test_teksti(self):
        self.varasto.lisaa_varastoon(5)
        expected_str = "saldo = 5, vielä tilaa 5"
        self.assertEqual(str(self.varasto), expected_str)        
        
  
