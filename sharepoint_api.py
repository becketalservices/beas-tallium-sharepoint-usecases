from client.office365.runtime.auth.authentication_context import AuthenticationContext
from client.office365.sharepoint.client_context import ClientContext
from client.office365.runtime.client_request import ClientRequest
from client.office365.runtime.utilities.request_options import RequestOptions
from settings import sharepoint as settings

site_url = settings['site_url']
user = settings['username']
passwd = settings['password']

ctx_auth = AuthenticationContext(site_url)

def load(obj):
	ctx.load(obj)
	ctx.execute_query()

def acquire_token():
	return ctx_auth.acquire_token_for_user(user, passwd)

def get_context():
	return ClientContext(site_url, ctx_auth)

def get_file(file_relative_url):
	file = ctx.web.get_file_by_server_relative_url(file_relative_url)
	load(file)
	return file

#Any web part in SharePoint that holds content is a SharePoint list.
def get_list(title):
	list_obj = ctx.web.lists.get_by_title(title)
	load(list_obj)
	return list_obj

def direct_query(url):
	request = ClientRequest(ctx_auth)
	options = RequestOptions(url)
	options.set_header('Accept', 'application/json')
	options.set_header('Content-Type', 'application/json')
	return request.execute_query_direct(options)

def get_deferred_property_uri(obj, propertie_name):
	load(obj)
	return obj.properties[propertie_name]['__deferred']['uri']


ctx = get_context() if acquire_token() else False

if ctx == False:
	print 'Error on auth'