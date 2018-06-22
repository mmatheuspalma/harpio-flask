from flask import Flask, request, jsonify
from flask_cors import CORS

from comic import Comic
from comic_params import ComicParams

from model_comics import ComicsModel

app = Flask(__name__)
CORS(app)

comics = ComicsModel()

@app.route('/comics', methods=['GET'])
def getComics():
    comicParams = ComicParams(request.args.get('order'), request.args.get('orderBy'), request.args.get('search'))   

    return jsonify(comics.getComics(comicParams))

@app.route('/comics/<int:comic_id>', methods=['GET'])
def getComic(comic_id):
    return jsonify(comics.getComic(comic_id))

@app.route('/comics/new', methods=['POST'])
def createComic():
    comic = Comic(request.form.get('name'), request.form.get('description'), request.form.get('thumbnail'))

    return jsonify(comics.createComic(comic=comic))

@app.route('/comics/edit/<int:comic_id>', methods=['PUT'])
def editComic(comic_id):
    comic = Comic(request.form.get('name'), request.form.get('description'), request.form.get('thumbnail'))

    return jsonify(comics.editComic(comic_id, comic=comic))

@app.route('/comics/remove/<int:comic_id>', methods=['DELETE'])
def removeComic(comic_id):
    return jsonify(comics.removeComic(comic_id))
    
if __name__ == '__main__':
    app.run(debug=True)