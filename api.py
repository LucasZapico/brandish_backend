from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api 
from flask_restful import reqparse
from get_site import  get_site_markup, tokenize, match_tokens, clean_copy
import json

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)

parser = reqparse.RequestParser()

tags_danish = ['JJ', 'NN', 'NNS', 'VBP', 'NNS', 'VB', 'NNS', 'VB', 'NNS', 'NN', 'NNP']



class HelloWorld(Resource):
  def get(self):
    return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

class Ipsum(Resource):
  
  @cross_origin(origin='*')
  def get(self):
    args = parser.parse_args()
    print('self', self)
    return "hello from get"

  @cross_origin(origin='*')
  def post(self):
    json_data = request.get_json()
    print(json_data)
    
    url = json_data['url'].strip()
    print('url', url)
    result = {
      "url": url,
    }

    # SiteSpider(CrawlSpider, url)
    copy = get_site_markup(url)
    clean = clean_copy(copy)
    tokenized = tokenize(clean)
    matches = match_tokens(tokenized, tags_danish)
    
    ipsum = ' '.join(matches)
    result["ipsum"] = ipsum

    
    return jsonify({result}), 200
    

api.add_resource(Ipsum, '/api/get-ipsum/')

if __name__ == '__main__':
  app.run(debug=True)

