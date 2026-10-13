@echo off
setlocal
cd /d "%~dp0"
echo Setting up Course Compass in its own Python environment...
where py >nul 2>nul
if %errorlevel%==0 (
    py -3 -m venv .venv
) else (
    python -m venv .venv
)
if errorlevel 1 (
    echo.
    echo Could not create the virtual environment. Install Python 3 and try again.
    pause
    exit /b 1
)
".venv\Scripts\python.exe" -m ensurepip --upgrade
if errorlevel 1 (
    echo Could not prepare pip. Please repair/reinstall Python and try again.
    pause
    exit /b 1
)
".venv\Scripts\python.exe" -m pip install --upgrade pip
if errorlevel 1 goto install_failed
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 goto install_failed
echo.
echo Setup complete. Double-click run_windows.bat to start Course Compass.
pause
exit /b 0
:install_failed
echo.
echo Dependency installation failed. Check the error above and your internet connection.
pause
exit /b 1
