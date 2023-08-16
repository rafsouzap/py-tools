import argparse
import pandas as pd
import os

parser = argparse.ArgumentParser(description='Splits a CSV file into smaller chunks')
parser.add_argument('-f', '--file', type=str, required=True, help='The CSV file to be split')
parser.add_argument('-c', '--chunkSize', type=int, default=10000, help='The chunk size for reading the CSV file')
parser.add_argument('-n', '--columnName', type=str, required=True, help='The name of the column to be extracted from the CSV file')
parser.add_argument('-e', '--endline', type=str, default='', help='The endline to be used when create a TXT file')
parser.add_argument('-q', '--quotechar', type=str, default='"', help='The quotechar to be used when create a TXT file (default: ")')

args = parser.parse_args()

file_counter = 0

try:
    filename_without_ext = os.path.splitext(args.file)[0]

    for chunk in pd.read_csv(args.file, chunksize=args.chunkSize):
        selected_column = chunk[args.columnName]
        selected_column = selected_column.apply(lambda x: f'{args.quotechar}{x}{args.quotechar}{args.endline}')

        with open(f'{filename_without_ext}__Part-{file_counter}.txt', 'w') as f:
            f.write('\n'.join(selected_column))

        file_counter += 1

    print(f"\nDone! {file_counter} files were created.")
except FileNotFoundError:
    print(f"\nThe file {args.file} was not found.")