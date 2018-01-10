@echo off
title Trinity
color d

:Launch
setlocal
%@Try%
    python3 trinity_server.py
%@EndTry%
:@Catch
    cls
    echo $-'python3' not a command, using 'python' instead..
    python trinity_server.py
:@EndCatch
pause