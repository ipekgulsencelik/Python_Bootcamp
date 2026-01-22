

from abc import ABC, abstractmethod


class CreditCard:
    def __init__(self):
        self.bank = ''
        self.card_limit = 0
        self.card_type = ''
        self.installment_shopping = False
        # sınıfı initilize ederken dışarıdan parametre almayacağımdan düz bir biçimde object attribute'Leri tanımladım.4


class CreditCardBuilder(ABC):
    def __init__(self):
        self._credit_card = CreditCard()

    @property
    def credit_card(self) -> CreditCard:  # __init__() tetiklendiğin CreditCard sınıfının instance otomatik olarak alınacak ve bu objeyi bu ata sınıftan beslenen alt sınıflarda kulalnmak üzere bir fonksiyon yazdım. Lakin bu fonksiyon bir attribute gibi davaranaktır. BUnu temin eden yapı ise üzerine yazdığımız "@property" decoratörüdür.
        return self._credit_card

    @abstractmethod
    def bank_name_func(self) -> str: pass

    @abstractmethod
    def card_limit_func(self) -> int: pass

    @abstractmethod
    def card_type_func(self) -> str: pass

    @abstractmethod
    def installment_shopping_func(self) -> bool: pass


class AmericanExpressCard(CreditCardBuilder):
    def __init__(self):
        super().__init__()
        self._credit_card = super().credit_card

    def bank_name_func(self) -> str:
        self._credit_card.bank = 'Garanti'
        return self._credit_card.bank

    def card_limit_func(self) -> int:
        self._credit_card.card_limit = 50000
        return self._credit_card.card_limit

    def card_type_func(self) -> str:
        self._credit_card.card_type = "American Express"
        return self._credit_card.card_type

    def installment_shopping_func(self) -> bool:
        self._credit_card.installment_shopping = True
        return self._credit_card.installment_shopping


class VisaCard(CreditCardBuilder):
    def __init__(self):
        super().__init__()
        self._credit_card = super().credit_card

    def bank_name_func(self) -> str:
        self._credit_card.bank = 'İş Bankası'
        return self._credit_card.bank

    def card_limit_func(self) -> int:
        self._credit_card.card_limit = 80000
        return self._credit_card.card_limit

    def card_type_func(self) -> str:
        self._credit_card.card_type = "Visa Card"
        return self._credit_card.card_type

    def installment_shopping_func(self) -> bool:
        self._credit_card.installment_shopping = True
        return self._credit_card.installment_shopping


class Creator:
    @staticmethod
    def create_credit_card(credit_card_builder: CreditCardBuilder):
        print(f'Bank Name: {credit_card_builder.bank_name_func()}')
        print(f'Card Limit: {credit_card_builder.card_limit_func()}')
        print(f'Card Type: {credit_card_builder.card_type_func()}')
        print(f'Installment Shopping: {credit_card_builder.installment_shopping_func()}')


def main():
    Creator.create_credit_card(AmericanExpressCard())
    Creator.create_credit_card(VisaCard())


main()