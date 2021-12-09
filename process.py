import pandas as pd
import sys

# to use: python3 process.py [infile] [outfile]
filename = sys.argv[1]
outfile = sys.argv[2]

# given y = mx + b generated from a standard curve
# where your current reading is y and you want x
# e.g abs = m[conc] + b
m = 0.004248
b = 0.3346


df = pd.read_excel(filename)
print("file read")

# converts from abs to mmol Pi
for (column, items) in df.iteritems():
    items = items.subtract(b)
    items = items.divide(m)
    df[column] = items

df.to_excel(outfile)
print("processed file written")
