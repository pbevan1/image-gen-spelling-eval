from datasets import load_dataset
from huggingface_hub import login
import requests
import os
from urllib.parse import urlparse
from tqdm import tqdm


def download_image(url, directory):
    """Function to download an image and save it to a specified directory"""
    try:
        filename = os.path.basename(urlparse(url).path)
        save_path = os.path.join(directory, filename)

        if os.path.exists(save_path):
            return filename

        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        with open(save_path, 'wb') as image_file:
            image_file.write(response.content)
        return filename
    except requests.RequestException as e:
        print(f"Failed to download {url}. Reason: {e}")
        return None


def create_caption_file(root_name, caption, directory):
    """Function to create a text file for the caption with the same root name as the image"""
    caption_filename = f"{root_name}.short_caption"
    caption_path = os.path.join(directory, caption_filename)
    with open(caption_path, 'w') as caption_file:
        caption_file.write(caption)


def main(download_directory, hf_dataset):
    """"""
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)

    dataset = load_dataset(hf_dataset)

    for item in tqdm(dataset['train']):  # Adjust the split name if necessary
        url, caption = item['url'], item['caption']
        filename = download_image(url, download_directory)
        if filename:
            root_name = os.path.splitext(filename)[0]
            create_caption_file(root_name, caption, download_directory)


if __name__ == '__main__':
    with open('hf.env', 'r') as hf_env:
        for line in hf_env:
            hf_key = line
        print(hf_key)
        print(f"Read key from hf.env")
        login(token=hf_key)
    hf_dataset="pbevan11/GPT4V-captions-from-LVIS-typography"
    download_directory = f'training_data/{hf_dataset}'
    main(download_directory, hf_dataset)
