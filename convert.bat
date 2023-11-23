@echo off
set "input_folder=dist\large"
set "output_folder=dist\png"

if not exist "%output_folder%" mkdir "%output_folder%"

for %%i in ("%input_folder%\*.svg") do (
  "C:\Program Files\Inkscape\bin\inkscape.exe" --export-type=png --export-filename="%output_folder%\%%~ni.png" "%%i"
)
