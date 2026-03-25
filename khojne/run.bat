@echo off
REM Khoj Sewa - Quick Start Script for Windows

title Khoj Sewa - Service Matching Platform

echo.
echo ============================================
echo   KHOJ SEWA - Quick Start
echo   Service Matching Platform for Nepal
echo ============================================
echo.

REM Check if virtual environment exists
if not exist ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
    call .venv\Scripts\activate.bat
    echo Installing dependencies...
    pip install -r requirements.txt
) else (
    echo Activating virtual environment...
    call .venv\Scripts\activate.bat
)

REM Run migrations
echo.
echo Running database migrations...
python manage.py migrate

REM Start server
echo.
echo ============================================
echo   SERVER STARTING...
echo ============================================
echo.
echo Open your browser and go to:
echo   http://127.0.0.1:8000/
echo.
echo Features:
echo   - User & Expert registration
echo   - Service request management
echo   - Google Maps with expert locations
echo   - 5-star rating system
echo   - Responsive design
echo.
echo Press Ctrl+C to stop the server
echo ============================================
echo.

python manage.py runserver 0.0.0.0:8000

pause
