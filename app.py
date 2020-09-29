from decimal import Decimal

from flask import Flask, make_response

from plan_service import PlanService
from sales_repository import SalesRepository

app = Flask(__name__)
sales_repository = SalesRepository()
plan_service = PlanService(sales_repository)


@app.route('/')
def index():
    return "Hello, It's IPay API!"


@app.route("/plan/product/<product_name>/price/<price>", methods=['GET'])
def predict_plan_product(product_name, price):
    price = float(price.replace(',', '.'))
    deal_response = plan_service.rate_deal(product_name, price)
    return make_response(deal_response, 200)


if __name__ == '__main__':
    app.run(debug=True)
