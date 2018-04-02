@echo off
title Trinity
color d

:Launch
setlocal
%@Try%
    python3 local_server.py
%@EndTry%
:@Catch
    cls
    echo 'python3' not a command, using 'python' instead..
    python local_server.py
:@EndCatch
pause