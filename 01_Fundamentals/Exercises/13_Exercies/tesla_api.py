
#! Tesla Articles (NewsAPI) + Author Search
# tesla_data üzerinde icra edilecektir.
# Kullanıcıdan yazar adı alınacaktır.
# Girilen yazar adına göre Tesla makaleleri aranacaktır.
# Arama işlemi:
#   - Tam eşleşme (author == input) VEYA
#   - İçeriyor mu kontrolü (input, author içinde geçiyor mu)
# olacak şekilde yapılacaktır.
# Elde edilen sonuçlar ekrana yazdırılacaktır.

from requests import get
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
from pprint import pprint

try:
    end_point = (
        "https://newsapi.org/v2/everything"
        "?q=tesla&from=2023-02-11&sortBy=publishedAt"
        "&apiKey=a3f6b8ab7c8544bda509d8f4a27cbfff"
    )    

    # API'den isteme talebi
    response = get(end_point, timeout=30)
    response.raise_for_status()  # HTTPError fırlatır (401, 429, 500 vs.)

    # talep sonucunda bize dönen veri kümesini Json (JavaScript Object Notation) tipine dönüştürük. 
    # Json dünya üzerinde ki uygulamalar arasında veri transferi yaparken yoğun olarak kullanılan bir veri türüdür.
    tesla_data = response.json()

    # veri kümesi dictionary olarak gelir.
    # print(type(tesla_data))
    
    # pprint(tesla_data)

    # region Reading
    # articles listesi (None gelirse boş liste)
    # dictionary tipinde olan tesla_data değişkenine, sözlüklere uygulanabilen 
    # get() built-in fonksiyonu ile 'articles' anahtarını parametre olarak gönderdik. 
    # elde ettiğimiz sonuç kümeside bir liste oldu. listeyi 'article_list' değişkenine assign ettik.
    # print(type(tesla_data.get('articles')))
    article_list = tesla_data.get("articles", [])
    # print(type(article_list))
    # pprint(article_list)
    print(f"✅ Total articles: {len(article_list)}")

    # Artık elimde 'article_list' adında bir liste bulunmaktadır. 
    # Listeler içerisinde index mantığı ile her hangi bir makaleyi nokta atışı çekebiliriz.
    if article_list:
        # listenin ilk index'sinde tutulunan makale bulunmaktadır. 
        first_article = article_list[0]

        # listenin item'larını incelediğimizde her bir item'ın bir dictionary olduğunu gözlemleriz. 
        # print(type(first_article))  # 'first_article' değişkenimin tipi bir dictionarydir.
        # print(first_article)
        
        # Soru: İlk makalenin yazar, başlık ve açıklama bildilerini ekrana basınız.
        author = first_article.get("author")
        title = first_article.get("title")
        description = first_article.get("description")

        print("\n--- First Article ---")
        print(f"Author Name: {author}")
        print(f"Title: {title}")
        print(f"Description: {description}")
    else:
        print("❌ No articles returned from API.")
        raise SystemExit
    # endregion


    # region Searching
    # Kullanıcı Yazar ismi giricek 
    # Kullanıcının girdigi yazara ait makale yada makaleler ekrana getirilecek.
    author_name = input("Please type into author name: ").strip().lower()

    print("\nSearch type:")
    print("1 - Exact match (tam eşleşme)")
    print("2 - Contains (içeriyor mu)")

    search_type = input("Choose (1/2): ").strip()

    if search_type not in ("1", "2"):
        print("❌ Invalid choice. Please choose 1 or 2.")
        raise SystemExit

    articles = tesla_data.get("articles", [])

    """ 
    # Path I — Classic for-loop
    matched_articles = []

    for article in articles:
        author = article.get("author")

        if not author:
            continue

        author_lower = author.strip().lower()

        # 1️⃣ Tam eşleşme
        if search_type == "1" and author_lower == author_name:
            matched_articles.append(article)
        # 2️⃣ İçeriyor mu
        elif search_type == "2" and author_name in author_lower:
            matched_articles.append(article)

    if not matched_articles:
        print("❌ No articles found for the given author.")
    else:
        print(f"\n✅ Found {len(matched_articles)} article(s):\n")
        for index, article in enumerate(matched_articles, start=1):
            print(
                f"{index}. {article.get('title', 'No title available')}\n"
                f"   Author: {article.get('author', 'Unknown')}\n"
                f"   Source: {article.get('source', {}).get('name', 'No source available')}\n"
                f"   PublishedAt: {article.get('publishedAt', 'N/A')}\n"
            )
    """

    # Path II — List Comprehension
    # Tam eşleşme
    # matched_articles = [article for article in articles if article.get("author") and article.get("author").strip().lower() == author_name]
    
    matched_articles = [
        article for article in articles
        if article.get("author") and (
            (search_type == "1" and article["author"].strip().lower() == author_name) or
            (search_type == "2" and author_name in article["author"].strip().lower())
        )
    ]

    if not matched_articles:
        print("No articles found for the given author.")
    else:
        print(f"\n✅ Found {len(matched_articles)} article(s):\n")
        for index, article in enumerate(matched_articles, start=1):
            print(
                f"{index}. {article.get('title', 'No title available')}\n"
                f"   Author: {article.get('author', 'Unknown')}\n"
                f"   Source: {article.get('source', {}).get('name', 'No source available')}\n"
                f"   PublishedAt: {article.get('publishedAt', 'N/A')}\n"
                f"   URL: {article.get('url', 'N/A')}\n"
            )
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