echo off
set arg=\s3abbv.py
set filepath=%0\..\%arg%
FOR /f %%p  in ('where python') do SET PYTHONPATH=%%p
shift
%PYTHONPATH% %filepath%
pause