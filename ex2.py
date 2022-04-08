#!/usr/bin/env python3
""" Tetranucleotide frequency """
# --------------------------------------------------
def frequency(seq) -> None:
    count_a, count_c, count_g, count_t = 0, 0, 0, 0
    for base in seq:
        if base == 'A':
            count_a += 1
        elif base == 'C':
            count_c += 1
        elif base == 'G':
            count_g += 1
        elif base == 'T':
            count_t += 1

    print("A =",count_a,"C =",count_c,"G =",count_g,"T =",count_t)

def main():
    seq="ATAATGATAGATAGATGATC"
    frequency(seq)

# --------------------------------------------------
if __name__ == '__main__':
    main()