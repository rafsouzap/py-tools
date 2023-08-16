import argparse
import pandas as pd
from tabulate import tabulate
from tqdm import tqdm

parser = argparse.ArgumentParser(description='Grouping and counting a CSV file')
parser.add_argument('-f', '--file', type=str, nargs='+', required=True, help='One or more CSV files to be read')
parser.add_argument('-g', '--columnGroup', type=str, required=True, help='The name of the column to be grouped')
parser.add_argument('-cf', '--columnFiltered', type=str, required=False, help='The name of the column to be filtered')
parser.add_argument('-cv', '--columnFilter', type=str, required=False, help='The value to use for the filter on the filtered column')
parser.add_argument('-e', '--encoding', type=str, required=False, default='ISO-8859-1', help='The encoding to be used when reading the CSV file (default: ISO-8859-1)')

args = parser.parse_args()

if args.columnFilter and not args.columnFiltered:
    parser.error("A filtered column argument is required when a value to filter is given")

if args.columnFiltered and not args.columnFilter:
    parser.error("An argument with the value for the filter is required when a column to be filtered is given")

try:
    csv_files = args.file
    
    df = pd.DataFrame()

    for file in tqdm(csv_files):
        temp_df = pd.read_csv(file, encoding=args.encoding, delimiter=';', low_memory=False)
        df = pd.concat([df, temp_df])

    if args.columnFiltered and args.columnFilter:
        df = df[df[args.columnFiltered] == args.columnFilter]

    grouped_df = df.groupby(args.columnGroup).size()

    counted_df = pd.DataFrame({args.columnGroup:grouped_df.index, 'count':grouped_df.values})
    counted_df[args.columnGroup] = counted_df[args.columnGroup].str.ljust(50)

    counted_df = counted_df.sort_values('count', ascending=False)

    total_count = counted_df['count'].sum()
    total_df = pd.DataFrame({args.columnGroup: ['Total'], 'count': [total_count]})

    counted_df = pd.concat([counted_df, total_df], ignore_index=True)
   
    print(f"\n{len(counted_df)} groups found.\n")
    print(tabulate(counted_df, headers='keys', tablefmt='simple_grid', showindex=False))

except FileNotFoundError:
    print(f"\nThe file {args.file} was not found.")