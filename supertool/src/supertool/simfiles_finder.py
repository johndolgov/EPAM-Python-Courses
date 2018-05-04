import os
import sys
import hashlib


def chunk_reader(f_obj, chunk_size: int = 1024):
    """
    Generator that reads a file in bytes

    :param f_obj:
    :param chunk_size:
    :return:
    """
    while True:
        chunk = f_obj.read(chunk_size)
        if not chunk:
            return
        yield chunk


def get_hash(filename, hash=hashlib.md5):

    hashobj = hash()
    with open(filename, 'rb') as file_obj:
        for chunk in chunk_reader(file_obj):
            hashobj.update(chunk)
    return hashobj.hexdigest()


def check_for_duplicates(paths, hash=hashlib.sha1):
    hashes_by_size = {}
    hashes_on_1k = {}
    hashes_full = {}

    for path in paths:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                try:
                    file_size = os.path.getsize(full_path)
                except (OSError,):
                    pass

                duplicate = hashes_by_size.get(file_size)

                if duplicate:
                    hashes_by_size[file_size].append(full_path)
                else:
                    hashes_by_size[file_size] = []  # create the list for this file size
                    hashes_by_size[file_size].append(full_path)

    # For all files with the same file size, get their hash on the 1st 1024 bytes
    for __, files in hashes_by_size.items():
        if len(files) < 2:
            continue    # this file size is unique, no need to spend cpy cycles on it

        for filename in files:
            small_hash = get_hash(filename, first_chunk_only=True)

            duplicate = hashes_on_1k.get(small_hash)
            if duplicate:
                hashes_on_1k[small_hash].append(filename)
            else:
                hashes_on_1k[small_hash] = []          # create the list for this 1k hash
                hashes_on_1k[small_hash].append(filename)

    # For all files with the hash on the 1st 1024 bytes, get their hash on the full file - collisions will be duplicates
    for __, files in hashes_on_1k.items():
        if len(files) < 2:
            continue    # this hash of fist 1k file bytes is unique, no need to spend cpy cycles on it

        for filename in files:
            full_hash = get_hash(filename, first_chunk_only=False)

            duplicate = hashes_full.get(full_hash)
            if duplicate:
                print("Duplicate found: %s and %s" % (filename, duplicate))
            else:
                hashes_full[full_hash] = filename

if sys.argv[1:]:
    check_for_duplicates(sys.argv[1:])
else:
    print("Please pass the paths to check as parameters to the script")