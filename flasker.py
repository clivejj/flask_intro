from flask import Flask

app = Flask(__name__)


@app.route("/")
def hey():
    print "test"
    return "Home Page"

@app.route("/Sub")
def hey1():
    return "Subby the elephant"

@app.route("/SubSub")
def hey2():
    return "Subby the bigger elephant"

if __name__ == "__main__":
    app.debug = True
    app.run()

    
