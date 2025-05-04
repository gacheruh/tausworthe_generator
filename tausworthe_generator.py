def tausworthe_generator():
    # Initialize parameters
    r, q = 7, 9
    initial_bits = [0, 0, 1, 1, 0, 0, 1, 1, 0]  # b_1 to b_9
    l = 7  # segment length
    num_numbers = 20
    total_bits_needed = num_numbers * l
    
    # Generate sufficient bits
    bits = initial_bits.copy()
    for i in range(len(initial_bits), total_bits_needed):
        new_bit = bits[i - r] ^ bits[i - q]  # XOR operation
        bits.append(new_bit)
    
    return bits

# Generate bits
bits = tausworthe_generator()

# Print bits in groups of 7
print("Generated Bits (Grouped in 7-bit Segments):")
for i in range(0, len(bits), 7):
    segment = bits[i:i + 7]
    print(f"Bits {i+1}-{i+7}: {''.join(map(str, segment))}")

# Calculate and print normalized numbers
print("\nNormalized Random Numbers:")
for i in range(0, len(bits), 7):
    segment = bits[i:i + 7]
    if len(segment) < 7:
        break  # In case we don't have complete segments at the end
    decimal = sum(bit * (2 ** (6 - j)) for j, bit in enumerate(segment))
    normalized = decimal / 127.0
    print(f"u_{i//7 + 1}: {normalized:.6f} (Binary: {segment})")
