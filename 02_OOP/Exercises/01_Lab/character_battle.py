
# Character isminde bir sınıf yaratalım
# Object Attribute => name, race, role, level, weapon, armour, hp
# attack, defend, escape => fonksiyonları olsun
# saldırırken level + weapon kadar vursun
# savunurken level + armour kadar savunsun
# escape olduğunda tapuk yapsın

class Character:
    """
    Character sınıfı bir savaş karakterini temsil eder.

    Object Attributes (Nesne Özellikleri):
        - name   : Karakter adı
        - race   : Irk
        - role   : Rol / sınıf (savaşçı, asker vs.)
        - level  : Seviye (güç belirleyici)
        - weapon : Silah gücü
        - armour : Zırh gücü
        - hp     : Can puanı (health point)
    """

    def __init__(self, name: str, race: str, role: str,  level: int, weapon: int, armour: int, hp: int):
        # Karakter temel bilgileri
        self.name = name
        self.race = race
        self.role = role

        # Savaş istatistikleri
        self.level = level
        self.weapon = weapon
        self.armour = armour
        self.hp = hp

    # --------------------------------------------------------
    # Attack Method
    # --------------------------------------------------------
    def attack(self) -> int:
        """
        Karakterin saldırı gücünü hesaplar.

        Formül:
            attack_power = level + weapon

        Returns:
            int: toplam saldırı gücü
        """
        return self.level + self.weapon

    # --------------------------------------------------------
    # Defend Method
    # --------------------------------------------------------
    def defend(self) -> int:
        """
        Karakterin savunma gücünü hesaplar.

        Formül:
            defend_power = level + armour

        Returns:
            int: toplam savunma gücü
        """
         return self.level + self.armour

    # --------------------------------------------------------
    # Escape Method
    # --------------------------------------------------------
    def escape(self) -> None:
        """
        Karakterin savaştan kaçmasını temsil eder.
        """
        print(f"{self.name} escape. Cowered..! 🏃‍♂️💨")


# endregion
# ============================================================


# ============================================================
# region Helper Functions
# ============================================================

def calculate_damage(attack_power: int, defend_power: int) -> int:
    """
    Hasar hesaplama fonksiyonu.

    Eğer savunma saldırıdan büyükse,
    hasar negatif olmasın diye 0 döner.

    Args:
        attack_power (int): saldırı gücü
        defend_power (int): savunma gücü

    Returns:
        int: gerçek hasar
    """
    return max(0, attack_power - defend_power)


def print_round_info(turn: int, attacker: Character, defender: Character, damage_to_defender: int,
                     damage_to_attacker: int) -> None:
    """
    Tur bilgilerini ekrana düzenli basar.
    """
    print("=" * 35)
    print(f"Tur: {turn}")
    print(f"{attacker.name} verdiği hasar --> {damage_to_defender}")
    print(f"{defender.name} verdiği hasar --> {damage_to_attacker}")
    print("-" * 35)
    print(f"{attacker.name} kalan can --> {attacker.hp}")
    print(f"{defender.name} kalan can --> {defender.hp}")
    print("=" * 35)


# endregion
# ============================================================


# ============================================================
# region Main Battle Loop
# ============================================================

def main() -> None:
    """
    Oyunun başladığı ana fonksiyon.
    """

    # Oyuncu karakterleri oluşturuluyor
    kara_murat = Character(name="Kara Murat", race="Türk", role="Akıncı", level=100, weapon=100, armour=0, hp=1000)
    savage_viking = Character(name="Raider", race="Viking",  role="Asker", level=80, weapon=80, armour=100, hp=1000)

    turn = 1

    # Sonsuz döngü (savaş bitene kadar)
    while True:
        action = input(
            "\nFor Attack  ==> 'a'\n"
            "For Defend  ==> 'd'\n"
            "For Escape  ==> 'e'\n"
            "Choose your move: "
        ).lower().strip()

        # ----------------------------------------------------
        # Escape
        # ----------------------------------------------------
        if action == "e":
            kara_murat.escape()
            print("Savaş sona erdi.")
            break

        # ----------------------------------------------------
        # Defend
        # ----------------------------------------------------
        elif action == "d":
            # Viking saldırır, Kara Murat savunur
            damage = calculate_damage(savage_viking.attack(), 
                                      kara_murat.defend() + 20  # savunma bonusu
                                    )
            kara_murat.hp -= damage

            print("=" * 35)
            print(f"Tur: {turn}")
            print(f"{savage_viking.name} verdiği hasar --> {damage}")
            print(f"{kara_murat.name} savunmada, saldırmadı.")
            print("=" * 35)

        # ----------------------------------------------------
        # Attack
        # ----------------------------------------------------
        elif action == "a":
            # Karşılıklı saldırı
            viking_damage = calculate_damage(savage_viking.attack(), kara_murat.defend())

            murat_damage = calculate_damage(kara_murat.attack(), savage_viking.defend())

            kara_murat.hp -= viking_damage
            savage_viking.hp -= murat_damage

            print_round_info(turn, kara_murat, savage_viking, murat_damage, viking_damage)

        else:
            print("Geçersiz seçim!")
            continue

        # ----------------------------------------------------
        # Kazanan Kontrolü
        # ----------------------------------------------------
        if kara_murat.hp <= 0 and savage_viking.hp > 0:
            print(f"{savage_viking.name} kazandı! 🏆")
            break
        elif kara_murat.hp > 0 and savage_viking.hp <= 0:
            print(f"{kara_murat.name} kazandı! 🏆")
            break
        elif kara_murat.hp <= 0 and savage_viking.hp <= 0:
            print("İkiniz de düştünüz! ☠️")
            break

        turn += 1


# Program giriş noktası
if __name__ == "__main__":
    main()

# endregion
# ============================================================