
# 1 Define a function with unknown parameters
#  k = F/x -> F=(1/k)*x, F=mass*9.81

d(x) = (1/k)*x

# 2 Fit the parameters with specified data
set datafile separator ',' # datafile separator ','
fit d(x) './demo/data/springData.csv' using ($2*9.81):1 via k    

set term wx    
set xlabel '|Force| (Newtons)'
set ylabel 'Distance (meters)'
set title 'Measured Displacement of Spring'
plot './demo/data/springData.csv' using  ($2*9.81):1 title '(Force,Distance)',\
     './demo/data/springData.csv' using ($2*9.81):(d($2*9.81)) title '',\
     './demo/data/springData.csv' using ($2*9.81):(d($2*9.81))  title 'Force=f(Distance)' with line ls 12
