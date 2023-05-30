#!/usr/bin/env python3

import string
import random

N=1000000

with open("file.json", "w") as f:
    f.write("{\n")
    for i in range(N):
        k = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        v = ''.join(random.choices(string.ascii_lowercase, k=5))
        f.write("  \"{0}\": \"{1}\"".format(k,v))
        if i == N-1:
            f.write("\n")
        else:
            f.write(",\n")
    f.write("}\n")

