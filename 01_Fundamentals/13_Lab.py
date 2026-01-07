
# Bu örnekte 'https://newsapi.org' web api'sinden data talebinde bulunacağız.
# Web API(Application Programming Interface) bizlere spesifik alanlarda veri temin eden platformlardır. Bu işlemi yaparken api'lerden bir talepte (request) bulunu yoruz, api'de bize bir response dönüyor. Bu döndüğü response ise bir data içermektedir.
# Ücretsiz apiler olduğu gibi ücretli apielrde bulunmaktadır. Api'ye bulunduğunuz talep sıklığına göre bir fiyatlandırma söz konusudur.
# Api'lere talepte bulunduğumuzu az önce belirttim. Bu request-response yapısıda bir protokol üzerinden yürümektedir. Bu protokolede HTTP (Hypertext Transfer Protocol) protokolü diyor.


# Bu örnekte bir harici modüle ihtiyacımız bulunmaktadır. Bu modül "requests" modülüdür.
# Request modülün yüklemek için
# 1. İndirileccek paketin ismi yazılır. İndireceğimiz paketin özelliklerini 'https://pypi.org/' sitesinden bulabilirsiniz.
# 2. Terminal açılır.
# 3. Terminale 'pip install requests' yazarak paketimizi indirebiliriz.

from requests import get
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
from pprint import pprint

try:
    end_point = 'https://newsapi.org/v2/everything?q=tesla&from=2023-02-11&sortBy=publishedAt&apiKey=a3f6b8ab7c8544bda509d8f4a27cbfff'
    
    # Aşağıda ki kod ile apimizden tesla makalelerini isteme talebinde bulunduk.
    response = get(end_point, timeout=6000)

    # Yukarıda bulunduğumuz talep sonucunda bize dönen veri kümesini Json (JavaScript Object Notation) tipine dönüştürük. 
    # Json dünya üzerinde uygulamalar arasında veri transferi yaparken yoğun olarak kullanılan bir veri türüdür.
    tesla_data = response.json()

    # Aşağıda ki kodları çalıştırdığımız da elde ettiğimiz veri kümesinin dictionary olduğunu görüyoruz.
    # print(type(tesla_data))
    
    pprint(tesla_data)

    # Burada dictionary tipinde olan tesla_data değişkenime, sözlüklere uygulanabilen get() built-in fonksiyonu ile 'articles' anahtarını parametre olarak gönderdik. 
    # Bunun sonucunda elde ettiğimiz sonuç kümeside bir liste oldu. Bu listeyi 'article_list' değişkenine assigned ettik.
    # print(type(tesla_data.get('articles')))
    article_list = tesla_data.get('articles')
    print(type(article_list))
    pprint(article_list)

    # Artık elimde 'article_list' adında bir liste bulunmaktadır. 
    # Listeler içerisinde index mantığı ile her hangi bir makaleyi nokta atışı çekebilirim.
    # Ayrıca elde ettiğim listenin item'larını incelediğimde her bir item'ın bir dictionary olduğunu gözlemledim. O zaman şu usavurumu yapabilirim. aşağıdaki kodu çalıştırdığımda 'first_article' değişkenimin tipi bir dictionarydir.
    # print(type(tesla_data.get('articles')[0]))
    first_article_dict = article_list[0]
    print(type(first_article_dict))
    print(first_article_dict)

    # Bu noktada elimizde listenin ilk index'sinde tutuluna makale bulunmaktadır. 
    # Çıktıyı incelediğimizde yada değişken tipine baktığımızda bu değişkenin dictionary olduğunu gördük. O halde gene anahtar değer mantığını kullanarak bu sözlük içerisinde bulunan yazar, başlık ve açıklama alanlarını ekrana yazdırabiliriz.

    # Soru: İlk makalenin yazar, başlık ve açıklama bildilerini ekrana basınız
    print(
        f'Author Name: {tesla_data.get("articles")[0].get("author")}\n'
        f'Title: {tesla_data.get("articles")[0].get("title")}\n'
        f'Description: {tesla_data.get("articles")[0].get("description")}\n'
    )

    author = first_article_dict.get('author')
    title = first_article_dict.get('title')
    description = first_article_dict.get('description')

    print(f'Author Name: {author}')
    print(f'Title: {title}')
    print(f'Description: {description}')


    # region Searching
    # Kullanıcı Yazar ismi giricek 
    # Kullanıcının girdigi yazara ait makale yada makaller ekrana getirilecek.
    author_name = input("Author Name: ").strip()

    # Path I — Classic for-loop
    for article in tesla_data.get("articles", []):
        if article.get("author") == author_name:
            pprint(article)

    # Path II — List Comprehension
    results = [article for article in tesla_data.get("articles", []) if article.get("author") == author_name]

    for result in results:
        pprint(result)
    # endregion

except HTTPError as err:
    print(f"HTTP Error: {err}")

except ConnectionError as err:
    print(f"Connection Error: {err}")

except Timeout as err:
    print(f"Timeout Error: {err}")

except RequestException as err:
    print(f"Request Error: {err}")

except Exception as err:
    print(f"Unexpected Error: {err}")