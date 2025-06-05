@echo off
set
file = screenshot_%date:~-4,4%%date:~-10,2%%date:~-7,2%_%time:~0,2%%time:~3,2%%time:~
6,2%.png
powershell -command "Add-Type -AssemblyName System.Windows.Forms; Add-Type
-AssemblyName System.Drawing; $bmp = New-Object
System.Drawing.Bitmap([System.Windows.Forms.Screen]::PrimaryScreen.Bounds.Width,
[System.Windows.Forms.Screen]::PrimaryScreen.Bounds.Height); $graphics =
[System.Drawing.Graphics]::FromImage($bmp);
$graphics.CopyFromScreen(0,0,0,0,$bmp.Size); $bmp.Save('%cd%\%file%');"
echo Screenshot salva como %file%
pause