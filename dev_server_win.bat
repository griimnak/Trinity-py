@echo off

:Launch
setlocal
%@Try%
    python3 local_server.py
%@EndTry%
:@Catch
    cls
    echo [DEV][INFO] `python3` is not a recognized command, falling back to `python` instead ..
    python dev_server.py
:@EndCatch
pause