import bitstring as b
import sys

def compress(string):
    S = {'':0}
    counter = ''
    out = ''
    fin = b.BitArray()
    for i in string:
        i = str(int(i))
        counter1 = counter
        counter += i
        if counter not in S:
            l = len(bin(len(S) - 1)) - 2
            ind = S[counter1]
            m = ("{0:0"+str(l)+"b}").format(ind)
            out += m + i
            S[counter] = len(S)
            counter = ''
        else:
            pass
        
    size = 8
    if counter != '':
        out += counter
        last = ("{0:0"+str(size)+"b}").format(len(counter))
    else:
        last = ("{0:0"+str(size)+"b}").format(0)

    if len(out) // 8 == 0:
        tam = 0
        last += ("{0:0"+str(size)+"b}").format(0)
    else:
        tam = int((1 - (len(out) / 8 - len(out) // 8)) * 8)
        last += ("{0:0"+str(size)+"b}").format(tam)

    n_out = out[::-1]
    n_out += last[::-1]
    out = n_out[::-1]

    fin.append('0b'+out+'0'*tam)
    return fin

def main(file):
    print(file)
    s = b.ConstBitStream(filename=file)
    print(len(s.bin))
    bits = compress(s)
    output_file = sys.argv[2]
    with open(output_file,'wb') as f:
        bits.tofile(f)
        f.close()

    return 0

if __name__ == '__main__':
    main(sys.argv[1])
