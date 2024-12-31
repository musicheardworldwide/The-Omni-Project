from flask import Flask

app = Flask()

@app.route('/')
def home():
    return "Welcome to The Omni Project!"

if __name__ == '__main__':
    app.run(debug=True)