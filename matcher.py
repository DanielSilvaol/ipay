from sales_repository import SalesRepository


class Matcher:

    def __init__(self, sales_repository):
        self._salesRepository = sales_repository
        self._companies = sales_repository.find_all_company()

    def match(self, search, dataset, rate_accept):
        match_accepted = []
        for data in dataset:
            if self._match(search, data, rate_accept):
                print('{matcher} ' + str(data))
                match_accepted.append(data)
            else:
                print(data)
        return match_accepted

    def _match(self, search, data, rate_accept):

        delta = 0
        value = data['name'].lower()
        delta += self._matcher_by_letter(search, self._prepare(value))
        delta += self._matcher_by_company(search, data) * 2
        delta += self._matcher_by_word(search, value) * 3
        delta += self._matcher_by_number(search, value) * 4

        perfect_delta = search.__len__() * 2 + \
                        data['company'].split(" ").__len__() * 2 + \
                        (search.split(" ").__len__() * 3) + \
                        (''.join([n for n in search if n.isdigit()]).__len__() * 4)
        error_bound = perfect_delta * 0.2

        ideal_delta = perfect_delta - error_bound
        return delta / ideal_delta > rate_accept

    @staticmethod
    def _matcher_by_letter(search, value):
        delta = 0
        try:
            for pos, letter in enumerate(search):
                if value.find(letter, pos - 1, pos + 1) != -1:
                    delta += 1
                if value.find(letter) != -1:
                    delta += 1
        except Exception as exc:
            print(f'matcher_by_letter {exc}')
        return delta

    @staticmethod
    def _matcher_by_word(search, value):
        delta = 0
        try:
            for word in value.split(' '):
                if search.lower().find(word.lower()) != -1:
                    delta += 1
        except Exception as exc:
            print(f"matcher_by_word {exc}")

        return delta

    @staticmethod
    def _matcher_by_number(search, value):
        delta = 0
        try:
            search_number = ''.join([n for n in search if n.isdigit()])
            value = ''.join([n for n in value if n.isdigit()])
            for letter in search_number:
                pos = value.find(letter)
                if pos != -1:
                    value = value[:pos] + value[pos+1:]
                    delta += 1
        except Exception as exc:
            print(f'matcher_by_number {exc}')
        return delta

    def _remove_company(self, value):
        for company in self._companies:
            value = value.lower().replace(company.lower(), '')
        return value

    @staticmethod
    def _prepare(value):
        return value.lower().strip().replace(' ', '')

    @staticmethod
    def _matcher_by_company(search, data):
        delta = 0
        for w in data['company'].split(" "):
            if w.find(search) != -1:
                delta += 1
        return delta


if __name__ == '__main__':

    search = "20gb"
    values = \
        [
         {"name": "13GB + Controle"},
         {"name": "20GB Pré Pago"},
         {"name": "8GB"},
         {"name": "11GB"}]

    print(Matcher(SalesRepository()).match(search, values, 0.7))
