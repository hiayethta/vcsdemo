with open("guitars.txt", "r") as in_file:
    for line in in_file:
        # print(line)
        parts = line.strip().split(',')
        # print(parts)
        guitar = parts[0]
        price = parts[2]
        print(f"The {guitar} costs ${price}")
