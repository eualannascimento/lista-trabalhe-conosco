from googlesearch import search

query = "Accenture trabalhe conosco carreiras"
for url in search(query, num_results=3, lang="pt"):
    print(url)
