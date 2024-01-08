from internetarchive import search_items, download, get_item
import time
import os

def download_with_retry(item_id, file_name, download_directory, max_retries=1):
    retries = 1
    file_path = os.path.join(download_directory, file_name)
    while retries < max_retries:
        if os.path.exists(file_path):
            print(f'File {file_name} already exists, skipping download.')
            return
        try:
            start_time = time.time()
            download(item_id, files=file_name, destdir=download_directory, timeout=15)
            end_time = time.time()

            # Estimate the download speed
            # Note: This is an estimate, the actual file size is not known
            avg_mp3_file_size_mb = 5  # average mp3 file size in MB
            download_time_seconds = end_time - start_time
            download_speed_mbps = avg_mp3_file_size_mb / download_time_seconds

            print(f'Downloaded file {file_name} at {download_speed_mbps:.2f} MB/s')
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