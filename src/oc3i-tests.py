from pathlib import Path

import pandas as pd
from oc3i import Coder

CURRENT_DIR = Path(__file__).resolve().parent
BENCHMARK_DATA_FILE = "isco_benchmark_data.xlsx"

data_file = CURRENT_DIR.parent / "data" / BENCHMARK_DATA_FILE

coder = Coder(scheme="isco")

dat = pd.read_excel(data_file, dtype={"MANUAL_ISCO": str})
dat["TASKS"] = dat["TASKS"].fillna("")
dat["INDUSTRY"] = dat["INDUSTRY"].fillna("")
dat["INDUSTRY2"] = ""

out = coder.code_data_frame(dat,
                            title_column="TITLE",
                            description_column="TASKS",
                            sector_column="INDUSTRY2")
out["MANUAL_ISCO"] = dat["MANUAL_ISCO"]
out.to_csv("output.csv", index=False)
