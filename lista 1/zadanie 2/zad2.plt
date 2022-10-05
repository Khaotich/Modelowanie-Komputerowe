set terminal png size 1024,1024 

set output "results.png"
set xlabel "Pokolenie"
set ylabel "Żywe komórki"
plot "p=0.1" with lines, "p=0.3" with lines, "p=0.6" with lines, "p=0.75" with lines, "p=0.8" with lines