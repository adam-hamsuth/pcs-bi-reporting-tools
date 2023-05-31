import argparse
import hashlib


def remove_dupes_from_csv(input_file, output_file):
    with open(input_file, "r") as file_in:
            with open(output_file, "w") as file_out:

                line_hashes = set()

                for line in file_in:
                    line_hash = hashlib.md5(line.encode()).digest()
                    if line_hash not in line_hashes:
                        line_hashes.add(line_hash)
                        file_out.write(line)


if __name__ == "__main__":

    input_file = "input.csv"
    output_file = "output.csv"

    parser = argparse.ArgumentParser(
        prog='CSV Duplicate Removal',
        description='Removes all duplicate lines from a CSV input file'
    )

    parser.add_argument('-f', '--infile')
    parser.add_argument('-o', '--outfile')

    args = parser.parse_args()

    if args.infile:
        input_file = args.infile
    if args.outfile:
        output_file = args.outfile

    remove_dupes_from_csv(input_file, output_file)
