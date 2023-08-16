# PyTools

PyTools are a set of small scripts developed in Python to optimize your day-to-day life.


## Installation

After cloning the repository, install the dependencies needed to use the scripts.

```bash
pip install -r requirements.txt
```

## Tools

### Splits a CSV file into smaller chunks

```bash
csv-split.py [-h] -f FILE [-c CHUNKSIZE] -n COLUMNNAME [-e ENDLINE] [-q QUOTECHAR]

# arguments:
#   -h, --help            show this help message and exit
#   -f FILE, --file FILE  The CSV file to be split
#   -c CHUNKSIZE, --chunkSize CHUNKSIZE
#                         The chunk size for reading the CSV file
#   -n COLUMNNAME, --columnName COLUMNNAME
#                         The name of the column to be extracted from the CSV file
#   -e ENDLINE, --endline ENDLINE
#                         The endline to be used when create a TXT file
#   -q QUOTECHAR, --quotechar QUOTECHAR
#                         The quotechar to be used when create a TXT file (default: ")
```

### Grouping and counting a CSV file

```bash
usage: csv-group-count.py [-h] -f FILE [FILE ...] -g COLUMNGROUP [-cf COLUMNFILTERED] [-cv COLUMNFILTER] [-e ENCODING]

# arguments:
#   -h, --help            show this help message and exit
#   -f FILE [FILE ...], --file FILE [FILE ...]
#                         One or more CSV files to be read
#   -g COLUMNGROUP, --columnGroup COLUMNGROUP
#                         The name of the column to be grouped
#   -cf COLUMNFILTERED, --columnFiltered COLUMNFILTERED
#                         The name of the column to be filtered
#   -cv COLUMNFILTER, --columnFilter COLUMNFILTER
#                         The value to use for the filter on the filtered column
#   -e ENCODING, --encoding ENCODING
#                         The encoding to be used when reading the CSV file (default: ISO-8859-1)
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License

[MIT](https://choosealicense.com/licenses/mit/)
