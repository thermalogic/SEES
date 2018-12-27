set term wx   # set the terminal 
set datafile separator ',' # datafile separator ','
set multiplot layout 2,2 margins 0.1, 0.9, 0.1, 0.9 spacing .2
set xrange [0:20]
set yrange [2:14]

f(x) =a*x+b

set title "Anscombe1"
fit f(x) './demo/data/Anscombe.csv' using 1:2 via a,b
plot './demo/data/Anscombe.csv' using 1:2 title "" with points pt 7  lc rgb "blue",f(x) title "" lw 1 lc rgb "orange"
unset title


fit f(x) './demo/data/Anscombe.csv' using 3:4 via a,b
set title "Anscombe2"
plot './demo/data/Anscombe.csv' using 3:4 title "" with points pt 7  lc rgb "blue",f(x) title "" lw 1 lc rgb "orange"
unset title


fit f(x) './demo/data/Anscombe.csv' using 5:6 via a,b
set title "Anscombe3"    
plot './demo/data/Anscombe.csv' using 5:6 title "" with points pt 7  lc rgb "blue",f(x) title "" lw 1 lc rgb "orange"
unset title

b=3
fit f(x) './demo/data/Anscombe.csv' using 7:8 via a  # non b
set title "Anscombe4"
plot './demo/data/Anscombe.csv' using 7:8 title "" with points pt 7  lc rgb "blue",f(x) title "" lw 1 lc rgb "orange"
unset multiplot
