
#! Basit Barbut Oyunu

from random import randint, choice

easy_bots = ['elton', 'adal', 'özlem', 'furkan', 'mirza']
hard_bots = ['burak', 'hakan', 'ipek']

users = {
    '1': {
        'username': 'beast',
        'password': '123',   # demo amaçlı
        'safe': 2000
    },
    '2': {
        'username': 'savage',
        'password': '123',
        'safe': 2000
    },
    '3': {
        'username': 'bear',
        'password': '657',
        'safe': 3000
    }
}

minimum_bet = 100


def gain_daily_chips(x: int = 1000, y: int = 2000) -> int:
    """
    Günlük ücretsiz chip kazancı üretir.

    Args:
        x (int): Minimum kazanılacak chip.
        y (int): Maksimum kazanılacak chip.

    Returns:
        int: x ile y arasında rastgele chip miktarı.
    """
    return randint(x, y)


def select_bot_player(bots_type: list = easy_bots) -> str:
    """
    Verilen bot havuzundan rastgele rakip seçer.

    Args:
        bots_type (list): Bot isimleri listesi. Varsayılan easy_bots.

    Returns:
        str: Seçilen bot adı.
    """
    return choice(bots_type)


def is_bet_valid(current_bet: int, safe: int) -> bool:
    """
    Bahis miktarı minimum bahis ile kullanıcının kasası arasında mı kontrol eder.

    Args:
        current_bet (int): Kullanıcının girdiği bahis.
        safe (int): Kullanıcının mevcut kasası.

    Returns:
        bool: Bahis geçerliyse True, değilse False.
    """
    return minimum_bet <= current_bet <= safe


def roll_dice() -> int:
    """
    2 ile 12 arasında (iki zar toplamı gibi) rastgele sayı döndürür.

    Returns:
        int: 2..12 arası zar sonucu.
    """
    return randint(2, 12)


def update_safe(user: dict, chip_amount: int, status: str = "win") -> str:
    """
    Kullanıcının kasasını (safe) kazanma/kaybetme durumuna göre günceller.

    Args:
        user (dict): Kullanıcı sözlüğü.
        chip_amount (int): Eklenecek / çıkarılacak chip miktarı.
        status (str): "win" veya "lose". Varsayılan "win".

    Returns:
        str: Kullanıcıya gösterilecek mesaj.
    """
    safe = int(user.get("safe", 0))

    if chip_amount < 0:
        raise ValueError("chip_amount negatif olamaz")

    if status not in ("win", "lose"):
        raise ValueError("status 'win' veya 'lose' olmalı")

    if status == "win":
        safe += chip_amount
        user["safe"] = safe
        return f"Well done..!\nYour current safe is {safe}"

    # lose
    if safe - chip_amount < 0:
        return "You lost..!\nYour safe is not enough"

    safe -= chip_amount
    user["safe"] = safe
    return f"You lost..!\nYour current safe is {safe}"


def login(users_dict: dict) -> dict | None:
    """
    Kullanıcıdan username/password alır ve doğrulama yapar.

    Not:
        Kullanıcı 'q' yazarsa login iptal edilir.

    Args:
        users_dict (dict): Tüm kullanıcıların tutulduğu sözlük.

    Returns:
        dict | None: Başarılıysa kullanıcı dict'i, değilse None.
    """
    print("=== LOGIN ===")
    while True:
        username = input("Username (q to quit): ").strip().lower()
        if username in ("q", "quit", "exit"):
            return None

        password = input("Password: ").strip()

        for user in users_dict.values():
            if user.get("username") == username and user.get("password") == password:
                print("Login successful!\n")
                return user

        print("Wrong username or password. Try again.\n")


def main():
    """
    Oyunun ana akışını çalıştırır:
    - Login
    - Zorluk seçimi
    - Günlük chip
    - Döngü: bahis al -> zar at -> kasa güncelle
    """
    sign_user = login(users)
    if not sign_user:
        print("Exiting...")
        return
    
    difficulty = input("Choose difficulty (easy/hard) [easy]: ").strip().lower()
    bot_pool = hard_bots if difficulty == "hard" else easy_bots

    gained_chip = gain_daily_chips()
    msg = update_safe(user=sign_user, chip_amount=gained_chip, status="win")

    print(
        f'Welcome, {sign_user.get("username")}\n'
        f'You earned daily free chips --> {gained_chip}\n'
        f'{msg}\n'
        f'Type "q" anytime to quit.\n'
    )

    while True:
        safe = int(sign_user.get("safe", 0))

        if safe < minimum_bet:
            print(f'Your safe ({safe}) is under the minimum table bet..\n')
            break

        opponent = select_bot_player(bot_pool)
        print(f'Your opponent came: {opponent}  (difficulty: {difficulty or "easy"})')

        raw = input("Please make a bet (q to quit): ").strip().lower()
        if raw in ("q", "quit", "exit"):
            print("Bye! 👋")
            break

        try:
            bet = int(raw)   # ✅ tek input’tan bet alıyoruz
            if bet <= 0:
                print("Bet must be greater than 0.\n")
                continue
        except ValueError:
            print("Please enter a number!\n")
            continue

        if not is_bet_valid(current_bet=bet, safe=safe):
            print("Your bet is not valid..!\n")
            continue

        user_roll = roll_dice()
        bot_roll = roll_dice()

        print(f"You rolled: {user_roll} | Bot rolled: {bot_roll}")

        # EASY MODE
        if difficulty != "hard":
            if user_roll > bot_roll:
                print(update_safe(user=sign_user, chip_amount=bet, status="win"))
            elif bot_roll > user_roll:
                print(update_safe(user=sign_user, chip_amount=bet, status="lose"))
            else:
                print("It's a tie! Your bet is returned.\n")
        # HARD MODE (reroll)
        else:
            reroll_count = 0
            max_reroll = 3

            while user_roll == bot_roll and reroll_count < max_reroll:
                reroll_count += 1
                print(f"Tie! Rerolling... ({reroll_count}/{max_reroll})")

                user_roll = roll_dice()
                bot_roll = roll_dice()
                print(f"You rolled: {user_roll} | Bot rolled: {bot_roll}")

            if user_roll > bot_roll:
                print(update_safe(user=sign_user, chip_amount=bet, status="win"))
            elif bot_roll > user_roll:
                print(update_safe(user=sign_user, chip_amount=bet, status="lose"))
            else:
                print("Still tie after rerolls. Bet returned.\n")



main()