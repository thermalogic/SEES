model VCRR134a
  import R134a = Modelica.Media.R134a.R134a_ph;

  type SpecificEnthalpy=Real(unit="kJ/kg",displayUnit="kJ/kg");
  type SpecificEntropy =Real(unit="kJ/(kg.K)",displayUnit="kJ/(kg.K)");
  type Pressure =Real(unit="MPa",displayUnit="MPa");
  type Temperature =Real(unit="° C",displayUnit="° C");
  type FlowRateofMass=Real(unit="kg/s",displayUnit="kg/s");
  type Work=Real(unit="kW",displayUnit="kW");
  type RefrigerationCapacity=Real(unit="ton",displayUnit="ton");
  type CoefficientofPerformance=Real;


  SpecificEnthalpy h1,h2,h3,h4 "Specific enthalpy";
  SpecificEntropy s1,s2 "Specific entropy";
  Pressure p1,p2,p3;
  Work wc;
  RefrigerationCapacity ql;
  CoefficientofPerformance cop;

  parameter FlowRateofMass mdot=0.08;
  parameter Temperature t1=0,t3=26;

equation
  //state 1
  p1=R134a.saturationPressure(t1+273.15)/1.0e6;
  h1=R134a.specificEnthalpy(R134a.setState_Tx(t1+273.15,1))/1000;
  s1=R134a.specificEntropy(R134a.setState_Tx(t1+273.15,1))/1000;

  //state 3
  p3=R134a.saturationPressure(t3+273.15)/1.0e6;
  h3=R134a.specificEnthalpy(R134a.setState_Tx(t3+273.15,0))/1000;

  //state 2
  p2=p3;
  s2=s1;
  h2=R134a.specificEnthalpy_ps(p2*1.0e6,s2*1000)/1000;

  //state 4
  h4=h3;

  // The compressor work
  wc=mdot*(h2-h1);

  // The refrigeration capacity in tons
  ql=mdot*(h1-h4)*60*(1/211);

  //The coefficient of performance
  cop=(h1-h4)/(h2-h1);
end VCRR134a;
