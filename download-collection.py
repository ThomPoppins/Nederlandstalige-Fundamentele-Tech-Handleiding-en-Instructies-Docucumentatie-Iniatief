from internetarchive import search_items, download, get_item
import time


"""
Downloads a file with retry mechanism.

Args:
    item_id (str): The ID of the item to download.
    file_name (str): The name of the file to save the downloaded content.
    max_retries (int, optional): The maximum number of retries. Defaults to 5.

Returns:
    None

Raises:
    None
"""

def download_with_retry(item_id, file_name, max_retries=1):

    retries = 0
    while retries < max_retries:
        try:
            download(item_id, files=file_name, timeout=30)
            return
        except Exception as e:
            print(f'Error downloading file {file_name}: {e}, retrying...')
            retries += 1
            time.sleep(5)  # wait for 5 seconds before retrying

    print(f'Failed to download file {file_name} after {max_retries} retries.')

# Search for all items in the collection
search = search_items('collection:speedcoreworldwide')

# Get the total number of items
total_items = search.num_found
print(f'Total items: {total_items}')

# Iterate over the items
for index, item in enumerate(search, start=1):
    # Get the item
    item = get_item(item['identifier'])

    print(f'Downloading item {index} of {total_items}: {item.identifier}')

    # Iterate over the files in the item
    for file in item.files:
        # Check if the file is an mp3
        if file['name'].endswith('.mp3'):
            print(f'Downloading file: {file["name"]}')
            # Download the file with retry
            download_with_retry(item.identifier, file['name'])