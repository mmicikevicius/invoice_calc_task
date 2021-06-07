class InvoiceCalculation:
    def __init__(self, amount, service_provider_vat_payer, service_provider_country, customer_vat_payer, customer_country):
        self.EU_VAT = {'Belgium':21, 'Bulgaria':20, 'Czech Republic':21, 'Denmark':25, 'Germany':19,
          'Estonia':20, 'Ireland':23, 'Greece':24, 'Spain':21, 'France':20, 'Croatia':25,
          'Italy':22, 'Cyprus':19, 'Latvia':21, 'Lithuania':21, 'Luxembourg':17, 'Hungary':27,
          'Malta':18, 'Netherlands':21, 'Austria':20, 'Poland':23, 'Portugal':23, 'Romania':19,
          'Slovenia':22, 'Slovakia':20, 'Finland':24, 'Sweden':25, 'United Kingdom':20}
        self.not_eu_vat = 0.20
        self.amount_without_vat = amount
        self.service_provider_vat_payer = service_provider_vat_payer
        self.service_provider_country = service_provider_country
        self.customer_vat_payer = customer_vat_payer
        self.customer_country = customer_country
               
    def vat(self):
        if self.customer_country in self.EU_VAT:
            percent = self.EU_VAT[self.customer_country] / 100
            self.vat_amount = percent * self.amount_without_vat
        else:
            self.vat_amount = self.not_eu_vat * self.amount_without_vat
        return self.vat_amount
    
    def invoice_amount(self, vat=0):
        self.invoice_amount = self.amount_without_vat + vat
        return self.invoice_amount
    
    def invoice_parameters(self):
        if self.service_provider_vat_payer:
            if (self.customer_country not in self.EU_VAT) & (self.customer_country !=self.service_provider_country):
                self.invoice_amount = self.amount_without_vat
            else:
                vat = self.vat()
                self.invoice_amount = self.invoice_amount(vat)         
        else:
            self.invoice_amount = self.amount_without_vat
        return(self.invoice_amount)