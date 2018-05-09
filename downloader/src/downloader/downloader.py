from multiprocessing.pool import ThreadPool
import os
import urllib.request
from io import BytesIO
import time

from PIL import Image


def get_size(size_str: str)-> tuple:
    """
    This function creates from size_str ordinary size in int
    Example:
    100x100 -> (100, 100)
    :param size_str: string size
    :return: tuple with size of picture
    """
    if not isinstance(size_str,str):
        raise TypeError('size should be a str with this format 100x100')
    try:
        size_tuple = tuple(int(size)for size in size_str.split('x'))
    except ValueError as e:
        print(f'This error raising {e}')
        return
    return size_tuple


def get_url(path: str)->tuple:

    """
    This function getting urls from file with urls

    :param path: path to the file where lives urls
    :return: tuple with all urls
    """
    if not isinstance(path, str):
        raise TypeError('Path should be a string')
    if not os.path.exists(path):
        raise ValueError('This path do not exist')
    with open(path, 'r') as urls:
        return tuple(urls.readlines())


def load_image(url: str)-> bytes:
    """
    This function opens URL and reads it

    :param url:
    :return:
    """
    if not isinstance(url, str):
        raise TypeError('Url should be str')
    with urllib.request.urlopen(url) as response:
        response = response.read()
    return response


def target_dir_maker(number: int, target_dir: str, len_urls: int)-> str:
    """
    This function creates path to target dir
    :param number: number of url
    :param target_dir: path to target dir
    :param len_urls: quantity of urls
    :return: str with target dir
    """

    name = str(number).rjust(len(str(len_urls)) - len(str(number)), '0')
    return os.path.join(target_dir, name + '.jpeg')


def download_url(download_option: dict)-> tuple:
    """
    This function download image using url and report about process

    :param download_option: option for download images
    :return: tuple with three parameters: Success rate, Error text and quantity of bytes
    """
    error_text = f'In this url line with number {download_option["number"]} problem'
    try:
        download_file = load_image(download_option['url'])
    except (TypeError, urllib.request.HTTPError, urllib.request.URLError, urllib.request.ssl.CertificateError):
        print(error_text)

        return tuple((False, error_text, 0))
    try:
        image = Image.open(BytesIO(download_file))
        image = image.convert('RGB')
        image.thumbnail(download_option['size'], Image.ANTIALIAS)
        image.save(download_option['target_dir'], 'jpeg')
    except IOError:
        print(error_text)
        return tuple((False, error_text, len(download_file)))
    print(f'Image with number {download_option["number"]} download normally')
    return tuple((True, 'OK', len(download_file)))


def printer(download_results: tuple, msgs: tuple, length_bytes: tuple, runtime: float)-> None:
    """
    This function prints report about downloading

    :param download_results: results of downloading
    :param msgs: messages about error or success
    :param length_bytes: quantity of bytes which you're downloaded
    :param runtime: runtime of downloading
    :return: None
    """
    print('Downloading images finally over')
    oks = sum(download_results)
    not_oks = len(download_results) - oks
    quantity_bytes = sum(length_bytes)
    print('Statistics')
    print(f'Successfully downloaded files: {oks}')
    print(f'Files with errors {not_oks}')
    print(f'Quantity of bytes downloaded: {quantity_bytes}')
    print(f'Runtime of the process: {runtime}')


def load_image_from_url_list(path: str, target_dir: str, size_str: str, threads: int):
    """
    This function creates download option for each url adress
    and downloading files using multithreads

    :param path: path to the file with urls
    :param target_dir: path to the file in which downloads files
    :param size_str: size of images
    :param threads: quantity of threads
    :return:
    """
    start = time.time()

    if not isinstance(target_dir, str):
        raise TypeError('Dir should be a str')
    if not isinstance(threads, int):
        raise TypeError('Threads should be int')
    size = get_size(size_str)
    urls = tuple(enumerate(get_url(path)))

    download_option = tuple({
                             'target_dir': target_dir_maker(url[0], target_dir, len(urls)),
                             'url': url[1],
                             'number': url[0],
                             'size': size}
                            for url in urls)

    pool = ThreadPool(threads)
    download_results = tuple(pool.map(download_url, download_option))

    pool.close()
    pool.join()
    runtime = time.time() - start
    printer(*zip(*download_results), runtime)


