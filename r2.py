
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f: #-sig去除開頭奇怪的符號
        for line in f:
            lines.append(line.strip())
    return lines


def convert(lines):
    allen_word__count = 0
    allen_sticker_count = 0
    allen_image_count = 0
    viki_word__count = 0
    viki_sticker_count = 0
    viki_image_count = 0
    for line in lines:
        s = line.split(' ') #需要存成一個s，不能只寫.split
        time = s[0] #[:3] => 0到3，0可省略 (不包括3)
        name = s[1] #[-2:] => 倒數第2個位置，到最後
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1
            else:
                for m in s[2:]: #範圍從index 2 到最後
                    allen_word__count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                    viki_sticker_count += 1
            elif s[2] == '圖片':
                    viki_image_count += 1
            else:
                for m in s[2:]: #範圍從index 2 到最後
                    viki_word__count += len(m)
    print('Allen傳了', allen_sticker_count, '個貼圖')
    print('Allen傳了', allen_image_count, '個圖片')
    print('Allen傳了', allen_word__count, '個字')
    print('Viki傳了', viki_sticker_count, '個貼圖')
    print('Viki傳了', viki_image_count, '個圖片')
    print('Viki傳了', viki_word__count, '個字')


def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)
    # write_file('output.txt', lines) #先不用寫進檔案內，註記


main()