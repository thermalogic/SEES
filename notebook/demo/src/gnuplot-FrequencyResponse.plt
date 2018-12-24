
A(jw) = ({0,1}*jw/({0,1}*jw+p1)) * (1/(1+{0,1}*jw/p2))
p1 = 10
p2 = 10000
set term wx
set dummy jw
set grid x y2
set key default
set logscale xy
set log x2
unset log y2
set title "Amplitude and Phase Frequency Response"
set xlabel "jw (radians)"
set xrange [1.1 : 90000.0]
set x2range [1.1 : 90000.0]
set ylabel "magnitude of A(jw)"
set y2label "Phase of A(jw) (degrees)"
set ytics nomirror
set y2tics
set tics out
set autoscale  y
set autoscale y2
plot abs(A(jw)), 180/pi*arg(A(jw)) axes x2y2
