from flask import Flask, request, jsonify
from aternos import Aternos

app = Flask(__name__)

# Example password-to-server mapping
server_mapping = {
    "7274": "ansh779.aternos.me",
    "5536": "other.server.ip"
}


app.run(host="0.0.0.0", port=8080)


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    try:
        # Authenticate user using Aternos API
        aternos = Aternos(username, password)
        aternos.login()  # Attempt login

        if password in server_mapping:
            return jsonify({"success": True, "server_ip": server_mapping[password]})
        else:
            return jsonify({"success": False, "error": "Invalid password!"})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
