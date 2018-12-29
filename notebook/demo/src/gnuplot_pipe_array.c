
#include <stdio.h>
#include <gsl/gsl_fit.h>

int main (void)
{
  int n = 11;
  double x[11] = {10.0, 8.0, 13.0, 9.0, 11.0,
                  14.0 ,6.0, 4.0 , 12.0,7.0,5.0};
  double y[11] = {8.04, 6.95,7.68, 8.81, 8.33,
                  9.96, 7.24,4.26,10.84, 4.82,5.68 };

  double c0, c1, cov00, cov01, cov11, sumsq;

  gsl_fit_linear(x, 1, y, 1, n,
                 &c0, &c1, &cov00, &cov01, &cov11,
                 &sumsq);

  printf ("best fit: Y = %g + %g X\n", c0, c1);
  printf ("covariance matrix:\n");
  printf ("[ %g, %g\n  %g, %g]\n", cov00, cov01, cov01, cov11);
  printf ("sumsq = %g\n", sumsq);
  printf ("\n");
  
  // plot
  FILE *pipe = popen("gnuplot -persist", "w"); // Open a pipe to gnuplot
  if (pipe) // If gnuplot is found
  { 
     fprintf(pipe, "set term wx\n");         // set the terminal
     fprintf(pipe, "set xlabel 'X'\n");
     fprintf(pipe, "set ylabel 'Y'\n");
     fprintf(pipe, "set xrange [0:20]\n");
     fprintf(pipe, "set yrange [2:14]\n");
     fprintf(pipe, "set title '<X,Y> and Linear fit:y=%.4f*x+%.4f'\n",c1,c0);
      
     /* In this case, the datafile is written directly to the gnuplot pipe with no need for a temporary file.
           The special filename '-' specifies that the data are inline; i.e., they follow the command.
        1 sending gnuplot the plot '-' command 
        2 followed by data points 
        3 followed by the letter "e" 
     */
     
     // 1 sending gnuplot the plot '-' command
     fprintf(pipe, "plot '-' title '<x,y>' with points  pt 7 lc rgb 'blue',\
                         '-' title 'Line' with  linespoints  pt  6 lc rgb 'red'\n");
     
     // 2 followed by data points: <x,y>
     for (int i = 0; i < n; i++)
     {
        fprintf(pipe, "%lf %lf\n", x[i], y[i]);
     }
     // 3 followed by the letter "e" 
     fprintf(pipe, "e");
     
     // linear fit
     fprintf(pipe,"\n"); // start a new draw item
     fprintf(pipe, "%lf %lf\n", 0.0, c0+c1*0,0);
     for (int i = 0; i < n; i++)
     {
        fprintf(pipe, "%lf %lf\n", x[i], c0+c1*x[i]);
     }
     fprintf(pipe, "%lf %lf\n", 20.0,c0+c1*20,0);
     fprintf(pipe, "e");
      
     fflush(pipe);
     fprintf(pipe, "exit \n"); // exit gnuplot
     pclose(pipe);             //close pipe
  }
  
  return 0;
}
