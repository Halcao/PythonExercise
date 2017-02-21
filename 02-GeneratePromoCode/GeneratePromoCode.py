import base64

src = "caohao+promo+"

arr = []
for n in range(0, 200, 1):
    # encode twice
    f = base64.encodestring(str(200-n)+'caohao'+str(100+n)+'promo'+str(n))
    s1 = base64.encodestring(f[::-1])
    print s1
    arr.append(s1)

for s1 in arr:
    print base64.decodestring(base64.decodestring(s1)[::-1])
