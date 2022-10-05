from math import sqrt

N = 10
files = ['L=10', 'L=100', 'L=200', 'L=500', 'L=1000']
file = open('errors.txt', 'w')

for f in files:
    data = open(f, 'r')
    data_float = []
    
    for d in data: data_float.append(float(d))
    data.close()
    
    avg = sum(data_float) / N
    sum_ = 0
    for i in data_float: sum_ += (i - avg)**2
    s = sqrt(sum_ / N)
    error_ = sum_ / sqrt(N)

    file.write(f"{f} {'{0:.20f}'.format(error_)}\n")

file.close()