@echo off
echo leere Temp-Ordner

Rem deletes everything in the Temps folder
cd %temp%
del * /f /q
