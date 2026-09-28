@echo off
title ScareX - Pi Node Simulation (Local PC Dev)
echo ==========================================================
echo       Starting ScareX Pi Edge Node (Local Simulation)
echo ==========================================================
cd /d "%~dp0"
echo Launching Camera Server on port 8000...
start "ScareX Pi Camera Server" python -m raspberry_pi.camera_server
timeout /t 2 /nobreak >nul
echo Launching Command Server on port 9000...
start "ScareX Pi Command Server" python -m raspberry_pi.command_server
echo.
echo Pi Node Services are running!
echo Camera Stream: http://127.0.0.1:8000/video
echo Command API:   http://127.0.0.1:9000/command
echo.
pause
