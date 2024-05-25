print("\nHello!\n")

import os
import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from concurrent.futures import ThreadPoolExecutor
import multiprocessing
import warnings
import urllib3
import logging


def setup_logging(log_file):
    """
    Set up logging configuration.
    """
    logging.basicConfig(filename=log_file, level=logging.ERROR, format='%(message)s', filemode='w')


def close_logging():
    """
    Close and remove all logging handlers.
    """
    for handler in logging.root.handlers[:]:
        handler.close()
        logging.root.removeHandler(handler)


def remove_empty_log_file(log_file):
    """
    Remove log file if it is empty.
    """
    if os.path.exists(log_file) and os.path.getsize(log_file) == 0:
        os.remove(log_file)


# Set up logging
current_directory = os.getcwd()
log_file = os.path.join(current_directory, 'ERROR.log')
if os.path.exists(log_file):
    os.remove(log_file)
setup_logging(log_file)

# Set up the session with retries
session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('https://', adapter)
session.verify = False

# Suppress SSL warnings
warnings.filterwarnings("ignore", category=urllib3.exceptions.InsecureRequestWarning)

# Read URLs from CSV
csv_file_path = 'URLs.csv'
df = pd.read_csv(csv_file_path, encoding='utf-8')

# Prompt user for download directory
default_download_dir = input("Please Enter Path: ")

# Ensure download directory exists
if not os.path.exists(default_download_dir):
    os.makedirs(default_download_dir)

# Initialize counter for successful downloads
successful_downloads = 0


def download_file(url, download_path):
    """
    Download a single file from the provided URL and save it to the specified path.
    """
    global successful_downloads
    try:
        response = session.get(url)
        response.raise_for_status()
        filename = url.split('/')[-1]
        file_path = os.path.join(download_path, filename)
        with open(file_path, 'wb') as file:
            file.write(response.content)
        successful_downloads += 1
        print(f"\r{successful_downloads} ", end=' ')
    except Exception as e:
        logging.error(f"Error downloading {url}: {e}")


def download_files(urls, download_path):
    """
    Download multiple files using threading.
    """
    with ThreadPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        # Submit all download tasks to the executor
        futures = [executor.submit(download_file, url, download_path) for url in urls]
        # Wait for all futures to complete
        for future in futures:
            future.result()


# Convert URLs from DataFrame and invoke download
urls = df['URL'].tolist()
download_files(urls, default_download_dir)

# Close logging and remove empty log file
close_logging()
remove_empty_log_file(log_file)
