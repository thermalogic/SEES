model Boiler "Boiler of Rankine Cycle"
  import Modelica.Media.Water.IF97_Utilities.h_pT;
  parameter Real p_in=16;
  parameter Real t_in=210;
  parameter Real p_out=16;
  parameter Real t_out=540;
  Real h_in;
  Real h_out;
  Real q "heat";
equation
  h_in = 0.001*h_pT(p_in*1000000,t_in + 273.15);
  h_out = 0.001*h_pT(p_out*100000,t_out + 273.15);
  q = h_out -h_in;
end Boiler;
