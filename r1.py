
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f: #-sig去除開頭奇怪的符號
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None #第一行無人名的時候
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person: #如果person有值，才執行
            new.append(person + ': ' + line)
    return new

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)


main()