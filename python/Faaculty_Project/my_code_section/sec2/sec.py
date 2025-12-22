import pandas as pd
import numpy as np

s1 = pd.Series(['a', np.arange(6).reshape(2, 3), 'b', [3.4, 4]])
print(s1)


# الفهرسه مش هتختلف كتير

S2 = s1[:5]

s4 = pd.Series(np.arange(10, 15), index=[
               'spring', 'river', 'lake', 'sea', 'ocean'])
s4['spring':'ocean':2]  # start : end : step
print(s4)

d = {
    "one": pd.Series("hi", index=["a", "b", "c", "d"]),
    "two": pd.Series([1.0, ["yes", "no"], 3.0, 5], index=["a", "b", "c", "d"]),
    "three": pd.Series({"c": 20, "a": 40, "b": 10}, index=["a", "b", "c", "d"])
}
df = pd.DataFrame(d)
print(df.one.index)
# print(df['a':'c'])
