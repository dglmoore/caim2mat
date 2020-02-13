# caim2mat

Convert Caim output files to CSV and Excel.

> **Note**: `caim2mat` requires python35 or greater.

## Installation

You can just clone and `python -m pip install [--user] .`.

## Usage

```shell
λ caim2mat -h
usage: caim2mat [-h] [--name NAME] [--csv] [--excel] [--value] [--pvalue]
                [--standarderror] [--all] [--force]
                FILE

Convert Caim output files to CSV or Excel format

positional arguments:
  FILE                  path to JSON file

optional arguments:
  -h, --help            show this help message and exit
  --name NAME, -n NAME  name of output files, defaults to the name of the
                        input file
  --csv, -c             output CSV files; one per data field
  --excel, -e           output Excel file; one worksheet per data field
  --value, -v           export the value field
  --pvalue, -p          export the p-values
  --standarderror, -s   export the standard error
  --all, -a             export all fields
  --force, -f           force overwriting if a file with the same name as an
                        output file already exists
```

Matrices are formatted with rows representing source variables and columns representing target
variables. That is the `(i,j)` element is the computed value between source `i` and target `j`. 

The output file names are based on the filename of the input file.
```shell
λ caim2mat mutual_info.json
λ ls
mutual_info.json  mutual_info_value.csv
```

This can be overridden with the `--name` argument:
```shell
λ caim2mat --name mi mutual_info.json
λ ls
mi_value.csv  mutual_info.json
```

You have the option of exporting to CSV and/or Excel files. If no format flag is provided, CSV is
assumed.
```shell
λ caim2mat --excel mutual_info.json
λ ls
mutual_info.json  mutual_info.xlsx
```

(Almost) all values stored in a JSON file output by Caim have a p-value and standard error
associated with them. You can optionally export those as well (`--all` to export all fields).

If you are converting to CSV files and request that more than one field be exported, each matrix is
output to a different file with the field name as a suffix.
```shell
λ caim2mat --all mutual_info.json
λ ls
mutual_info.json  mutual_info_pvalue.csv  mutual_info_standarderror.csv  mutual_info_value.csv
```

If you are exporting to Excel, each field gets its own worksheet, so only a single file is produced
and no field suffix is used.

Finally, `caim2mat` will not overwrite files by default. You can force overwriting with the
`--force` flag.
```shell
λ ../../caim2mat mutual_info.json
Error: file "mutual_info_value.csv" already exists; consider passing --force argument
λ ../../caim2mat --force mutual_info.json
```
