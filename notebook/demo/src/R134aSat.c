#include <math.h>
#include "R134aSat.h"

PORT pSat(double t)
{
	const double ti[]={1,1.5,2.3,3.6,5.2,7.3};
    const double Ni[]={-7.6896400207782598, 2.0859760566425463, -2.6755347075503888,
                       0.3010493765467589, -5.8583601582059233, 3.4788072104059631};
    double Pcrit=4059280.0;
    double Tcrit=374.21;
    double Treduce=374.18;
    double summer=0,theta;
    double T=t+273.15;
    theta=1.0-T/Treduce;
    for (int i=0;i<=5;i++)
    {
        summer +=Ni[i]*pow(theta,ti[i]);
    }
    return  Pcrit*exp(summer*Tcrit/T)/1.0e6;
}
