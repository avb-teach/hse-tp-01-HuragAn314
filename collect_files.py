import os, sys, shutil as s

input_dir, output_dir = sys.argv[1], sys.argv[2]
mx=int(sys.argv[4]) if '--max_depth' in sys.argv else None
os.makedirs(output_dir, exist_ok=True)
k = {}
for d, i1, f in os.walk(input_dir):
    r=os.path.relpath(d, input_dir)
    l=r.split(os.sep).index('.') if r=='.' else len(r.split(os.sep))
    if mx is not None and l>mx: continue
    for i in f:
        a, x=os.path.splitext(i)
        n =k.get(a, 0)
        while os.path.exists(p:=f"{output_dir}/{a}_{n}{x}" if n else f"{output_dir}/{a}{x}"): n+=1
        k[a], i1 =n+1, s.copy2(os.path.join(d, i), p)