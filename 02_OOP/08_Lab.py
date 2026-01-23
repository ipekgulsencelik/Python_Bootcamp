
"""
============================================================
Credit Card Builder
============================================================

Bu örnek, farklı türde kredi kartlarının (Visa, American Express vb.)
aynı nesne yapısı üzerinden fakat farklı özelliklerle
oluşturulmasını gösterir.

------------------------------------------------------------
BUILDER DESIGN PATTERN
------------------------------------------------------------

Builder Design Pattern, karmaşık bir nesnenin
adım adım (step-by-step) oluşturulmasını sağlar.

Amaç:
- Nesnenin oluşturulma sürecini, nesnenin kendisinden ayırmak
- Aynı nesneyi farklı konfigürasyonlarla üretmek
- Constructor şişmesini (çok fazla parametre) engellemek

Bu örnekte:
-------------
- CreditCard              → Product
- CreditCardBuilder       → Builder (Abstract)
- AmericanExpressCard     → Concrete Builder
- VisaCard                → Concrete Builder
- Creator                 → Director
"""

from abc import ABC, abstractmethod


# ============================================================
# region Product
# ============================================================

class CreditCard:
    """
    Oluşturulacak karmaşık nesne (Product).

    Attributes:
        bank_name (str):
            Kartı veren banka.

        card_limit (int):
            Kredi kartı limiti.

        card_type (str):
            Kart tipi (Visa, American Express vb.).

        installment_shopping (bool):
            Taksitli alışveriş yapılabilir mi?
    """

    def __init__(self):
        self.bank_name = None
        self.card_limit = None
        self.card_type = None
        self.installment_shopping = False
        # sınıfı initilize ederken dışarıdan parametre almayacağımdan 
        # düz bir biçimde object attribute'Leri tanımladım.

# endregion
# ============================================================


# ============================================================
# region Builder (Abstract Builder)
# ============================================================

class CreditCardBuilder(ABC):
    """
    Builder Design Pattern'de Abstract Builder rolünü üstlenir.

    Bu sınıf:
    - CreditCard nesnesini oluşturur
    - Hangi adımların uygulanması gerektiğini TANIMLAR
    - Nasıl uygulanacağını alt sınıflara bırakır
    """

    def __init__(self):
        self._credit_card = CreditCard()

    @property
    def credit_card(self) -> CreditCard:  # __init__() tetiklendiğin CreditCard sınıfının instance otomatik olarak alınacak ve bu objeyi bu ata sınıftan beslenen alt sınıflarda kulalnmak üzere bir fonksiyon yazdım. Lakin bu fonksiyon bir attribute gibi davaranaktır. BUnu temin eden yapı ise üzerine yazdığımız "@property" decoratörüdür.

        """
        Oluşturulan CreditCard nesnesini döner.

        Returns:
            CreditCard: oluşturulan kart nesnesi
        """
        return self._credit_card

    @abstractmethod
    def bank_name_func(self) -> str:
        """Kartın bağlı olduğu bankayı ayarlar."""
        pass

    @abstractmethod
    def card_limit_func(self) -> int:
        """Kart limitini ayarlar."""
        pass

    @abstractmethod
    def card_type_func(self) -> str:
        """Kart tipini ayarlar."""
        pass

    @abstractmethod
    def installment_shopping_func(self) -> bool:
        """Taksitli alışveriş özelliğini ayarlar."""
        pass

# endregion
# ============================================================


# ============================================================
# region Concrete Builders
# ============================================================

class AmericanExpressCard(CreditCardBuilder):
    """
    Concrete Builder - American Express Kartı
    """

    def __init__(self):
        super().__init__()
        self._credit_card = super().credit_card

    def bank_name_func(self) -> str:
        self._credit_card.bank_name = "Garanti"
        return self._credit_card.bank_name

    def card_limit_func(self) -> int:
        self._credit_card.card_limit = 1_000_000
        return self._credit_card.card_limit

    def card_type_func(self) -> str:
        self._credit_card.card_type = "American Express"
        return self._credit_card.card_type

    def installment_shopping_func(self) -> bool:
        self._credit_card.installment_shopping = True
        return self._credit_card.installment_shopping


class VisaCard(CreditCardBuilder):
    """
    Concrete Builder - Visa Kartı
     """

    def __init__(self):
        super().__init__()
        self._credit_card = super().credit_card

    def bank_name_func(self) -> str:
        self._credit_card.bank_name = "İş Bankası"
        return self._credit_card.bank_name

    def card_limit_func(self) -> int:
        self._credit_card.card_limit = 10_000_000
        return self._credit_card.card_limit
    
    def card_type_func(self) -> str:
        self._credit_card.card_type = "Visa"
        return self._credit_card.card_type

    def installment_shopping_func(self) -> bool:
        self._credit_card.installment_shopping = True
        return self._credit_card.installment_shopping

# endregion
# ============================================================


# ============================================================
# region Director
# ============================================================

class Creator:
    """
    Director sınıfı, Builder Pattern'de
    nesnenin OLUŞTURULMA SIRASINI yöneten sınıftır.

    Önemli nokta:
    -------------
    Director:
    - Concrete Builder'ı bilmez
    - Sadece Abstract Builder ile çalışır
    """

    @staticmethod
    def create_credit_card(credit_card_builder: CreditCardBuilder) -> None:
        """
        STATIC METHOD:
        Creator sınıfının bir durumu (state) yoktur.
        Sadece builder üzerinden adımları çalıştırır.

        Bu yüzden create metodu static olarak tanımlanmıştır.
        """

        print(
            f"Bank Name : {credit_card_builder.bank_name_func()}\n"
            f"Card Limit: {credit_card_builder.card_limit_func()}\n"
            f"Card Type : {credit_card_builder.card_type_func()}\n"
            f"Installment Shopping  : {credit_card_builder.installment_shopping_func()}\n"
        )

# endregion
# ============================================================


# ============================================================
# region Application Entry Point
# ============================================================

def main() -> None:
    """
    Client code.

    Client:
    - Concrete Builder seçer
    - Nesnenin nasıl oluşturulduğunu BİLMEZ
    """

    Creator.create_credit_card(credit_card_builder=AmericanExpressCard())
    Creator.create_credit_card(credit_card_builder=VisaCard())


if __name__ == "__main__":
    main()

# endregion
# ============================================================