# Multiple URL Downloader

This script downloads files from a list of URLs provided in a CSV file. It uses multithreading to speed up the download process and handles retries for failed requests.

## Features
- Downloads files from URLs listed in a CSV file.
- Supports multithreading to speed up downloads.
- Handles retries for failed requests.
- Logs errors to a file.

## Requirements
- Python 3.x
- `pandas==2.1.1`
- `requests==2.31.0`
- `urllib3==2.2.1`

## Installation
1. **Clone the repository:**
    ```sh
    git clone https://github.com/mofasuhu/multiple-url-downloader.git
    ```

2. **Navigate to the project directory:**
    ```sh
    cd multiple-url-downloader
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. **Prepare your CSV file:**
   Ensure that your CSV file (e.g., `URLs.csv`) contains a column named `URL` with the URLs of the files to be downloaded.

2. **Run the script:**
    ```sh
    python multiple_download_urls.py
    ```

3. **Follow the prompts:**
   - Enter the path to the directory where you want to save the downloaded files.

### Example
Here's an example of how to run the script:
```sh
python multiple_download_urls.py
```

You will be prompted to enter the download directory:
```sh
Please Enter Path: /path/to/download/directory
```

## File Structure
- **multiple_download_urls.py:** The main script for downloading files from URLs.
- **URLs.csv:** A sample CSV file containing URLs for testing.
- **LICENSE:** The MIT license file for the project.
- **README.md:** This detailed readme file.
- **requirements.txt:** The dependencies required to run the script.

## Contributing
If you have suggestions for improving this project, feel free to open an issue or create a pull request. Contributions are welcome!

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any inquiries or issues, please contact the project owner at [mofasuhu@gmail.com](mailto:mofasuhu@gmail.com).
