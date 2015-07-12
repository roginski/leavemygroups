#!/usr/bin/env python
import requests

access_token = '041cfc0c19e18a9803066a3d1fa0bee4f45d19e87aa3658c88522a06d495433400f229dbe2226d6f1327d'
user_id = '1801158'
app_id = 4989700

def login(email, password):
  r = session.get('http://vk.com/login.php', params={'email': email, 'pass': password})
  r.raise_for_status()

def auth(user_id):
  #url = 'https://oauth.vk.com/authorize?client_id=4989700&scope=groups&redirect_uri=https://oauth.vk.com/blank.html&display=popup&v=5.34&response_type=token'
  r = session.get(
    'https://oauth.vk.com/authorize', 
    params={
      'client_id': app_id, 
      'scope': 'groups',
      'redirect_uri': 'https://oauth.vk.com/blank.html',
      'display': 'popup',
      'v': '5.34',
      'response_type': 'token'})
  print r.text
  
def get_groups():
  url = 'https://api.vk.com/method/groups.get?user_id=%s&access_token=%s&v=5.34' % (user_id, access_token)
  r = requests.get(url)
  r.raise_for_status()
  return r.json()['response']['items']
  
def leave_group(group_id):
  url = 'https://api.vk.com/method/groups.leave?group_id=%s&user_id=%s&access_token=%s&v=5.34' % (group_id, user_id, access_token)
  r = requests.get(url)
  r.raise_for_status()

def leave_groups():
  groups = get_groups()
  print len(groups), 'groups found, leaving!'
  for gr in groups:
    leave_group(gr)
    print 'Left group', gr

session = requests.Session()
login('eugene.roginsky@gmail.com', 'drjynfrntujdyj')
auth(user_id)
