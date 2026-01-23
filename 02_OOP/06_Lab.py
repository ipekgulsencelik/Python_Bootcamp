
"""
============================================================
Coffee Bean Import System
============================================================

Bu modül, dünyanın farklı bölgelerinden kahve çekirdeği ithalatını,
kahve çekirdeklerinin lezzeti ve kalitesi açısından
hasat zamanlarına göre yöneten bir sistem örneğidir.

Kullanılan OOP Prensipleri
-------------------------
1) Abstraction (Soyutlama)
   - BaseService ile tüm ithalat servisleri için ortak sözleşme tanımlanır.

2) Polymorphism (Çok Biçimlilik)
   - ship_from() metodu her ülkede farklı davranış gösterir.

3) Factory Pattern (Basit)
   - Shipment.shipment_method()
   - Ay bilgisine göre hangi servis kullanılacağını belirler.

Senaryo Kuralları
-----------------
- 4–7. aylar     : Kolombiya
- 8–11. aylar    : Sumatra
- 1, 2, 12. aylar: Afrika (Kenya örneği)
- 3. ay          : Hasat yok → ithalat yapılmaz

------------------------------------------------------------
FACTORY DESIGN PATTERN
------------------------------------------------------------

Factory Design Pattern, bir nesnenin *hangi türden* oluşturulacağı
bilgisini, bu nesneyi kullanan taraftan (client code) gizlemeyi amaçlar.

Bu desen sayesinde:
- Nesne oluşturma sorumluluğu tek bir noktada toplanır
- Client code (main) if / else karmaşasından kurtulur
- Yeni bir servis eklendiğinde mevcut kod minimum düzeyde değiştirilir

Bu örnekte Factory Pattern şu şekilde uygulanmıştır:
---------------------------------------------------
- Shipment sınıfı → Factory (Creator)
- BaseService     → Product Interface
- ColumbiaService, SumatraService, KenyaService
                  → Concrete Product

Client code (main):
-------------------
- Concrete sınıfları BİLMEZ
- Sadece BaseService ile çalışır
- Nesnelerin nasıl oluşturulduğuyla ilgilenmez

Bu yapı, Factory Pattern’in temel amacını birebir karşılar.
"""

from abc import ABC, abstractmethod


# ============================================================
# region Abstract Service (Contract)
# ============================================================

class BaseService(ABC):
    """
    Tüm kahve çekirdeği ithalat servisleri için soyut sınıf.

    Bu sınıf bir *sözleşme* görevi görür.
    Alt sınıflar, kahvenin hangi ülkeden geleceğini
    ship_from metodu ile belirtmek zorundadır.
    """

    @abstractmethod
    def ship_from(self) -> str:
        """
        Kahve çekirdeğinin hangi ülkeden gönderileceğini belirtir.

        Returns:
            str: İthalat yapılacak ülke bilgisi.
        """
        pass

# endregion
# ============================================================


# ============================================================
# region Concrete Services (Country Based Imports)
# ============================================================

class SumatraService(BaseService):
    """
    Sumatra (Endonezya) kahve çekirdeği servisi.
    """

    def ship_from(self) -> str:
        return "from Sumatra"


class ColumbiaService(BaseService):
    """
    Kolombiya kahve çekirdeği servisi.
    """

    def ship_from(self) -> str:
        return "from Colombia"


class KenyaService(BaseService):
    """
    Kenya kahve çekirdeği servisi.
    Afrika bölgesi için örnek olarak kullanılır.
    """

    def ship_from(self) -> str:
        return "from Kenya"


class SouthAfricaService(BaseService):
    """
    Güney Afrika kahve çekirdeği servisi.
    (Bu örnekte aktif kullanılmıyor ama genişletilebilirlik için duruyor.)
    """

    def ship_from(self) -> str:
        return "from South Africa"


class DefaultService(BaseService):
    """
    Hasat olmayan veya ithalat yapılamayan durumlar için servis.
    """

    def ship_from(self) -> str:
        return "not available (no harvest)"

# endregion
# ============================================================


# ============================================================
# region Factory (Shipment Decision Maker)
# ============================================================

class Shipment:
    """
    Ay bilgisine göre hangi kahve ithalat servisinin
    kullanılacağını belirleyen Factory sınıfı.

    Bu sınıf Factory Pattern'de:
        → Factory (Creator) rolünü üstlenir.

    Görevi:
        - Ay bilgisine göre doğru Concrete Service'i üretmek
        - Client code'un (main) bu kararı bilmesini engellemek

    Client code şunu söyler:
        "Bana bir BaseService ver"

    Factory şunu çözer:
        "Hangi servis? Columbia mı, Sumatra mı, Kenya mı?"

    Shipment sınıfı bir *nesne davranışı* değil, bir *karar mekanizması* içerir.

    Factory'nin bir durumu (state) olmadığı için nesne üretmeye gerek yoktur.

    Bu sınıfın görevi:
        → Ay bilgisine bak
        → Hangi servis kullanılacak kararını ver

    Bu yüzden burada kullanılan method:
        ✔ static method
    """

    @staticmethod
    def shipment_method(month: int) -> BaseService:
        """
        Bu metodun static olmasının SEBEBİ:

        1️⃣ Bu metot `self` kullanmaz
           - Shipment nesnesinin herhangi bir durumu (state) yoktur.

        2️⃣ Shipment nesnesi üretmenin mantığı yoktur
           - shipment = Shipment() gibi bir nesneye ihtiyaç duyulmaz.

        3️⃣ Bu metot bir *karar verir*
           - Ay → Hangi ülke servisinden ithalat yapılacak?

        4️⃣ Mantıksal olarak sınıfa aittir, nesneye değil
            - Bu yüzden @staticmethod kullanılır.

        Eğer static olmasaydı:

            shipment = Shipment()
            shipment.shipment_method(5)

        Bu şu anlama gelirdi:
            "Shipment nesnesinin bir durumu var ve ona göre karar veriyor"

        Halbuki:
            ❌ Shipment'ın durumu yok
            ✅ Sadece ay → servis eşlemesi var

        Verilen aya göre uygun kahve çekirdeği servisini döner.

        Args:
            month (int):
                1–12 arasında ay bilgisi.

        Returns:
            BaseService:
                İlgili ülkenin servis nesnesi.
        """

        # Kolombiya hasat dönemi
        if 4 <= month <= 7:
            return ColumbiaService()

        # Sumatra hasat dönemi
        elif 8 <= month <= 11:
            return SumatraService()
        
        # Afrika hasat dönemi
        else:
            if month == 1 or month == 2 or month == 12:
                return KenyaService()
            
            # 3. ay: dünyada hasat yok
            else:
                return DefaultService()

# endregion
# ============================================================


# ============================================================
# region Application Entry Point
# ============================================================

def main() -> None:
    """
    Uygulamanın başlangıç noktası.

    1–12 ayları arasında döner,
    her ay için hangi ülkeden kahve çekirdeği ithal edileceğini yazdırır.
    """

    for month in range(1, 13):
        # DİKKAT:
        # shipment_method static olduğu için Shipment() nesnesi oluşturmuyoruz
        shipment_service = Shipment.shipment_method(month)

        print(
            f"Month {month:02d} -> Coffee beans shipment "
            f"{shipment_service.ship_from()}"
         )


if __name__ == "__main__":
    main()

# endregion
# ============================================================