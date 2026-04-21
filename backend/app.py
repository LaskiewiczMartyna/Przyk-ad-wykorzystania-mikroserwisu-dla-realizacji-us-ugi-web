from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  
rates = {
    "PLN": 1.0,
    "USD": 3.6624,
    "EUR": 4.2369,
    "GBP": 4.8375
}

@app.route("/convert", methods=["GET"])
def convert():
    amount = float(request.args.get("amount", 0))
    from_currency = request.args.get("from", "PLN")
    to_currency = request.args.get("to", "USD")
    
    amount_in_pln = amount * rates[from_currency]
    converted = amount_in_pln / rates[to_currency]

    return jsonify({
        "from": from_currency,
        "to": to_currency,
        "amount": amount,
        "converted": round(converted, 2)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
