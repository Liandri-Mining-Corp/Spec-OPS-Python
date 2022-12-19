@echo off
title Boost

Rem attemps to implement Powerplan
powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61 > NUL 2>NUL

for /f "tokens=4" %%a in ('powercfg -list ^| findstr " (<guid>) Ultimative Leistung"') do (set "guid=%%a")
powercfg -setactive %guid%

Rem adds Registrykey to boost Start up time
echo Optimiere Startzeit
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Serialize" /v StartupDelayInMSec /t reg_dword /d 0x0 /f

Rem adds Registrykey to improve the Taskbar
echo Optimiere Taskleiste
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v ExtendedUIHoverTime /t reg_dword /d 0x2 /f

taskkill /IM explorer.exe /F > NUL 2>NUL
start explorer.exe