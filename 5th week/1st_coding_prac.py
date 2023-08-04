w = 8
h = 12

for i in range(min(w, h), 0, -1):
    if w % i == 0 and h % i == 0:
        divide = i
        break

w_div = int(w/divide)
h_div = int(h/divide)
last = (w_div - 1) * (h_div - 1)
answer = (w*h) - (((w_div * h_div) - last) * divide)