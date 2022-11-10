from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def get_hello():
    return "hello world"


@app.route('/', methods=["POST"])
def post_hello():
    person = request.get_json()
    print(person)

    return person["name"]


@app.get('/json')
def get_json():
    friends = [
        {"name": "Jack"},
        {"name": "Amy"}
    ]

    return jsonify(friends)


if __name__ == "__main__":
    app.run(debug=True)
