import requests

'''
the api parameters can be referenced at the following url:
https://opentdb.com/api_config.php
'''

api_url = 'https://opentdb.com/api.php'
api_parameter = {
    'amount': 10,
    'type': 'boolean'
}


question_data = requests.get(api_url, params=api_parameter).json()['results']

print(question_data[0])
