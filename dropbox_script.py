import dropbox
import os

def download_files():
    # Define your access token
    ACCESS_TOKEN = 'sl.B1nX501NKRjohwMJmE04PeAFhu7KP3Q2AaI1_BevZVVKYjaDOwUyTXrS-CYtVQMSMddMP5XWOFA7nyCetCIprRMHlgvu9sKD3ROPONQmwjs1AUNp2ww7I63l_N1zzvw-nxaTRPLq1LMUtqm4-yo7EOQ'

    # Initialize Dropbox object
    dbx = dropbox.Dropbox(ACCESS_TOKEN)

    # Specify the Dropbox path and local folder path
    dropbox_path = '/RagBasedLLM'
    local_path = '/home/sumit/gate_cse_gpt/Dropbox'

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
