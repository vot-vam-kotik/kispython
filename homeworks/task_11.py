from struct import *


FMT = dict(
    char='<c',
    int8='<b',
    uint8='<B',
    int16='<h',
    uint16='<H',
    int32='<i',
    uint32='<I',
    int64='<q',
    uint64='<Q',
    float='<f',
    double='<d'
)


def parse(buf, offs, ty):
    return unpack_from(FMT[ty], buf, offs)[0], offs + calcsize(FMT[ty])


def parse_a(buf, offs):
    a1, offs = parse(buf, offs, 'double')
    a2_size = 3
    a2 = []
    for _ in range(a2_size):
        val, offs = parse_b(buf, offs)
        a2.append(val)

    a3_size = 2
    a3 = []
    for _ in range(a3_size):
        val, offs = parse_c(buf, offs)
        a3.append(val)

    a4, offs = parse(buf, offs, 'int8')
    a5, offs = parse(buf, offs, 'int16')

    a6_size, offs = parse(buf, offs, 'uint16')
    a6_offs, offs = parse(buf, offs, 'uint32')
    a6 = []
    for _ in range(a6_size):
        val, a6_offs = parse(buf, a6_offs, 'uint32')
        a6.append(val)

    return dict(A1=a1, A2=a2, A3=a3, A4=a4,
                A5=a5, A6=a6), offs


def parse_b(buf, offs):
    b1, offs = parse(buf, offs, 'int16')
    b2, offs = parse(buf, offs, 'int32')
    b3, offs = parse(buf, offs, 'float')
    return dict(B1=b1, B2=b2, B3=b3), offs


def parse_c(buf, offs):
    c1_offs, offs = parse(buf, offs, 'uint32')
    c1, c1_offs = parse_d(buf, c1_offs)
    c2, offs = parse(buf, offs, 'uint32')
    c3, offs = parse(buf, offs, 'int8')
    c4, offs = parse(buf, offs, 'int64')
    c5, offs = parse(buf, offs, 'int8')
    c6, offs = parse(buf, offs, 'uint64')
    c7, offs = parse(buf, offs, 'float')
    return dict(C1=c1, C2=c2, C3=c3, C4=c4, C5=c5, C6=c6, C7=c7), offs


def parse_d(buf, offs):
    d1, offs = parse(buf, offs, 'int8')
    d2, offs = parse(buf, offs, 'uint32')
    d3, offs = parse(buf, offs, 'int8')
    d4_size = 2
    d4 = []
    for _ in range(d4_size):
        val, offs = parse(buf, offs, 'uint8')
        d4.append(val)  # возможно тут нужен декод, см у ани
    d5, offs = parse(buf, offs, 'float')
    return dict(D1=d1, D2=d2, D3=d3, D4=d4, D5=d5), offs


def main(buf):
    return parse_a(buf, 3)[0]

data1 = (
    b'HSZ\xd8\x9e\x07J\xf1<\xe6\xbfl O\xeak;\x9e\xcd\x9f\xbe O\xc0\x9e{s\x02'
    b'q\xc5\xbe\xe3\xc5\xd7M\xb1A\x1ad\\?n\x00\x00\x00)\xaf\xefm\xdb\x15c5--\x1c'
    b'\x12#^\xc2M\x14\x18\xe7\x9a\x80\x08M\x93\x15\xbez\x00\x00\x00\xe5\x00\xe1T;'
    b'\x7f\xaej\xda\xf5Cm\x1f\xb0B\xc9\xeb\xfa\xd85\xbb\xb4\x94\xf9\xc3>\xfdp\xac'
    b'\x07\x00\x86\x00\x00\x00\x82H\x9e\x88u\xd6\xe7\xea\xe9\x8b\xd4<1\x025yM\x98'
    b'1>*\xe7\x8f\xbep\xa8\xd6p\xca\x82\xe3\x13\xcd\xafT\xa6\xe3\xecg\xea\x11l'
    b'\xad)?\xe1/\xec\xd0\xcd\xfbF'
)
print(main(data1))