# filter_deacot

## What This App Does

`filter_deacot.py` downloads annual CFTC legacy futures Commitments of Traders (COT) data for a given year, filters the dataset to a predefined list of contract market codes, and exports the filtered result to CSV.

Input:
- Year passed on the command line, for example `2024`

Output:
- `reports/filtered_data_<year>.csv` (for example `reports/filtered_data_2024.csv`)
- A row count message in the terminal after filtering

## Prerequisites

- Python 3.12+ (`python3 --version`)

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```

## Run

```bash
python filter_deacot.py <year>
```

Example:

```bash
python filter_deacot.py 2024
```

Expected output includes:

- `Rows after filtering: ...`
- `Filtered data saved to reports/filtered_data_2024.csv`

## Troubleshooting

- If activation fails, ensure you run from the project root:
  - `cd /home/ren/Documents/Projects/filter_deacot`
- If `pip` cannot download packages, check network access and retry:
  - `python -m pip install -r requirements.txt`
- If import errors occur, confirm the venv is active:
  - `which python`
  - `python -c "import pandas, cot_reports; print('ok')"`
