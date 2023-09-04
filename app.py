import os, random

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)

arr1 = ["Logic will get you from A to B. Imagination will take you everywhere.",
        "There are 10 kinds of people. Those who know binary and those who don't.",
        "There are two ways of constructing a software design. One way is to make it so simple that there are obviously no deficiencies and the other is to make it so complicated that there are no obvious deficiencies.",
        "It's not that I'm so smart, it's just that I stay with problems longer.",
        "It is pitch dark. You are likely to be eaten by a grue."]
        
   
@app.route('/')
def index():
   randomindex1 = random.randint(0,4)
   randomstring1 = arr1[randomindex1]
   print('Request for index page received [%s]' % randomindex1)
   return render_template('index.html', randomstring = randomstring1)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/sanrio.icon')

if __name__ == '__main__':
   app.run()
