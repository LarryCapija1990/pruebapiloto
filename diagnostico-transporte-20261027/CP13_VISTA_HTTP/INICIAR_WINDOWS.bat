@echo off
cd /d "%~dp0"
where py >nul 2>nul
if errorlevel 1 (python INICIAR.py) else (py INICIAR.py)
pause
