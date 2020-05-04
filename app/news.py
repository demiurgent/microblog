# https://rapidapi.com/mikilior1/api/FinancialTimes
# https://rapidapi.com/blog/rapidapi-featured-news-apis/?utm_source=google&utm_medium=cpc&utm_campaign=Beta_101089624300&utm_term=%2Bnews%20%2Bfree%20%2Bapi_b&utm_content=&gclid=EAIaIQobChMIoLKN866a6QIVyqiaCh0T1Q1eEAAYASAAEgL3fPD_BwE

import requests

url = "https://guardianmikilior1v1.p.rapidapi.com/getTags"

payload = ""
headers = {
    'x-rapidapi-host': "Guardianmikilior1V1.p.rapidapi.com",
    'x-rapidapi-key': "948363e921msh034582e12f546efp13f70fjsnf5b4f9880dfd",
    'content-type': "application/x-www-form-urlencoded"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)