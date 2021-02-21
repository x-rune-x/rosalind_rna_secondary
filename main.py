import math


def find_matching(input_file):
    file = open(input_file, "r")

    rna_seq = file.read()

    # Find the number of AU and GC pairs.
    au_count = 0
    gc_count = 0

    for nucleotide in range(len(rna_seq)):
        if rna_seq[nucleotide] == "A":
            au_count += 1
        elif rna_seq[nucleotide] == "G":
            gc_count += 1

    # For each possible AU pair, multiply it by all possible GC pairs.
    perfect_matchings = math.factorial(au_count) * math.factorial(gc_count)

    return perfect_matchings


solution = find_matching("rosalind_pmch.txt")
print(solution)
