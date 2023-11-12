@echo off
if exist output rd output /s /q
pyinstaller setup.py --onefile
pyinstaller main.pyw --onefile
if not exist output md output
if exist dist\setup.exe if exist output move dist\setup.exe output
if exist dist\main.exe if exist output move dist\main.exe output
if exist dist rd dist /s /q
if exist build rd build /s /q
if exist *.spec del *.spec /q