echo off
set arg1=%1
set arg2=%~dp0
set arg3=\s3abbv.py
set filepath=%0\..\%arg3%
FOR /f %%p  in ('where python') do SET PYTHONPATH=%%p
shift
%PYTHONPATH% %filepath%
pause