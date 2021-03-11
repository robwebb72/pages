import os

def file_ext_matches(file_, ext):
    filename = os.path.splitext(file_)
    return len(filename) == 2 and filename[1] == ext


for dir_, sub, files_ in os.walk('.'):
    matched_files = [x for x in files_ if file_ext_matches(x, '.py')]
    for matched_file in matched_files:
        print(matched_file)
