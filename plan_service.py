
class PlanService:

    def __init__(self, sales_repository):
        self.__sales_repository = sales_repository

    def rate_deal(self, product_name, price):

        deals_by_name = self.__match_products(product_name)
        deal = self.__rate_better_than(deals_by_name, price)
        return deal

    def __match_products(self, product_name):
        # TODO criar metodo de match de palavra aqui ao invez de buscar a base toda
        return self.__sales_repository.find_all()

    def __rate_better_than(self, deals_by_name, price):
        min_price = float(deals_by_name[0]['price'].replace(',', '.'))
        company_better = ""

        for deal in deals_by_name:
            deal_price = float(deal['price'].replace(',', '.'))

            if deal_price < min_price:
                min_price = deal_price
                company_better = deal['company']

        perc_deal_rate = round((price/min_price-1)*100, 2)
        return {"price_rate": perc_deal_rate, "company": company_better}

    def __avg(self, list):
        return sum(list) / len(list)

#average_price = self.__avg(list(map(lambda deal: Decimal(deal['price'].replace(',', '.')), deals_by_name)))
        #deal_price = Decimal(deal['price'].replace(',', '.'))
        #average_price = round((deal_price/price-1)*-100, 2)
        #company_name = deal['company']