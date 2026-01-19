# ============================================================
# region ABSTRACTION (SOYUTLAMA) - BILLING DOMAIN
# ============================================================

"""
Bu senaryoda amaç:

- Fatura entity'leri sadece veri taşısın.
- Her fatura türünün hesaplama iş kuralı servislerde olsun.

Ayrıca burada KDV / vergi konusu var:
- vat_rate oran olarak tutulmalı.
  Örn: %25.5 => 0.255

Hesaplama yaklaşımı:
- base_cost = unit_price * usage
- total = base_cost + (base_cost * vat_rate)
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime



# --------------------------
# ENTITY KATMANI (VERİ)
# --------------------------

@dataclass
class BaseBill:
    """
    Tüm faturaların ortak entity alanları.

    - bill_name : fatura adı
    - vat_rate  : KDV oranı (0.20 gibi)
    - unit_price: birim fiyat
    """
    bill_name: str
    vat_rate: float
    unit_price: float


@dataclass
class WaterBill(BaseBill):
    """
    Su faturası.

    - cubic_meter: tüketilen su miktarı (m3)
    """

    cubic_meter: float


@dataclass
class NaturalGasBill(BaseBill):
    """
    Doğalgaz faturası.

    - cubic_meter: tüketilen doğalgaz miktarı (m3)
    """

    cubic_meter: float


@dataclass
class ElectricityBill(BaseBill):
    """
    Elektrik faturası.

    - kwh: tüketilen elektrik miktarı
    """

    kwh: float


# -----------------------------
# B) SERVICE KATMANI (BUSINESS)
# -----------------------------


class BaseBillService(ABC):
    """
    Fatura servisleri için soyut sınıf.

    Sözleşme:
    - calculate_total(bill) alt sınıfta zorunlu.
    Ortak davranış:
    - create_log(bill, total)
    """

    @abstractmethod
    def calculate_total(self, bill: BaseBill) -> float:
        """
        Her fatura türü kendi hesaplama mantığını yazmak zorunda.
        """
        raise NotImplementedError

    def create_log(self, bill: BaseBill, total: float, filename: str = "bill_info.txt") -> str:
        """
        Ortak loglama (somut metot).
        Tüm servisler olduğu gibi kullanabilir.

        Not:
        Burada basit şekilde dosyaya yazıyoruz.
        Gerçek projede:
        - logging modülü
        - veritabanı log tablosu
        - elastic / kibana
        gibi sistemlere gider.
        """
        with open(filename, "a", encoding="utf-8") as f:
            f.write(
                f"Bill Name     : {bill.bill_name}\n"
                f"Unit Price    : {bill.unit_price}\n"
                f"VAT Rate      : {bill.vat_rate}\n"
                f"Total Amount  : {total:.2f}\n"
                f"Payment Date  : {datetime.now().isoformat(sep=' ', timespec='seconds')}\n"
                f"===============================\n"
            )
        return f"{bill.bill_name} payment logged successfully."


class WaterBillService(BaseBillService):
    """
    Su faturası servis.
    """

    def calculate_total(self, bill: WaterBill) -> float:
        base_cost = bill.unit_price * bill.cubic_meter
        return base_cost + (base_cost * bill.vat_rate)


class NaturalGasBillService(BaseBillService):
    """
    Doğalgaz faturası servis.
    """

    def calculate_total(self, bill: NaturalGasBill) -> float:
        base_cost = bill.unit_price * bill.cubic_meter
        return base_cost + (base_cost * bill.vat_rate)


class ElectricityBillService(BaseBillService):
    """
    Elektrik faturası servis.
    """

    def calculate_total(self, bill: ElectricityBill) -> float:
        base_cost = bill.unit_price * bill.kwh
        return base_cost + (base_cost * bill.vat_rate)


def bill_demo() -> None:
    """
    Bill domain demo akışı:
    - Fatura entity oluştur
    - Servis oluştur
    - calculate_total ile hesapla
    - create_log ile logla
    """

    water_bill = WaterBill(
        bill_name="İSKİ",
        vat_rate=0.255,      # %25.5
        unit_price=45.7,     # m3 başına fiyat gibi düşün
        cubic_meter=10       # tüketim
     )

    service = WaterBillService()
    total = service.calculate_total(water_bill)
    msg = service.create_log(water_bill, total)

    print("---- BILL DEMO ----")
    print(msg)
    print(
        f"Bill Name : {water_bill.bill_name}\n"
        f"Unit Price: {water_bill.unit_price}\n"
        f"Usage (m3): {water_bill.cubic_meter}\n"
        f"VAT Rate  : {water_bill.vat_rate}\n"
        f"TOTAL     : {total:.2f}"
      )


# ============================================================
# endregion
# ============================================================


# ============================================================
# region MAIN (ÇALIŞTIRMA)
# ============================================================

def main() -> None:
    """
    Bill demo
    """
    print("\n==== BILL DOMAIN ====")
    bill_demo()


if __name__ == "__main__":
    main()

# ============================================================
# endregion
# ============================================================