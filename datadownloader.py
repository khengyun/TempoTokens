import gdown
import zipfile
import os

def download_and_unzip(url, output_dir):
    """
    Downloads a file from Google Drive and extracts it if it's a zip file.

    Args:
        url (str): The Google Drive URL of the file.
        output_dir (str): The directory to save and extract the file.
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Extract the file ID from the URL
    file_id = url.split('/d/')[1].split('/view')[0]
    download_url = f"https://drive.google.com/uc?id={file_id}"

    # Define the output file path
    output_file = os.path.join(output_dir, "dataset.zip")

    print("Downloading dataset...")
    gdown.download(download_url, output_file, quiet=False)

    # Check if the downloaded file is a zip file and extract it
    if zipfile.is_zipfile(output_file):
        print("Extracting dataset...")
        with zipfile.ZipFile(output_file, 'r') as zip_ref:
            zip_ref.extractall(output_dir)
        print("Extraction complete.")
    else:
        print("Downloaded file is not a zip file.")

    # Optionally, delete the zip file after extraction
    os.remove(output_file)

# Example usage
url = "https://drive.google.com/file/d/1Wo0jiKYtxXs1Tl_SJACBbxniDDKeTGc4/view?usp=sharing"
output_dir = "./datasets"
download_and_unzip(url, output_dir)
