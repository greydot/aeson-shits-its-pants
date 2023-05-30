#!/usr/bin/env python3

import string
import random

N=1000000

def rand_str():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=5))

with open("file.json", "w") as f:
    f.write("{\n")
    s = set()
    for i in range(N):
        k = rand_str()
        while k in s:
            k = rand_str()
        s.add(k)
        v = rand_str()
        f.write("  \"{0}\": \"{1}\"".format(k,v))
        if i == N-1:
            f.write("\n")
        else:
            f.write(",\n")
    f.write("}\n")

