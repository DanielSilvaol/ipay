from matcher import Matcher


class PlanService:

    _DELTA = 0.7
    _OUTLIER = 50
    _MAX_INTEGER = 2 ** 32

    def __init__(self, sales_repository):
        self.__sales_repository = sales_repository
        self.__matcher = Matcher(sales_repository)

    def rate_deal(self, product_name, price):
        try:
            deals_by_name = self.__match_products(product_name)
            deal = self.__rate_better_than(deals_by_name, price)
        except Exception as exc:
            print(f'rate_deal {exc}')
            deal = {"price_rate": price}
        return deal

    def __match_products(self, product_name):
        return self.__matcher.match(product_name,
                                    self.__sales_repository.find_all(),
                                    self._DELTA)

    def rate_deal_by_classification(self, classification, product_name, price):
        try:
            deals_by_name = self.__match_products_by_classification(classification, product_name)
            deal = self.__rate_better_than(deals_by_name, price)
        except Exception as exc:
            print(f'rate_deal {exc}')
            deal = {"price_rate": price}
        return deal

    def __match_products_by_classification(self, classification, product_name):
        return self.__matcher.match(product_name,
                                    self.__sales_repository.find_all_by_classification(classification),
                                    self._DELTA)

    def __rate_better_than(self, deals_by_name, price):

        if len(deals_by_name) == 0:
            return {"price_rate": 0}

        company_better = ""
        min_price = self._MAX_INTEGER
        average_price = self._avg(list(map(lambda deal: deal['price'], deals_by_name)))

        for deal in deals_by_name:
            deal_price = deal['price']
            if deal_price < min_price and self._is_not_an_outlier(average_price, deal_price):
                min_price = deal_price
                company_better = deal['company']

        perc_deal_rate = self._calc_perc_rate(price, min_price)

        if company_better == "":
            return {"price_rate": perc_deal_rate}

        return {"price_rate": perc_deal_rate, "company": company_better}

    @staticmethod
    def _calc_perc_rate(price, min_price):
        if min_price == 0:
            return 0
        return round((price/min_price-1)*100, 2)

    def _is_not_an_outlier(self, average_price, price):
        rate = abs(self._calc_perc_rate(average_price, price))
        return rate < self._OUTLIER

    @staticmethod
    def _avg(list):
        if len(list) == 0:
            return 0
        return sum(list) / len(list)

    def search_companies(self):
        companies = self.__sales_repository.find_all_company()
        return companies

    def search_companies_by_classification(self, classification):
        plans_by_classification = self.__sales_repository.find_plans_by_classification(classification)
        return list(dict.fromkeys(map(lambda plan: plan['company'], plans_by_classification)))


