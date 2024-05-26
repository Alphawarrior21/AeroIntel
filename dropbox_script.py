import dropbox
import os

def download_files():
    # Define your access token
    ACCESS_TOKEN = 'sl.B15-H2CsWk4Xiio4qNbO2b_wnH3l0q7bv4OuumD4bbEm7rLBbXe2Y04man8aZaIo8SRAHGL7q_MS4_ZWs4xO5XSVk2ktsZAy4g2t5TgtUsqVtHoKDvCzJ69c8NSc0-OsuHyB413SxQTeOYRxh7kb'

    # Initialize Dropbox object
    dbx = dropbox.Dropbox(ACCESS_TOKEN)

    # Specify the Dropbox path and local folder path
    dropbox_path = '/RagBasedLLM'
    local_path = '/home/sumit/AeroIntel/Dropbox'

    # Create local folder if it doesn't exist
    if not os.path.exists(local_path):
        os.makedirs(local_path)

    # List files in the Dropbox folder
    for entry in dbx.files_list_folder(dropbox_path).entries:
        local_file_path = os.path.join(local_path, entry.name)
        # Check if the file already exists locally
        if not os.path.exists(local_file_path):
            # Download each file if it does not exist locally
            _, res = dbx.files_download(dropbox_path + '/' + entry.name)
            data = res.content

            # Write the downloaded file to the local folder
            with open(local_file_path, 'wb') as f:
                f.write(data)
            print(f"Downloaded: {entry.name}")
        else:
            print(f"Skipped (already exists): {entry.name}")

    print("File check and download completed!")