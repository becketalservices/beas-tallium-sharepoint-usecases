from sharepoint_api import get_file
from tallium_api import quickpost

file_relative_url = '/python/lib_tallyfox/doc1.docx' # Sample

if __name__ == '__main__':
	file = get_file(file_relative_url)
	file_url = file.properties['LinkingUrl'];
	description = 'Look at this awesome document: <a href="{0}">{0}</a>'.format(file_url);
	res = quickpost(description=description)
	print res
