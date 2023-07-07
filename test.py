'''import requests

print(requests.get("https://raw.githubusercontent.com/idummyuser/nlp/main/index.txt").text)'''

import urllib.request
urllib.request.urlretrieve("https://raw.githubusercontent.com/idummyuser/ml/main/4a_salary_data.csv", "4a_salary_data.csv")