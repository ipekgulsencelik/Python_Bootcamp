
# Dünyanın farklı lokasyonalrından kahve çekirdeği ithal edeceğiz.
# Lakin kahce çekirdeklerinin lezzeti ve kalitesi açısından hasat zamanları göz önünde bulundurularak ital edilmesi gerekmektedir.
# 4-11 aylar arasında columbia 'dan ithal edilecek
# 1 yada 2 yada 12 . aylarda africadan
# 3. ayda ise dünyada hasat bulunmadığından herhangi bir çekirdek ithal edilmeyecek

from abc import ABC, abstractmethod


class BaseService(ABC):

    @abstractmethod
    def ship_from(self) -> str: pass


class SumatraService(BaseService):
    def ship_from(self) -> str:
        return 'from Samutra'


class ColumbiaService(BaseService):
    def ship_from(self) -> str:
        return 'from Columnia'


class KenyaService(BaseService):
    def ship_from(self) -> str:
        return 'from Kenya'


class SouthAfrica(BaseService):
    def ship_from(self) -> str:
        return 'South Afirca'


class DefaultService(BaseService):
    def ship_from(self) -> str:
        return 'not avaliable'


class Shipment:
    @staticmethod
    def shipment_method(month) -> BaseService:
        if 4 <= month <= 7:
            return ColumbiaService()
        elif 8 <= month <= 11:
            return SumatraService()
        else:
            if month == 1 or month == 2 or month == 12:
                return KenyaService()
            else:
                return DefaultService()


def main():
    for month in range(1, 13):
        product_shipment = Shipment.shipment_method(month)
        print(f'Coffee beans shipment {product_shipment.ship_from()}')


main()