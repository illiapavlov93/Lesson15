import os


def gen_path(top):
    for path, dir_list, file in os.walk(top):
        for f in file:
            yield os.path.join(path, f)


py_files = gen_path('.')
for i in py_files:
    print(i)
