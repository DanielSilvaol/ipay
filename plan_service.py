from matcher import Matcher


class PlanService:

    _DELTA = 0.6
    _OUTLIER = 50

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

    def __rate_better_than(self, deals_by_name, price):

        if len(deals_by_name) == 0:
            return {"price_rate": price}

        company_better = ""
        min_price = price
        average_price = self._avg(list(map(lambda deal: float(deal['price'].replace(',', '.')), deals_by_name)))

        for deal in deals_by_name:
            deal_price = float(deal['price'].replace(',', '.'))
            if deal_price < min_price and self._is_not_an_outlier(average_price, deal_price):
                min_price = deal_price
                company_better = deal['company']

        perc_deal_rate = self._calc_perc_rate(price, min_price)
        return {"price_rate": perc_deal_rate, "company": company_better}

    @staticmethod
    def _calc_perc_rate(price, min_price):
        return round((price/min_price-1)*100, 2)

    def _is_not_an_outlier(self, average_price, price):
        rate = abs(self._calc_perc_rate(average_price, price))
        return rate < self._OUTLIER

    @staticmethod
    def _avg(list):
        return sum(list) / len(list)

    def search_companies(self):
        companies = self.__sales_repository.find_all_company()
        return companies

    def search_companies_by_classification(self, classification):
        plans_by_classification = self.__sales_repository.find_plans_by_classification(classification)
        return list(dict.fromkeys(map(lambda plan: plan['company'], plans_by_classification)))


