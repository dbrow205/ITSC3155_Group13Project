import os
from flask import Flask

app = Flask(__name__)


app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True);
# To see the web page in your web browser, go to the url,
#   http://127.0.0.1:5000
