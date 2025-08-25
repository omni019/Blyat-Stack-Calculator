@echo off
:: Enable ANSI escape codes
for /f "tokens=2 delims==" %%I in ('"prompt $E"') do set "ESC=%%I"

:: Define colors
set "RED=%ESC%[91m"
set "GREEN=%ESC%[92m"
set "YELLOW=%ESC%[93m"
set "BLUE=%ESC%[94m"
set "MAGENTA=%ESC%[95m"
set "CYAN=%ESC%[96m"
set "RESET=%ESC%[0m"

:: Intro
echo %CYAN%
echo =====================================================
echo 🔧 BLYAT STACK CALCULATOR - INSTALLER 🔧
echo =====================================================
echo %MAGENTA%Created by Omni019
echo %MAGENTA%Website: omni019.rf.gd
echo %MAGENTA%Guns.lol: guns.lol/omni019
echo %RESET%
echo.

:: Step 1: Install PyInstaller
echo %YELLOW%Step 1: Installing PyInstaller...%RESET%
pip install pyinstaller

:: Step 2: Build the EXE
echo.
echo %YELLOW%Step 2: Compiling Blyat Stack Calculator...%RESET%
python -m PyInstaller ^
  --onefile ^
  --windowed ^
  --name "Blyat Stack Calculator" ^
  --icon "shulker.ico" ^
  --add-data "background.png;." ^
  --add-data "gunslol.png;." ^
  --add-data "shulker.ico;." ^
  --add-data "shulker.png;." ^
  --distpath . ^
  --workpath .\.build ^
  --specpath . ^
  main.py

:: Optional Cleanup
echo.
echo %YELLOW%Cleaning up build files...%RESET%
rd /s /q .build
del Blyat Stack Calculator.spec

:: Outro
echo.
echo %GREEN%
echo =====================================================
echo ✅ INSTALLATION COMPLETE!
echo Your EXE is ready: Blyat Stack Calculator.exe
echo =====================================================
echo %RESET%
pause
start "" "Blyat Stack Calculator.exe"