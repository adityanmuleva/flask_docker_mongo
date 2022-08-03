import get_userdata
from flask import Flask

app = Flask(__name__)


@app.route("/userdata")
def firstpage():
    res = get_userdata.get_user_data("Aaditya")
    print("==>", res)
    return str(res)

if __name__ == "__main__":
    app.run(debug=False)