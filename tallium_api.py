from settings import tallium as settings
import requests
import json

# Tallium settings
base_url = settings['base_url']
login_data = settings['login_data']

base_api = '{0}/api/'.format(base_url)
public_api = '{0}/public/api'.format(base_url)

login_api = '{0}/users/login.json'.format(public_api)
upload_api = '{0}/media.json'.format(base_api)
quickpost_api = '{0}/quickposts.json'.format(base_api)
document_api = '{0}/documents.json'.format(base_api)

# Login and get authorization token
auth_token = requests.post(login_api, data=login_data).json()['authorization']

headers = {
	'auth': 'Bearer {0}'.format(auth_token)
}

def upload(files):
	return requests.post(upload_api, headers=headers, files=files)

def quickpost(description):
	payload = {
		'description': description,
		'taxonomy': [],
		'media': [],
		'mentions': []
	}
	return requests.post(quickpost_api, headers=headers, data=json.dumps(payload))

def document(title = '', description = '', taxonomy = [], classifying = '', media = '', mentions = []):
	payload = {
		'title': title,
		'description': description,
		'taxonomy': taxonomy,
		'classifying': classifying,
		'media': media
		'mentions': mentions
	}
	return requests.post(document_api, headers=headers, data=json.dumps(payload))