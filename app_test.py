from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def dummy_api():
  return jsonify(data="hello from api")

if __name__ == '__main__':
  app.run(debug=True, port=5000)