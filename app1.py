from flask import Flask, redirect, url_for, render_template, request
import tweepy
from keys import *

# Authenticate to Twitter

auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(akey,asecret)

api = tweepy.API(auth)


def postweets(city,resources):
    return tweepy.Cursor(api.search,q='"'+city+'"'+' '+'"'+resources+'" "'+ 'verified'+'"'+'-"not verified" -"unverified" -"needed" -"need" -"needs" -"required" -"require" -"requires" -"requirement" -"requirements"').items(50)



app= Flask(__name__)

@app.route("/")
def home():
    return render_template("ct.html")
#@app.route("/test")
#def test():
#    return render_template("index.html")


@app.route("/test",methods=["POST","GET"])
def test():
    if request.method=="POST":
        cityname=request.form["city"]
        resourcename=request.form["resource"]

        tweets=postweets(cityname,resourcename)

        text=[]
        time=[]

        for tweet in tweets:
            text.append(tweet.text)
            time.append(tweet.created_at)


        return render_template("output.html",text=text,time=time,tweet=tweets)

    else:
        return render_template("input.html")


if __name__=="__main__":
    app.run()

# if __name__=='__main__':
 #   app.run(debug=True)