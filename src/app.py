# Stock Price Tracker App
# *-* coding:utf-8 *-*

import yfinance as yf

from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template

# app
app = Flask(__name__)
app.template_folder = 'template'
app.static_folder = 'static'
app.secret_key = 'SECRET_KEY'


# router
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_stock_data', methods=['POST'])
def get_stock_data():
    ticker = request.get_json()['ticker']
    data = yf.Ticker(ticker).history(period='1y')
    return jsonify({'currentPrice': data.iloc[-1].Close,
                    'openPrice': data.iloc[-1].Open})


# run app
if __name__ == '__main__':
    app.run(debug=True)