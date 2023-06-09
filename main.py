import requests
from flask import Flask
from flask_mail import Mail, Message
import smtplib, ssl

app = Flask(__name__)

app.config["MAIL_SERVER"]= "smtp.gmail.com"
app.config["MAIL_PORT"]= 465
app.config["MAIL_USERNAME"]="eglebabachinaite123@gmail.com"
app.config["MAIL_PASSWORD"]= open("password", "r").read()
app.config["MAIL_USE_TLS"]= False
app.config["MAIL_USE_SSL"]= True
mail = Mail(app)

api_key = open("api_key", "r").read()
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-05-09&" \
      "sortBy=publishedAt&apiKey="+api_key

# ----------MAKE A REQUEST----------
request = requests.get(url)
# Get a dictionary with json
content = request.json()

# Accessing the article titles and its descriptions
def get_Data():
    for article in content["articles"]:
        title = article["title"]
        description = article["description"]
        url = article["url"]
        full_text = f"{title} \n {description} \n {url}"
        return full_text
data = get_Data()


@app.route("/")
def index():
    msg = Message("All articles about TESLA from the last month",
                  sender="eglebabachinaite123@gmail.com",
                  recipients= ["eglebabachinaite123@gmail.com"])
    msg.body = data
    # msg.body = str(content)
    mail.send(msg)
    return "Message sent"

if __name__ == '__main__':
   app.run(debug=True)


