#include <math.h>
#include "R134aSat.h"

double pSat(double t)
{
    // p = pc*exp(Tc/T*sum(n_i*theta^t_i))
	const double ti[]={0.845,0.99,1.14,2.651,4.507,17.235};
    const double Ni[]={0.4331478287291047, -9.090302559074352, 2.1476074125217703,
                      -1.557687007603464,  -3.5020328972698604, 14.958442337201044};
    double Pcrit=4059280.0;
    double Tcrit=374.21;
    double Treduce=374.21;
    double summer=0,theta;
    double T=t+273.15;
    int i;
    theta=1.0-T/Treduce;
    for (i=0;i<=5;i++)
    {
        summer += Ni[i]*pow(theta,ti[i]);
    }
    return Pcrit*exp((Tcrit/T)*summer)/1.0e6;
}
