from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Velasco, Josaiah D. BSIT III-B"

if __name__ == '__main__':
    app.run(debug=True)