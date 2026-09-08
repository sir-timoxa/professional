def nonempty_lines(file):
    with open(file, encoding='utf-8') as file:
        file_lines = (line.strip() for line in file)
        not_empty = (line for line in file_lines if line)
        result = (line if len(line) < 25  else '...' for line in not_empty)
        yield from result

def nonempty_lines(file):
    with open(file, encoding='utf-8') as f:
        yield from ('...' if len(line.strip()) > 25 else line.strip()
                    for line in f if line.strip())