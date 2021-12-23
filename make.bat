@echo off
pyinstaller src\main.py --windowed --clean --noconfirm --noupx ^
	--name writer ^
	--paths venv\Lib\site-packages ^
	--add-data "src\resources;resources" ^
	--add-data "LICENSE;."
pause
