set term wx                # set the terminal               
set datafile separator ',' # datafile separator ','
set xlabel '|Force| (Newtons)'
set ylabel 'Distance (meters)'
set title 'Measured Displacement of Spring'
plot './demo/data/springData.csv' using ($2*9.81):1 title ""
