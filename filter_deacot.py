import sys
import pandas as pd
import cot_reports as cot

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <year>")
        sys.exit(1)
    
    markets = ['001601', '001602', '002601', '002602', '005601', '005602', '007601', '020601', '022651', '023651', '025651', '026603', 
               '033661', '039601', '039781', '040701', '042601', '043602', '044601', '045601', '054642', '057642', '058643', '061641',
               '067651', '06765T', '073732', '075651', '076651', '080732', '083731', '084691', '085692', '088691', '090741', '092741',
               '095741', '096741', '096742', '097741', '098661', '098662', '099741', '102741', '111659', '112741', '112661', '1170E1', 
               '122741', '124603', '124601', '13874A', '138741', '209742', '209741', '232741', '239741', '239742', '23977A', '23977A', 
               '240743', '244041', '244042', '244741', '244742', '299741', '133741', '146021', '135731', '058644', '047745', '221602',
               '004603'] 

    year = sys.argv[1]

    # Fetch data for the given year
    df = cot.cot_year(year=int(year), cot_report_type='legacy_fut')

    filtered_df = df[df["CFTC Contract Market Code"].isin(markets)].reset_index(drop=True)

    print(f"Rows after filtering: {len(filtered_df)}")
    filtered_df.to_csv(f"filtered_data_{year}.csv", index=False)
    print(f"Filtered data saved to filtered_data_{year}.csv")

if __name__ == "__main__":
    main()


