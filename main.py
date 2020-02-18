import json
import random

import falcon

from quotes import quotes


class QuoteResource:
    @staticmethod
    def on_get(req, resp):
        print('Request: ', req.method)
        quote = {
            'quote': random.choice(quotes),
            'author': 'Islam Mesha'
        }
        resp.body = json.dumps(quote)


api = falcon.API()
quote = QuoteResource()
api.add_route('/quote', quote)
