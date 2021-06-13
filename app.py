# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 21:13:27 2021

@author: vijay
"""


from flask import Flask,Request,request,jsonify
from scrape_linkedin import ProfileScraper

app = Flask(__name__)

@app.route('/index/')
def index():
    return "<h1>Heroku deployment</h1>"

def fetch_user_data(cokie,url):
    
    try: 
        with ProfileScraper(cookie=cokie) as scraper:
            profile = scraper.scrape(url=url)
            return profile.to_dict()
    except Exception as e:
       return e
        
    
@app.route('/user/',methods=['GET'])
def home():
    data = request.get_json()
    cokie = data['cookies']
    url = data['url']
    data = fetch_user_data(cokie, url)
    if type(data) is not dict:
        return data.msg
    else:
        return data

if __name__ == "__main__":
    app.run(debug=True)
