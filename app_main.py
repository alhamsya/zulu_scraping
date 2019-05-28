from flask import Flask, jsonify, request
from app.scraping import scrape, youtube


app = Flask(__name__)

ACARA = 'the_east'

@app.route('/')
def index():
    list_program = {
        'the_east': "7-7/the-east-season-1",
        "tonight_show": "17-17/tonight-show-season-1"
    }
    result = scrape(request, list_program.get(ACARA))
    return jsonify(result)


@app.route('/youtube/<path:subpath>')
def link(subpath):

    result = {
        "link_youtube": youtube(subpath)
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='192.168.0.101', port=5000)
