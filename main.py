import requests

api_key = "ef4019274a94408b9a1284a04ccbbe41"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-05-08&sortBy=publishedAt&apiKey=" \
      "ef4019274a94408b9a1284a04ccbbe41"

# Make a request
request = requests.get(url)

# Get a dictionary with json
content = request.json()

# Accessing the article titles and its descriptions
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
