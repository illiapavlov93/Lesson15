def read_file(file_name):
    for line in open(file_name):
        yield line.strip()


def print_lines(line_s):
    unique = set()
    for line in line_s:
        if line not in unique:
            unique.add(line)
            print(line)


lines = read_file('File.txt')
print_lines(lines)
