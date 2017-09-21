@echo off
title Trinity
color d

:Launch
setlocal
%@Try%
    python3 Core.py
%@EndTry%
:@Catch
    cls
    echo $-'python3' not a command, using 'python' instead..
    python Core.py
:@EndCatch
pause