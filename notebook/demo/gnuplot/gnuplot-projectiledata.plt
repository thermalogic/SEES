set term wx                # set the terminal               
set xlabel 'Distance from Launch Point(inches)'
set ylabel 'Altitude of the Projectile(inches)'
set title 'Trajectory of Projectile'
plot './demo/data/projectileData.txt' using 1:2 title "trial1", \
     './demo/data/projectileData.txt' using 1:3 title "trial2", \
     './demo/data/projectileData.txt' using 1:4 title "trial3", \
     './demo/data/projectileData.txt' using 1:5 title "trial3"
