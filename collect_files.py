import os, sys, shutil as s

input_dir, output_dir,mx =sys.argv[1:4] if '--max_depth' in sys.argv else (sys.argv[1], sys.argv[2], None)
os.makedirs(output_dir, exist_ok=True)
k, m_d= {}, int(mx.split('=')[1]) if mx else None
for d, i1, fs in os.walk(input_dir):
    if m_d and len(os.path.relpath(d, input_dir).split(os.sep))> m_d: continue
    for f in fs:
        p =f"{output_dir}/{n[0]}_{n[1]}{n[2]}" if (n:=(*os.path.splitext(f), k.get((output_dir:=os.path.splitext(f)[0]), 0))) and os.path.exists(t:=f"{output_dir}/{n[0]}{n[2]}") else t
        while os.path.exists(p):n =(n[0], n[1]+1, n[2]); p= f"{output_dir}/{n[0]}_{n[1]}{n[2]}"
        k[output_dir] = n[1] +1; s.copy2(f"{d}/{f}", p)
