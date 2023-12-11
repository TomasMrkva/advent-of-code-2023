from math import prod

sol = lambda time, distance: sum(i * (time - i) > distance for i in range(1, time + 1))

vals_pt_a = [(52, 426), (94, 1374), (75, 1279), (94, 1216)]
print(prod((sol(t, d)) for (t, d) in vals_pt_a))

vals_pt_b = (52947594, 426137412791216)
print(sol(*vals_pt_b))