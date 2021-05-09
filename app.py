from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///table.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Table(db.Model):

    Daytime=db.Column(db.DateTime, default=datetime.utcnow , primary_key=True)
    Spo2=db.Column(db.Integer)
    Pulse=db.Column(db.Integer)
    Temp=db.Column(db.Integer)

    def __repr__(self) -> str:
        return f"{self.Daytime}-{self.Spo2}-{self.Pulse}-{self.Temp}"

@app.route('/',methods=['GET','POST'])
def tablee():

    if request.method=='POST':
        Spo2=request.form["Spo2"]
        Pulse=request.form["Pulse"]
        Temp=request.form["Temp"]

        table=Table(Spo2=Spo2,Pulse=Pulse,Temp=Temp)
        db.session.add(table)
        db.session.commit(table)

    table=Table
    alltable=table.query.all()
    print(type(alltable))
    return render_template("table.html",alltable=alltable)


if __name__=="__main__":
    app.run()
#headings=("Day", "Time","Spo2","Pulse","Temperature")
#users=[]
#data=[[[]]]

#@app.route('/',methods=["POST","GET"])
#def user():

 #   if request.method=="POST":
  #      username=request.form["person"]
   #     if(username in data==1):
    #        return render_template("table.html", data=data[username],)
     #       tabledata=request.form["tabledata"]



    #else:
     #   return render_template("login.html")


#@app.route('/')
#def table():
 #   return render_template("table.html",headings=headings, data=data)

  #  for row in data:

   #     for cell in row:
      #      r=request.form["da"]