import os
import sqlite3
from datetime import datetime, timedelta

import pandas as pd
from dotenv import load_dotenv
from gspread_pandas import Spread

load_dotenv()
load_dotenv(".env.googlesheets")


CONED_SPREADSHEET_COPY = os.getenv("CONED_SPREADSHEET_COPY")
TILLER_SPREADSHEET_COPY = os.getenv("TILLER_SPREADSHEET_COPY")
QUIRK_CLASS_LIST = os.getenv("QUIRK_CLASS_LIST")




def main():
    
    # spread = Spread(QUIRK_CLASS_LIST)

    # spread.open_sheet("All Info")

    # last_existing_row = spread.get_sheet_dims()[0]
    # starting_row = last_existing_row + 1

    # df = spread.sheet_to_df(index=None)
    # print(df)

    # with sqlite3.connect("quirk_list.db") as conn:
    #     df.to_sql("quirk_list", conn, if_exists="replace")

    with sqlite3.connect("quirk_list.db") as conn:
        df = pd.read_sql("SELECT * from quirk_list", conn)

    print(df)


        

    # df_new = pd.read_csv("test.csv", index_col=0)

    # # df = pd.concat([df, df_new], ignore_index=True)

    # spread.df_to_sheet(df_new, index=False, headers=False, start=(starting_row, 1))


    # # Save DataFrame to worksheet 'New Test Sheet', create it first if it doesn't exist
    # spread.df_to_sheet(df, index=False, sheet='New Test Sheet', start='A1', replace=True)

    # Make columns bold!
    # spread.sheet.format('A1:AL1', {'textFormat': {'bold': True}})



if __name__ == "__main__":
    main()