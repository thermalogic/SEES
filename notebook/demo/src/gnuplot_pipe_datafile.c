
#include <stdio.h>

int main (void)
{

    FILE *pipe = popen("gnuplot -persist", "w");  // Open a pipe to gnuplot

    if (pipe) {   // If gnuplot is found
      fprintf(pipe, "set term wx\n");         // set the terminal               
      fprintf(pipe, "set datafile separator ','\n"); //datafile separator ','
      fprintf(pipe, "set xlabel '|Force| (Newtons)'\n");
      fprintf(pipe, "set ylabel 'Distance (meters)'\n");
      fprintf(pipe, "set title 'Measured Displacement of Spring'\n");
      fprintf(pipe, "plot './demo/data/springData.csv' using  ($2*9.81):1 title '(Force,Distance)'\n");
      
      fflush(pipe); //flush pipe
      fprintf(pipe,"exit \n");   // exit gnuplot
      pclose(pipe);    //close pipe
    }
    return 0;
};
