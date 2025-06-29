from datetime import datetime


# Invoice wird gefüllt mit Position Objekten.
# Die muss ich alle aus den erhaltenen Daten erstellen

class Invoice:
    def __init__(self, postions, name_of_customer, invoice_id, ):
        self.__postions = postions
        self.__date = datetime.today().strftime("%B %-d, %Y")
        self.__name_of_customer = name_of_customer
        self.__invoice_id = invoice_id

    def get_invoice_total(self):
        return sum(pos.get_total() for pos in self.__postions)

    def get_postions(self):
        return self.__postions

    def get_invoice_number(self):
        return self.__invoice_id

    def get_date(self):
        return self.__date


class Position:
    def __init__(self, commission_type, price, quantity):
        self.__commission_type = commission_type
        self.__price = price
        self.__quantity = quantity

    def get_commission_type(self):
        return self.__commission_type

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def get_total(self):
        return self.__quantity * self.__price
