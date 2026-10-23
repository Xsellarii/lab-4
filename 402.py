import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    counts = {}
    max_freq = 0

    for char in line:
        if char.isalpha():
            upper_char = char.upper()
            counts[upper_char] = counts.get(upper_char, 0) + 1
            if counts[upper_char] > max_freq:
                max_freq = counts[upper_char]

    if max_freq == 0:
        continue

    most_common = sorted([char for char, freq in counts.items() if freq == max_freq])

    print("".join(most_common))
    print(max_freq)