from flask import Flask
from flask_cors import CORS
from flask import render_template

app = Flask(__name__,
         static_folder="SDWebFrontEnd/dist/static",
         template_folder="SDWebFrontEnd/dist")
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/')
def render_vue():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(port=5000, debug=False)