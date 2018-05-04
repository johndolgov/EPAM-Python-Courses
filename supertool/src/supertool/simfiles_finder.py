import os
import hashlib


def printer(duplicates):

    if duplicates:
        print('There is duplicate:')
        for key, values in duplicates.items():
            print('-------------------\n')
            print('This files duplicate each other')
            print('------------------\n')
            print('\nand\n'.join(values))
    else:
        print('There is not duplicates here')


def chunk_reader(f_obj, chunk_size: int = 1024):
    while True:
        chunk = f_obj.read(chunk_size)
        if not chunk:
            return
        yield chunk


def get_hash(filename, hash_func = hashlib.md5):

    hashobj = hash_func()
    file_object = open(filename, 'rb')
    for chunk in chunk_reader(file_object):
        hashobj.update(chunk)
    hashed = hashobj.digest()
    file_object.close()
    return hashed


def check_for_duplicates(path):

    hashes_size = {}
    for dir_path, dir_names, file_names in os.walk(path):
        for filename in file_names:
            full_path = os.path.join(dir_path, filename)
            if hashes_size.get(os.path.getsize(full_path)):
                hashes_size[os.path.getsize(full_path)].append(full_path)
            else:
                hashes_size[os.path.getsize(full_path)] = []
                hashes_size[os.path.getsize(full_path)].append(full_path)

    if not os.path.exists(path):
        raise ValueError("Directory do not exist")

    result_size = list(filter(lambda entry: len(entry) > 1, hashes_size.values()))

    hashes = {}
    for files in result_size:
        for filename in files:
            if hashes.get(get_hash(filename)):
                hashes[get_hash(filename)].append(filename)
            else:
                hashes[get_hash(filename)] = []
                hashes[get_hash(filename)].append(filename)
    return dict(filter(lambda entry: len(entry[1]) > 1,
                       hashes.items()))
