@echo off
echo clearing Temp-Folder

Rem deletes everything in the Temps folder
cd %temp%
del * /f /q
