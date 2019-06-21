import requests
from django.conf import urls
from newsapi import NewsApiClient
import json
from django.http import HttpResponse, JsonResponse
def News():
    while  True:
            newsapi = NewsApiClient(api_key='7afe78e453a64e3ca55b795fdf8f0f04')

            agric_articles = newsapi.get_everything(q='agriculture',

                                                    # domains='bbc.co.uk,techcrunch.com',
                                                    from_param='2019-04-25',
                                                    to='2019-04-05',
                                                    # category = 'science, technology',
                                                    language='en',
                                                    )

            print(agric_articles)
            # print(agric_articles)
            json_status = agric_articles['status']
            if json_status == 'ok':
                 for article in agric_articles['articles'][:10]:
                     print(article)

                     return News()


