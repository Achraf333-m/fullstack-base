from flask import Flask

app = Flask(__name__)

#values API route

@app.route("/values")
def values():
    return {
        "values": [
            "value__1",
            "value__2",
            "value__3",
            "value__4",
        ]
    }

if __name__=="__main__":
    app.run(debug=True)
