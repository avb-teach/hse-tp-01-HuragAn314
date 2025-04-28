import os, sys, shutil as s

input_dir, output_dir =sys.argv[1:3]
os.makedirs(output_dir, exist_ok=True)
k = {}
for d, i1, fs in os.walk(input_dir):
    for f in fs:
        b, e =os.path.splitext(f)
        n =k.get(b, 0)
        while os.path.exists(p:=f"{output_dir}/{b}_{n}{e}" if n else f"{output_dir}/{b}{e}"): n += 1
        k[b]= n+ 1
        s.copy2(f"{d}/{f}", p)
        