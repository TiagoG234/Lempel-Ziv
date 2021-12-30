import bitstring as b
import sys

def decompress(string):
    S = ['']
    out = ''
    init = 8
    string = string.bin
    f = b.BitArray()
    fin = int(string[:init], 2)
    pad = int(string[8:16], 2)
    j = 16
    valid = True
    string = string[:-pad]
    while valid:
        l = len(bin(len(S) - 1)) - 2
        point = string[j:j+l]
        new = string[j+l]
        out += (S[int(point,2)] + new)
        S.append(S[int(point,2)] + new)
        j += l + 1
        if j >= len(string) - fin:
            valid = False
    out += string[len(string) - fin:]
    f.append('0b'+out)
    return f
    
def main(file):

    s = b.ConstBitStream(filename=file)
    bits = decompress(s)
    output_file = sys.argv[2]
    with open(output_file,'wb') as f:
        bits.tofile(f)
        f.close()

    return 0

if __name__ == '__main__':
    main(sys.argv[1])
