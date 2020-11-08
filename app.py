from flask import Flask

# from plan_service import PlanService
# from sales_repository import SalesRepository

app = Flask(__name__)
# sales_repository = SalesRepository()
# plan_service = PlanService(sales_repository)


@app.route('/')
def index():
    return "Hello, It's IPay API!"


# @app.route("/plan/product/<product_name>/price/<price>", methods=['GET'])
# def predict_plan_product(product_name, price):
#     price = float(price.replace(',', '.'))
#     deal_response = plan_service.rate_deal(product_name, price)
#     return make_response(deal_response, 200)


# @app.route("/plan/companies", methods=['GET'])
# def search_companies():
    # companies = plan_service.search_companies()
    # response = json.dumps(companies)
    # return make_response(response, 200)


# @app.route("/plan/classification/<classification>/companies", methods=['GET'])
# def search_companies_by_classification(classification):
#     companies = plan_service.search_companies_by_classification(classification)
#     response = json.dumps(companies)
#     return make_response(response, 200)


if __name__ == '__main__':
    app.run(debug=True)
