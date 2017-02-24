from sharepoint_api import get_list, load
from tallium_api import upload

sharepoint_library = 'lib_tallyfox' # Sample library name, replace by your own
library_files = []

def load_files(folder):
	load(folder)
	if folder.properties['Name'] != 'Forms': # Remove this condition if you want to download files from this folder
		files = folder.files
		set_library_files(files)
	
def set_library_files(files):
	load(files)
	for file in files:
		load(file)
		properties = file.properties
		file_name = properties['Name']
		server_relative_url = properties['ServerRelativeUrl']
		print 'Downloading {0}'.format(file_name)
        res = file.open_binary(ctx, server_relative_url)
        library_file = {'file': (file_name, res.content)}
        library_files.append(library_file)

def tallium_upload(file):
	res = upload(file)
	json = res.json()
	media_id = json['preview_job']['media_id']
	print 'Media ID: {0}'.format(media_id)

if __name__ == '__main__':
	list_obj = get_list(sharepoint_library) #A library in SharePoint is essentially a special list

	root_folder = list_obj.root_folder
	load_files(root_folder)

	folders = root_folder.folders
	load(folders)
	for folder in folders:
		load_files(folder)

	for file in library_files:
		tallium_upload(file)	

