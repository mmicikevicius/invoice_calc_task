import unittest
from invoice_calc import InvoiceCalculation

class TestCalc(unittest.TestCase):
    def setUp(self):
        self.invoice_1 = InvoiceCalculation(50, False, 'Austria', True, 'Spain')
        self.invoice_2 = InvoiceCalculation(122.5, True, 'Latvia', True, 'Chile')
        self.invoice_3 = InvoiceCalculation(0.5, True, 'Lithuania', False, 'Sweden')
        self.invoice_4 = InvoiceCalculation(100, True, 'Slovenia', True, 'Slovenia')
        self.invoice_5 = InvoiceCalculation(1020, False, 'Austria', False, 'Spain')
        self.invoice_6 = InvoiceCalculation(150, True, 'Australia', True, 'Slovenia')
        self.invoice_7 = InvoiceCalculation(150, True, 'Australia', True, 'Australia')
    
    def test_vat(self):
        self.assertEqual(self.invoice_1.vat(), 10.5)
        
    def test_invoice_amount(self):
        self.assertEqual(self.invoice_1.invoice_amount(10.5), 60.5)
        self.assertEqual(self.invoice_3.invoice_amount(), 0.5)
        
    def test_invoice_parameters(self):
        self.assertEqual(self.invoice_1.invoice_parameters(), 50)
        self.assertEqual(self.invoice_2.invoice_parameters(), 122.5)
        self.assertEqual(self.invoice_3.invoice_parameters(), 0.625)
        self.assertEqual(self.invoice_4.invoice_parameters(), 122)
        self.assertEqual(self.invoice_5.invoice_parameters(), 1020)
        self.assertEqual(self.invoice_6.invoice_parameters(), 183)
        self.assertEqual(self.invoice_7.invoice_parameters(), 180)
        

if __name__ == '__main__':
    unittest.main()