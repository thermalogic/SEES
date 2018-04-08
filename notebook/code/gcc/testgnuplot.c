
#include <stdio.h>

int main (void)
{

    FILE *gnuplotPipe = popen("gnuplot -persist", "w");  // Open a pipe to gnuplot

    if (gnuplotPipe) {   // If gnuplot is found
      fprintf(gnuplotPipe, "set datafile separator ','\n"); //datafile separator ','
      fprintf(gnuplotPipe, "set xlabel 'Distances'\n");
      fprintf(gnuplotPipe, "set ylabel 'Mass'\n");
      fprintf(gnuplotPipe, "set title 'Observable'\n");
      fprintf(gnuplotPipe, "plot './src/springData.csv' using 1:2 title 'Mass=f(Distance)-' \n");

    fflush(gnuplotPipe); //flush pipe

    fprintf(gnuplotPipe,"exit \n");   // exit gnuplot
    pclose(gnuplotPipe);    //close pipe
                 }
    return 0;
};