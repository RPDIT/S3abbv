echo off
set arg=\gui.py
set filepath=%0\..\%arg%
FOR /f %%p  in ('where python') do SET PYTHONPATH=%%p
shift
%PYTHONPATH% %filepath%
pause