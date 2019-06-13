@echo off
::设置要永久加入到path环境变量中的路径
set My_PATH=C:\Program Files\gnuplot\bin
 
set PATH=%PATH%;%My_PATH%
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v "Path" /t REG_EXPAND_SZ /d "%PATH%" /f
exit