with open("input_file.csv", "r") as infile, open("output_file.csv", "w") as outfile:
    for lines in infile:
        print(lines.strip())
        outfile.write(lines)