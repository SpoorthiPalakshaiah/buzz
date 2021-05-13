"""Create python flask wrapper around our buzz generator"""
import os
from flask import Flask
import generator


app = Flask(__name__)


@app.route("/")
def generate_buzz():
    """generate flask wrapper"""
    page = '<html><body style="background-color:#7be1e8"><center><h1 style="font-family:cursive">'
    page += generator.generate_buzz()
    page += '</center></h1></body></html>'
    return page


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
