# permutation_boxes.py
# Author: Nazibur Rahman
# Description: Implements PC-1, Compression 64->48, and Expansion 48->64
# Usage: Run to test sample inputs

def permute(input_bits, permutation_table):
    """Permute bits according to permutation_table."""
    return ''.join(input_bits[i - 1] for i in permutation_table)

# 1. Permutation Choice-1 Box (64-bit to 56-bit)
PC1_TABLE = [
    57, 49, 41, 33, 25, 17, 9,
    1,  58, 50, 42, 34, 26, 18,
    10, 2,  59, 51, 43, 35, 27,
    19, 11, 3,  60, 52, 44, 36,

    63, 55, 47, 39, 31, 23, 15,
    7,  62, 54, 46, 38, 30, 22,
    14, 6,  61, 53, 45, 37, 29,
    21, 13, 5,  28, 20, 12, 4
]

# 2. Compression Box (64-bit to 48-bit)
COMPRESSION_BOX = [
    1,  3,  5,  7,  9,  11, 13, 15,
    17, 19, 21, 23, 25, 27, 29, 31,
    33, 35, 37, 39, 41, 43, 45, 47,
    49, 51, 53, 55, 57, 59, 61, 63,
    2,  4,  6,  8,  10, 12, 14, 16,
    18, 20, 22, 24, 26, 28, 30, 32
]

# 3. Expansion Box (48-bit to 64-bit)
EXPANSION_BOX = [
    1,  1,  2,  2,  3,  3,  4,  4,
    5,  5,  6,  6,  7,  7,  8,  8,
    9,  9,  10, 10, 11, 11, 12, 12,
    13, 13, 14, 14, 15, 15, 16, 16,
    17, 17, 18, 18, 19, 19, 20, 20,
    21, 21, 22, 22, 23, 23, 24, 24,
    25, 25, 26, 26, 27, 27, 28, 28,
    29, 29, 30, 30, 31, 31, 32, 32
]

def hex_to_bin(hex_str, length):
    return bin(int(hex_str, 16))[2:].zfill(length)

def bin_to_hex(bin_str):
    return hex(int(bin_str, 2))[2:].upper().zfill(len(bin_str) // 4)

def test():
    input_64bit = "0123456789ABCDEF"
    bin_input = hex_to_bin(input_64bit, 64)
    print("Original 64-bit input :", input_64bit)

    # PC-1
    pc1_result = permute(bin_input, PC1_TABLE)
    print("PC-1 output (56-bit)   :", bin_to_hex(pc1_result))

    # Compression
    compression_result = permute(bin_input, COMPRESSION_BOX)
    print("Compressed to 48-bit   :", bin_to_hex(compression_result))

    # Expansion
    expansion_input = compression_result  # simulate E -> 48-bit to 64-bit
    expanded_result = permute(expansion_input, EXPANSION_BOX)
    print("Expanded back to 64-bit:", bin_to_hex(expanded_result))

if __name__ == "__main__":
    test()
