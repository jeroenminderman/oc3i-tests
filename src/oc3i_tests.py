from pathlib import Path

import pandas as pd
from oc3i import Coder

CURRENT_DIR = Path(__file__).resolve().parent
BENCHMARK_DATA_FILE = "isco_benchmark_data.xlsx"

data_file = CURRENT_DIR.parent / "data" / BENCHMARK_DATA_FILE


def summarise_output(df,
                     given_code,
                     prediction1,
                     prediction2,
                     prediction3,
                     filter_col=None,
                     filter_value=None):
    """Summarise the output of the coding process."""
    """If filter_col and filter_value are provided,
    filter the dataframe accordingly."""

    if filter_col and filter_value:
        df = df[df[filter_col] == filter_value]

    total_cases = len(df)
    match1 = (df[given_code] == df[prediction1]).sum()
    match123 = (
            (df[given_code] == df[prediction1]) |
            (df[given_code] == df[prediction2]) |
            (df[given_code] == df[prediction3])
        ).sum()

    return {
        "total_cases": total_cases,
        "match1": match1,
        "match123": match123
    }


def main():
    coder = Coder(scheme="isco")

    dat = pd.read_excel(data_file, dtype={"MANUAL_ISCO": str})
    dat["TASKS"] = dat["TASKS"].fillna("")
    dat["INDUSTRY"] = dat["INDUSTRY"].fillna("")

    out = coder.code_data_frame(dat,
                                title_column="TITLE",
                                description_column="TASKS",
                                sector_column="INDUSTRY")

    perf1 = summarise_output(out,
                             given_code="MANUAL_ISCO",
                             prediction1="prediction 1",
                             prediction2="prediction 2",
                             prediction3="prediction 3")
    print(perf1)

    perf2 = summarise_output(out,
                             given_code="MANUAL_ISCO",
                             prediction1="prediction 1",
                             prediction2="prediction 2",
                             prediction3="prediction 3",
                             filter_col="TYPE",
                             filter_value="Exact match")
    print(perf2)


if __name__ == "__main__":
    main()
