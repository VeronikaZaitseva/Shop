from django.conf import settings
from shop.models import Tea
from decimal import Decimal


class Basket():
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if not basket:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket

    def add(self, product, count=1, update_count=False):
        product_id = str(product.id)
        if product_id not in self.basket:
            self.basket[product_id] = {'count': 0,
                                       'price': str(product.price)}

        if update_count:
            self.basket[product_id]['count'] = count
        else:
            self.basket[product_id]['count'] += count
        self.save()

    def save(self):
        self.session[settings.BASKET_SESSION_ID] = self.basket
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.basket.keys()
        products = Tea.objects.filter(id__in=product_ids)

        for product in products:
            self.basket[str(product.id)]['product'] = product

        for item in self.basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['count'] * item['price']
            yield item

    def __len__(self):
        res = sum(x['count'] for x in self.basket.values())
        return res

    def get_total_price(self):
        res = sum(Decimal(x['count']) * Decimal(x['price']) for x in self.basket.values())
        return res

    def clear(self):
        del self.session[settings.BASKET_SESSION_ID]
        self.session.modified = True


def basket(request):
    return {'basket': Basket(request)}
