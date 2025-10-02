import pandas as pd
from oc3i import Coder
from oc3i.coder import get_example_file

coder = Coder(scheme="isco")

dat = pd.read_csv(get_example_file())
dat = pd.read_excel("../data/isco_benchmark_data.xlsx")
out = coder.code_data_frame(dat,
                            title_column="job_title",
                            description_column="job_description",
                            sector_column="job_sector")
print(out.head())
