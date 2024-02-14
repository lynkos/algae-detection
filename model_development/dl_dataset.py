from concurrent.futures import ProcessPoolExecutor
from os import getcwd, path
from glob import glob
from requests import get, exceptions, Response
from time import perf_counter

FILEPATH = path.join(getcwd(), "dataset")
"""Path to dataset folder"""

TEXT_FILES = glob(path.join(FILEPATH, "*.txt"))
"""List of all text files in `FILEPATH`" containing URLs of images to download"""

TIMEOUT: int = 10
"""Number of seconds till request times out"""

def connect(url: str) -> Response | None:
    """
    Connect to URL

    Args:
        url (str): URL to connect to
        
    Returns:
        Response | None: HTTP request response if applicable, else None
    """    
    try:
        return get(url, allow_redirects = True, stream = True, timeout = TIMEOUT)

    except exceptions.ConnectTimeout:
        print(f"Request to {url} timed out after {TIMEOUT} seconds")

    except exceptions.ReadTimeout:
        print(f"{url} failed to send data within {TIMEOUT} seconds")

    except exceptions.TooManyRedirects:
        print(f"{url} has too many redirects")

    except (exceptions.URLRequired, exceptions.InvalidURL):
        print(f"{url} is not a valid URL")

    except exceptions.HTTPError:
        print(f"HTTP error while connecting to {url}")

    except exceptions.SSLError:
        print(f"SSL error while connecting to {url}")

    except exceptions.ProxyError:
        print(f"Proxy error while connecting to {url}")

    except exceptions.ConnectionError:
        print(f"Connection error while connecting to {url}")

    except exceptions.RequestException:
        print(f"Unable to handle request to {url}")

    except Exception as error:
        print(f"Unexpected error while connecting to {url} ({error})")

def download(file_url: str, new_filepath: str) -> None:
    """
    Download image from URL

    Args:
        file_url (str): URL of file to download
        new_filepath (str): Absolute path to save file to
    """
    response = connect(file_url)
    
    if response and response.status_code == 200:         
        try:
            with open(new_filepath, "wb") as file:
                file.write(response.content)

        except ChildProcessError:
            print(f"Child process error while downloading {file_url}\n")

        except InterruptedError:
            print(f"Interrupted while downloading {file_url}\n")

        except ProcessLookupError:
            print(f"Process lookup error while downloading {file_url}\n")

        except MemoryError:
            print(f"Memory error while downloading {file_url}\n")

        except TimeoutError:
            print(f"Timeout error while downloading {file_url}\n")

        except PermissionError:
            print(f"Permission error while downloading {file_url}\n")

        except (IOError, OSError):
            print(f"I/O error while downloading {file_url}\n")

        except Exception as error:
            print(f"Unexpected error while downloading {file_url} ({error})\n")

    else:
        print(f"Failed to connect to {file_url}\n")

def download_images(filepath: str, folder: str) -> None:
    """
    Download images from URLs in text file

    Args:
        filepath (str): Absolute path to text file containing URLs of images to download
        folder (str): Folder to download images to
    """
    counter = 0
    
    with open(filepath) as file:
        for line in file:
            line = line.split()
            
            if line[1] == "StillImage" and line[2] == ("image/jpeg" or "image/png"):
                extension = line[2].removeprefix("image/")
                download(line[3], path.join(FILEPATH, folder, f"{folder}{counter}.{extension}"))
                counter += 1

def work() -> None:
    """
    Download all images(s)
    """
    for filepath in TEXT_FILES:
        filename = path.basename(filepath)
        
        with ProcessPoolExecutor() as executor:
            executor.submit(download_images, filepath, filename[:filename.index("_")])
        print("Finished downloading one batch of images\n")

if __name__ == "__main__":
    print("Starting script...\n")
    start = perf_counter()

    work()

    end = perf_counter()
    print(f"Total runtime: {(end - start):.2f} second(s)")