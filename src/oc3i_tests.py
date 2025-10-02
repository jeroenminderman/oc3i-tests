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


def load_clean_and_code():
    coder = Coder(scheme="isco")

    dat = pd.read_excel(data_file, dtype={"MANUAL_ISCO": str})
    dat["TASKS"] = dat["TASKS"].fillna("")
    dat["INDUSTRY"] = dat["INDUSTRY"].fillna("")

    out = coder.code_data_frame(dat,
                                title_column="TITLE",
                                description_column="TASKS",
                                sector_column="INDUSTRY")

    return (out)


def report_match_stats(perf, type="match1"):
    if type == "match1":
        return (float(round(perf["match1"] / perf["total_cases"], 2) * 100))
    if type == "match123":
        return (float(round(perf["match123"] / perf["total_cases"], 2) * 100))


def main():
    out = load_clean_and_code()

    perf1 = summarise_output(out,
                             given_code="MANUAL_ISCO",
                             prediction1="prediction 1",
                             prediction2="prediction 2",
                             prediction3="prediction 3")

    perf2 = summarise_output(out[~out["TYPE"].isin(["Deeper ambiguity",
                                                    "Semantic ambiguity",
                                                    "Scheme ambiguity"])],
                             given_code="MANUAL_ISCO",
                             prediction1="prediction 1",
                             prediction2="prediction 2",
                             prediction3="prediction 3")

    print("")
    print(f"Performance on all {perf1["total_cases"]} cases:")
    print("Accuracy results: ")
    print(
        f"Manual code matches best prediction: "
        f"{report_match_stats(perf1, type="match1"):.1f}%"
    )
    print(
        f"Manual code included in top 3 predictions: "
        f"{report_match_stats(perf1, type="match123"):.1f}%"
        )
    print("")
    print(
        f"Performance when excluding a priori ambiguous cases "
        f"(retaining {perf2["total_cases"]} cases):"
        )
    print("Accuracy results: ")
    print(
        f"Manual code matches best prediction: "
        f"{report_match_stats(perf2, type="match1"):.1f}%"
        )
    print(
        f"Manual code included in top 3 predictions: "
        f"{report_match_stats(perf2, type="match123"):.1f}%"
        )


if __name__ == "__main__":
    main()
