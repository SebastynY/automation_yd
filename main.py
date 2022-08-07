from datetime import datetime
from pathlib import Path
import requests
import pandas as pd
from io import BytesIO
from settings import (
    URL, BODY, HEADER,
    FORM_DATETIME
)


class Report:
    __report_folder: Path = Path("reports")

    @staticmethod
    def __get_filename():
        return Path(
            f"report[{datetime.now().strftime(FORM_DATETIME)}].xlsx"
        )

    @staticmethod
    def __get_content_response():
        return requests.post(
            url=URL, json=BODY,
            headers=HEADER
        ).content

    def create_report(self):
        file_from_bytes = BytesIO(self.__get_content_response())
        df = pd.read_csv(file_from_bytes, delimiter='\t')
        df.to_excel(self.__report_folder / self.__get_filename())
        return df


if __name__ == '__main__':
    Report().create_report()
