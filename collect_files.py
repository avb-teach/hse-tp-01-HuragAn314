import os, sys, shutil as s

input_dir, output_dir =sys.argv[1], sys.argv[2]
mx=int(sys.argv[sys.argv.index('--max_depth')+1]) if '--max_depth' in sys.argv else None
os.makedirs(output_dir, exist_ok=True)
k={}
for d, i1, fs in os.walk(input_dir):
    p=os.path.relpath(d, input_dir)
    if mx is not None and (p.count(os.sep) +1 if p != '.' else 0)>mx: continue
    for f in fs:
        a, x= os.path.splitext(f)
        n =k.get(a, 0)
        while os.path.exists(dx:=os.path.join(output_dir, f"{a}_{n}{x}") if n else os.path.join(output_dir, f"{a}{x}")):n+=1
        k[a] =n+1
        s.copy2(os.path.join(d, f), dx)