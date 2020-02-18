import json
import random

import falcon

from quotes import quotes, authors


class QuoteResource:
    @staticmethod
    def on_get(req, resp):
        print('Request: ', req.method)
        quote = {
            'quote': random.choice(quotes),
            'author': random.choice(authors)
        }
        resp.body = json.dumps(quote)


api = falcon.API()
quote = QuoteResource()
api.add_route('/quote', quote)
