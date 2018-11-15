import requests
my_domain = 'RafaelMonty.pythonanywhere.com'
username = 'RafaelMonty'
token = 'b1f6f6c24ddffb85d9fe45600ae626f4c05d520c'

response = requests.post(
  'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain}/reload/'.format(
      username=username, domain=my_domain
  ),
  headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
  print('All OK')
else:
  print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))
                        