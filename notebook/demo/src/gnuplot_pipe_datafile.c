
#include <stdio.h>

int main (void)
{

    FILE *pipe = popen("gnuplot -persist", "w");  // Open a pipe to gnuplot

    if (pipe) {   // If gnuplot is found
      fprintf(pipe, "set term wx\n");         // set the terminal               
      fprintf(pipe, "set datafile separator ','\n"); //datafile separator ','
      fprintf(pipe, "set xlabel 'Distances'\n");
      fprintf(pipe, "set ylabel 'Mass'\n");
      fprintf(pipe, "set title 'Observable'\n");
      fprintf(pipe, "plot './demo/data/springData.csv' using 1:2 title 'Mass=f(Distance)-' \n");

    fflush(pipe); //flush pipe

    fprintf(pipe,"exit \n");   // exit gnuplot
    pclose(pipe);    //close pipe
    }
    return 0;
};
