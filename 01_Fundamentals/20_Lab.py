
#! Basit Bankamatik uygulaması - ATM Application

from uuid import uuid4

burak_account = {
    'id': str(uuid4()),
    'name': 'burak yilmaz',
    'username': 'beast',
    'password': '123',
    'account_no': '12345',
    'balance': 3000,
    'additional_balance': 2000,
    'additional_limit': 2000
}

hakan_account = {
    'id': str(uuid4()),
    'name': 'hakan yilmaz',
    'username': 'bear',
    'password': '987',
    'account_no': '98745',
    'balance': 4000,
    'additional_balance': 6000,
    'additional_limit': 6000
}

ipek_account = {
    'id': str(uuid4()),
    'name': 'ipek yilmaz',
    'username': 'keko',
    'password': '456',
    'account_no': '98456',
    'balance': 1000,
    'additional_balance': 1000,
    'additional_limit': 1000
}

USERS = [burak_account, hakan_account, ipek_account]


# region Captcha
def generate_captcha() -> str:
    """
    Basit bir güvenlik kodu (captcha) üretir.

    Bu fonksiyon UUID4 kullanarak rastgele bir değer oluşturur
    ve bu değerin '-' ile ayrılmış parçalarından ikinci kısmını
    captcha olarak döndürür.

    uuid4 çıktısı örneği:
        'f29a0c7f-7f1a-4a4c-8c5b-1c2a3d4e5f6a'

    split("-") ile parçalayınca:
        ['f29a0c7f', '7f1a', '4a4c', '8c5b', '1c2a3d4e5f6a']

    Biz burada [1] (2.parça) alıp captcha gibi kullanıyoruz.

    Returns:
        str: Kullanıcıdan istenecek captcha metni.
    """
    return str(uuid4()).split("-")[1]
# endregion


# region Auth
def login(username: str, password: str, user_captcha: str, captcha: str) -> dict:
    """
    Kullanıcı giriş doğrulamasını yapar.

    Kontroller:
        - Kullanıcı adı doğru mu?
        - Şifre doğru mu?
        - Girilen captcha, üretilen captcha ile eşleşiyor mu?

    Tüm kontroller başarılıysa ilgili kullanıcı hesabı döndürülür.
    Aksi durumda boş bir sözlük ({}) döner.

    Args:
        username (str): Kullanıcının girdiği kullanıcı adı.
        password (str): Kullanıcının girdiği şifre.
        user_captcha (str): Kullanıcının girdiği güvenlik kodu.
        captcha (str): Sistem tarafından üretilen güvenlik kodu.

    Returns:
        dict: Başarılı girişte kullanıcı hesabı, başarısızsa {}.
    """
    for user in USERS:
        if (
            user["username"] == username
            and user["password"] == password
            and user_captcha == captcha
        ):
            return user

    return {}
# endregion


# region Input Helpers
def get_int(prompt: str) -> int:
    """
    Kullanıcıdan güvenli bir şekilde tam sayı (int) girişi alır.

    Bu fonksiyon, kullanıcıdan alınan input'u kontrol eder:
        - Girilen değer int'e çevrilebiliyorsa döndürür
        - Çevrilemiyorsa (harf, özel karakter vb.) kullanıcıyı uyarır ve tekrar giriş ister

    Amaç:
        - int(input()) kullanımında oluşabilecek ValueError hatalarını
          önlemek
        - Programın beklenmeyen şekilde çökmesini engellemek

    Args:
        prompt (str): Kullanıcıya gösterilecek input mesajı

    Returns:
        int: Kullanıcıdan alınan geçerli tam sayı değeri
    """
    while True:
        value = input(prompt).strip()
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid number!")


def get_valid_answer(question: str, valid_options: tuple) -> str:
    """
    Kullanıcıdan geçerli bir cevap alana kadar input ister.

    Girilen cevap:
        - strip() ile boşluklardan arındırılır
        - lower() ile küçük harfe çevrilir

    Args:
        question (str): Kullanıcıya sorulacak soru
        valid_options (tuple[str, ...]): Kabul edilen cevaplar (örn: ('y', 'n'))

    Returns:
        str: Geçerli ve normalize edilmiş kullanıcı cevabı
    """
    valid_options = tuple(opt.strip().lower() for opt in valid_options)
    question += f'({", ".join(valid_options)}): '

    while True:
        response = input(question).strip().lower()

        if response in valid_options:
            return response
        
        print('Please type the valid options..!')
# endregion


# region Account UI
def account_information(account: dict) -> None:
    """
    Hesap özetini formatlı şekilde ekrana yazdırır.

    Beklenen anahtarlar:
        - name
        - account_no
        - balance
        - additional_balance
    """
    print(
        "\n================ ACCOUNT INFO ================\n"
        f"Name              : {account['name']}\n"
        f"Account No        : {account['account_no']}\n"
        f"Balance           : {account['balance']}\n"
        f"Additional Balance: {account['additional_balance']} / {account['additional_limit']}\n"
        "==============================================\n"
    )


def check_balance(account: dict) -> None:
    """
    Menüden 'Bakiye Sorgula' seçildiğinde çağrılır.
    """
    account_information(account)
# endregion


# region Banking Operations
def withdraw_money(account: dict, amount: int, transaction_name: str = "owner") -> bool:
    """
    Hesaptan para çekme işlemini gerçekleştirir.

    Kurallar:
        1) Ana bakiye yeterliyse:
            - Tutar doğrudan ana bakiyeden düşülür
        2) Ana bakiye yetersizse:
            - Toplam bakiye (ana + ek) kontrol edilir
            - Toplam yeterliyse kullanıcıya ek bakiye kullanımı sorulur
            - Kullanıcı onaylarsa ek bakiye devreye girer
        3) Toplam bakiye yetersizse:
            - İşlem iptal edilir

    Args:
        account (dict): İşlem yapılacak hesap.
        amount (int): Çekilmek istenen tutar.
         transaction_name (str):
            İşlemin türü.
            'owner' ise hesap bilgileri ekrana yazdırılır,
            'eft' ise sessiz çalışır.

    Returns:
        bool: İşlem başarılıysa True, aksi halde False.
    """
    if amount <= 0:
        print("Amount must be greater than 0!")
        return False
    
    # Ana bakiye yeterli mi?
    if account['balance'] >= amount:
        account['balance'] -= amount
        print("Withdraw successful (main balance).")
        if transaction_name == "owner":
            account_information(account=account)
        return True
    else:
        # Toplam (ana + ek) yeterli mi?
        total_balance = account['balance'] + account['additional_balance']

        if total_balance >= amount:
            # Ek bakiye kullanılsın mı?
            used_additional_balance = get_valid_answer(question="Insufficient balance..!\nDo you want to use additional balance?", valid_options=("y", "n"))

            match used_additional_balance:
                case 'y':
                    needed = amount - account['balance']
                    account['balance'] = 0
                    account['additional_balance'] -= needed
                    print("Withdraw successful (used additional balance).")
                    if transaction_name == "owner":
                        account_information(account=account)
                    return True
                case 'n':
                    print("Transaction has been canceled by user..!")
                    if transaction_name == "owner":
                        account_information(account=account)
                    return False
        else:
            print("Insufficient balance..!\nTransaction has been canceled..!")
            if transaction_name == "owner":
                account_information(account=account)
            return False


def deposit_money(account: dict, amount: int, transaction_name: str = "owner") -> bool:
    """
    Hesaba para yatırma işlemini gerçekleştirir.

    Bankacılık mantığı:
        - Eğer ek bakiye (kredi limiti) daha önce kullanılmışsa, yatırılan para önce bu bakiyeyi limite kadar doldurur
        - Ek bakiye tamamen dolduktan sonra kalan tutar ana bakiyeye eklenir

    Args:
        account (dict): İşlem yapılacak hesap.
        amount (int): Yatırılacak tutar.
        transaction_name (str):
            'owner' ise işlem sonrası hesap bilgileri gösterilir.

    Returns:
        bool: Yatırma işlemi başarılıysa True.
    """
    if amount <= 0:
        print("Amount must be greater than 0!")
        return False

    additional_limit = account.get("additional_limit", 0)
    current_additional = account.get("additional_balance", 0)

    # Ek bakiyede ne kadar eksik var?
    debt = additional_limit - current_additional

    if debt > 0:
        # Yatırılan para borcu tamamen kapatabiliyor mu?
        if amount >= debt:
            # Borcun tamamı kapanır
            account['additional_balance'] += debt
            amount -= debt
        else:
            # Para borcu kapatmaya yetmez
            account['additional_balance'] += amount
            amount = 0

    # Kalan para (varsa) ana bakiyeye eklenir
    account['balance'] += amount

    if transaction_name == "owner":
        print("Deposit successful.")
        account_information(account=account)

    return True


def eft_money(account: dict, receiver_no: str, amount: int) -> None:
    """
    Bir hesaptan başka bir hesaba EFT işlemi yapar.

    İşlem adımları:
        - Alıcı hesap doğrulanır
        - Gönderici hesaptan para çekilir
        - Alıcı hesaba para yatırılır

    Args:
        account (dict): Gönderici hesap.
        receiver_no (str): Alıcı hesap numarası.
        amount (int): Gönderilecek tutar.
    """
    # Validasyon
    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    if account.get("account_no") == receiver_no:
        print("You cannot transfer money to your own account.")
        return
    
    # Path I
    # receiver bul
    # found = [user for user in USERS if user.get('account no') == receiver_no]
    # if not found:
    #     print("Alıcı bulunamadı. EFT iptal.")
    #     return
    # receiver = found[0]

    # Path II
    receiver = None
    for user in USERS:
        if user.get('account_no') == receiver_no:
            receiver = user
            break

    if receiver is None:
        print("Receiver account not found. EFT canceled.")
        return

    ok = withdraw_money(account=account, amount=amount, transaction_name="eft")
    if not ok:
        print("Insufficient balance. EFT canceled.")
        return

    deposit_money(account=receiver, amount=amount, transaction_name='eft')
    print("EFT successful.")
# endregion


# region Main App
def main():
    """
    Konsol tabanlı ATM uygulamasını çalıştırır.

    Akış:
        1) Captcha üretilir ve kullanıcıya gösterilir.
        2) Kullanıcı adı, şifre ve captcha istenir.
        3) Giriş başarılıysa menü açılır:
            - 1: Bakiye sorgula
            - 2: Para çek
            - 3: Para yatır
            - 4: EFT yap
            - e: Çıkış
    """
    counter = 3

    while counter > 0:
        captcha = generate_captcha()
        print(f"Security Code: {captcha}")

        username = input("Username: ").strip()
        password = input("Password: ").strip()
        user_captcha = input("Security Code: ").strip()

        account = login(username, password, user_captcha, captcha)

        if not account:
            print('Invalid Credentials..!')
            counter -= 1
            print(f'Remaining attempts: {counter}')
            continue
        
        print(f'Welcome, {account["account_no"]}')

        while True:
            print(
                "Exit                ==> (e)\n"
                "Check balance       ==> (1)\n"
                "Withdraw money      ==> (2)\n"
                "Deposit money       ==> (3)\n"
                "EFT money           ==> (4)\n"
            )

            process = input("Please select an option: ").strip().lower()

            if process == "e":
                print("Goodbye!")
                break
            elif process == '1':
                check_balance(account)
            elif process == '2':
                withdraw_amount = get_int("Withdrawal amount: ")
                withdraw_money(account=account, amount=withdraw_amount)
            elif process == '3':
                deposit_amount = get_int("Deposit amount: ")
                deposit_money(account=account, amount=deposit_amount)
            elif process == "4":
                receiver_no = input('Receiver No: ').strip()
                try:
                    amount = int(input('Amount: '))
                except ValueError:
                    print("Amount must be a number!")
                    continue

                eft_money(account=account, receiver_no=receiver_no, amount=amount)
            else:
                print("Invalid option!")
# endregion


main()