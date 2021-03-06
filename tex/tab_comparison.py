s = """70.4       & 73.9       & 76.0 & 71.4      & 71.2      & -0.2      & 75.8
     28.1       & 32.9       & 37.2      & 29.0      & 41.7 & \ma{12.7} & 40.5
     54.1       & 65.6       & 60.7      & 61.8      & 67.3 & \ma{5.5}  & 66.4
     33.7       & 36.7       & 41.1      & 34.5      & 42.4 & \ma{7.9}  & 43.9
     58.6       & 70.8 & 67.4 & 68.0 & 70.8 & \ma{2.8}  & 70.1
     61.7 & 65.1 & 59.8      & 59.1      & 59.7      & 0.6       & 62.9
     53.4       & 63.6 & 59.6      & 60.1      & 65.1      & \ma{5.0}  & 63.5
     69.0 & 78.4 & 76.1      & 76.8      & 78.8      & 2.0       & 79.2
     73.8 & 78.2 & 80.4      & 71.2      & 74.4      & 3.2       & 80.8
     70.5 & 78.5 & 82.7      & 76.6      & 75.9      & -0.7      & 77.7
     61.8       & 59.8       & 51.0      & 42.7      & 60.0      & \ma{17.3} & 64.3
     80.9 & 73.7       & 73.5      & 36.2      & 38.6      & \ma{2.4}  & 77.2      
     83.8 & 81.2       & 86.2      & 78.8      & 87.5      & \ma{8.7}  & 88.8"""
c = [0, 1, 2, 3, 4, 6]
tc=7
#th=[1.3, 1.6, 1.6, 2.3, 3.9, 4.3, 4.6, 5.1, 9.2, 13.8, 0.68, 0.74, 6.30]
th=[2.3 ,2.8 ,2.8 ,4.0 ,6.7 ,7.5 ,8.0 ,8.9 ,16.0 ,23.9 ,0.68 ,0.74 ,6.30]
assert max(c)+1==tc
for ir, row in enumerate(s.split("\n")):
    row=[e.strip() for e in row.strip().split("&")]
    out=[None]*len(row)
    for i in range(tc):
        if i not in c:
            out[i]=row[i]
    row=[(i, float(e)) for i, e in enumerate(row) if i in c]
    mv=max(row, key=lambda x: x[1])[1]
    for (i, e) in row:
        if e >= mv-th[ir]:
            e=r"\myu{%0.1f}"%e
        else:
            e="%0.1f"%e
        out[i]=e
    print " & ".join(out)
            
