import pandas as pd
import simple_chalk as sc

class Observations:

    def __init__(self, wb_folder_path:str):
        self.wb_folder:str = wb_folder_path # Folder with Microsoft Excel workbooks with Observations data

        df = pd.DataFrame()
        # If data in excel workbook is tabular (in Excel tables)
        if tabular_data == True:
            try:
                df = pd.ExcelFile(path_or_buffer=ms_excel_wb_path, engine="openpyxl")
                        
            except FileNotFoundError:
                print(sc.red("The file was not found."))
            except IsADirectoryError:
                print(sc.red("The path is a directory, not a file."))
            except PermissionError:
                print("You do not have permission to access this file.")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            try:
                df = pd.read_excel(io=ms_excel_wb_path)
                        
            except FileNotFoundError:
                print("The file was not found.")
            except IsADirectoryError:
                print("The path is a directory, not a file.")
            except PermissionError:
                print("You do not have permission to access this file.")
            except Exception as e:
                print(f"An error occurred: {e}")

        if df.empty == False:
            return df
        else:
            return None


# Clean up dataframe
## Convert or Enum text result to numeric data