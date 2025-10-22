from numbers_parser import Document
import pandas as pd
from pathlib import Path


class DataExtract:
    def __init__(self, base_path: Path):
        self.base_path = base_path

    def from_numbers(self, input_filename: str, output_filename: str) -> pd.DataFrame:

        numbers_file = self.base_path / "data" / input_filename
        output_path = self.base_path / "data" / output_filename

        doc = Document(numbers_file)
        sheet = doc.sheets[0]
        table = sheet.tables[0]

        data = []
        for row in table.rows():
            values = [cell.value for cell in row]
            data.append(values)

        header = data[0]
        rows = data[1:]
        df = pd.DataFrame(rows, columns=header)
        df.to_csv(output_path, index=False, encoding="utf-8")

        return df

    def from_csv(self, input_filename: str, headers: list[str] = None, first_row_header: bool = False) -> pd.DataFrame:

        input_path = self.base_path / "data" / input_filename

        if first_row_header:
            df = pd.read_csv(input_path, header=0)
        else:
            df = pd.read_csv(input_path, header=None)
            if headers:
                df.columns = headers

        return df