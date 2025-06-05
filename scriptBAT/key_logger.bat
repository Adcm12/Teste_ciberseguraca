@echo off

setlocal enabledelayedexpansion

echo Keylogger simulado, iniciando... Digite 'exit' para sair.

:loop
set /p input=Digite algo:
if /i "!input!"=="exit" goto end
echo !input! >> key_log.txt
goto loop

:end
echo Keylogger finalizado. As entradas foram salvas em key_log.txt.
pause
