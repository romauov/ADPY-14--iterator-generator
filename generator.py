import hashlib

def my_hash_generator(input_file):

    with open(input_file, encoding='utf8') as f:
        while True:
            text_line = f.readline().rstrip()
            hash_object = hashlib.md5(text_line.encode())
            yield hash_object.hexdigest()

            if not text_line:
                break

for elm in my_hash_generator('countries wiki URLs.html'):
    print(elm)
