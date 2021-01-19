from flask import Response
from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from datetime import datetime

app = FlaskAPI(__name__)

@app.route('/', methods=['POST'])
def processPayment():
    
    creditCardNumber = request.data.get('creditCardNumber')
    if creditCardNumber == '' :
        return {
            "Response": 'Credit card number cant be blank'
        }
    if type(creditCardNumber) != str:
        return {
            "Response": 'Credit card number cant be string'
        }
    cardHolder = request.data.get('cardHolder')
    if cardHolder == '' :
        return {
            "Response": 'Card holder cant be blank'
        }
    if type(cardHolder) != str:
        return {
            "Response": 'Card holder cant be string'
        }

    expirationDate = request.data.get('expirationDate')
    curr_date = datetime.now()
    exp_date = datetime.strptime(expirationDate, "%Y-%m-%d")
    # print("curr_date", curr_date)
    # print('exp_date', exp_date)

    if exp_date < curr_date:
        return {
            "Response": 'Expiration date is in past'
        }

    securityCode = request.data.get('securityCode')
    if len(securityCode) != 3:
        return {
            "Response": 'Security code needs to be of 3 digits'
        }
    amount = request.data.get('amount')
    if isinstance(amount, float) and amount > 0:
        pass
    else:
        return {
            "Response": 'Amount should be in decimals and greater than zero'
        }

    return {
        "Response": 'Ok',
        "amount": amount
    }

app.run()
