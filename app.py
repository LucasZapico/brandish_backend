from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from helpers import  get_site_markup, tokenize, match_tokens, clean_copy, make_para

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

tags_danish = ['JJ', 'NN', 'NNS', 'VBP', 'NNS', 'VB', 'NNS', 'VB', 'NNS', 'NN', 'NNP']


@app.route('/', methods=["GET"])
@cross_origin('*')
def hello_world():
    return "Hello World"

@app.route('/api/')
@cross_origin('*')
def hello_api():
    return jsonify({"hello": "hello from deta brandish api endpoint"})

@app.errorhandler(404)
def page_not_found(e):
  return jsonify({404: 'the page you are looking for does not exist'})


@app.route('/make-ipsum/')
@cross_origin('*')
def make_ipsum():
  try: 
    url = request.args.get('url')
    para_size = request.args.get('para-size')
    number_para = request.args.get('number-para')
    print('pra', para_size)
    print('num', number_para)
    result = {
      "url": url,
    }
    # return 'Query string example'
    url = url.strip()
    print('url', url)

    # SiteSpider(CrawlSpider, url)
    copy = get_site_markup(url)
    clean = clean_copy(copy)
    tokenized = tokenize(clean)
    matches = match_tokens(tokenized, tags_danish)
    
    ipsum = ' '.join(matches)
    para_ipsum = make_para(ipsum, para_size, number_para)
    result["ipsum"] = para_ipsum

    
    return jsonify(data=result), 200
  except: 
    return jsonify(error={"message": 'Ooof some of these fancy site block our bot'}), 403

if __name__ == '__main__':
  app.run(debug=True, port=5000)






