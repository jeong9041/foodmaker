def avg(data, start=0, end=None) :
    if not end :
        end = len(data)
    return sum(data[start:end])/float(end-start)

d = (3, 4, 5, 6, 7)
d2 = d[1:3]
print(d2)
avg(d, 0, 5)
print(avg(d, 0, 5))
avg(d)
print(avg(d))
avg(d, end=3)
print(avg(d, end=3))   