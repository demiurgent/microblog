from newsapi import NewsApiClient

# Init/Users/micky/Documents/madpaws/ta/new_app_app/cypress/cypress/integration/mobile-ionic/browserTests/test.js
newsapi = NewsApiClient(api_key='0a9d300e652e44d88bd252ab440503da')


# /v2/top-headlines

top_headlines = newsapi.get_top_headlines(q='coronavirus',
                                          sources='business-insider',
                                          # category='business',
                                          language='en',
                                          # country='us'
                                          )
# print(top_headlines)

"""
# /v2/everything

all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2020-05-01',
                                      to='2020-05-05',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# /v2/sources
sources = newsapi.get_sources()

"""