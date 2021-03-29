@echo off

echo Instalador de Servidores de Minecraft
echo MCSSTools v0.0.0.4-Alpha por NGDPL Nk
echo --------------------------------------

:tipo
echo(
set /P c=Escribe el tipo de Servidor que deseas instalar (Snapshot/Stable)= 
if /I "%c%" EQU "SNAPSHOT" goto :snapshot
if /I "%c%" EQU "STABLE" goto :stable
goto :tiponull

:tiponull
echo(
echo Ese tipo de Server es incorrecto o no se encuentra disponible
set /P c=Vuelve a escribir el tipo de Servidor que deseas instalar (Snapshot/Stable)= 
if /I "%c%" EQU "SNAPSHOT" goto :snapshot
if /I "%c%" EQU "STABLE" goto :stable
goto :tiponull

:stable
echo ---------------------------------------------
echo(
echo Has seleccionado un Servidor de tipo Stable
:stableyn
echo(
set /P c=Es ese el tipo de Servidor que deseas instalar? [S/N]= 
if /I "%c%" EQU "S" goto :stabley
if /I "%c%" EQU "N" goto :tipo
goto :stableyn

:stabley
echo ---------------------------------------------
echo(
echo Perfecto, es un Servidor tipo Stable
:stableversion
echo(
set /P c=Escribe la Version de Minecraft Stable para la que estara dedicado tu nuevo Servidor= 
if /I "%c%" EQU "1.2.1" goto :1.2.1
if /I "%c%" EQU "1.2.2" goto :1.2.2
if /I "%c%" EQU "1.2.3" goto :1.2.3
if /I "%c%" EQU "1.2.4" goto :1.2.4
if /I "%c%" EQU "1.2.5" goto :1.2.5
if /I "%c%" EQU "1.3.1" goto :1.3.1
if /I "%c%" EQU "1.3.2" goto :1.3.2
if /I "%c%" EQU "1.4.2" goto :1.4.2
if /I "%c%" EQU "1.4.4" goto :1.4.4
if /I "%c%" EQU "1.4.5" goto :1.4.5
if /I "%c%" EQU "1.4.6" goto :1.4.6
if /I "%c%" EQU "1.4.7" goto :1.4.7
if /I "%c%" EQU "1.5.1" goto :1.5.1
if /I "%c%" EQU "1.5.2" goto :1.5.2
if /I "%c%" EQU "1.6.1" goto :1.6.1
if /I "%c%" EQU "1.6.2" goto :1.6.2
if /I "%c%" EQU "1.6.4" goto :1.6.4
if /I "%c%" EQU "1.7.2" goto :1.7.2
if /I "%c%" EQU "1.7.3" goto :1.7.3
if /I "%c%" EQU "1.7.4" goto :1.7.4
if /I "%c%" EQU "1.7.5" goto :1.7.5
if /I "%c%" EQU "1.7.6" goto :1.7.6
if /I "%c%" EQU "1.7.7" goto :1.7.7
if /I "%c%" EQU "1.7.8" goto :1.7.8
if /I "%c%" EQU "1.7.9" goto :1.7.9
if /I "%c%" EQU "1.7.10" goto :1.7.10
if /I "%c%" EQU "1.8" goto :1.8
if /I "%c%" EQU "1.8.1" goto :1.8.1
if /I "%c%" EQU "1.8.2" goto :1.8.2
if /I "%c%" EQU "1.8.3" goto :1.8.3
if /I "%c%" EQU "1.8.4" goto :1.8.4
if /I "%c%" EQU "1.8.5" goto :1.8.5
if /I "%c%" EQU "1.8.6" goto :1.8.6
if /I "%c%" EQU "1.8.7" goto :1.8.7
if /I "%c%" EQU "1.8.8" goto :1.8.8
if /I "%c%" EQU "1.8.9" goto :1.8.9
if /I "%c%" EQU "1.9" goto :1.9
if /I "%c%" EQU "1.9.1" goto :1.9.1
if /I "%c%" EQU "1.9.2" goto :1.9.2
if /I "%c%" EQU "1.9.3" goto :1.9.3
if /I "%c%" EQU "1.9.4" goto :1.9.4
if /I "%c%" EQU "1.10" goto :1.10
if /I "%c%" EQU "1.10.1" goto :1.10.1
if /I "%c%" EQU "1.10.2" goto :1.10.2
if /I "%c%" EQU "1.11" goto :1.11
if /I "%c%" EQU "1.11.1" goto :1.11.1
if /I "%c%" EQU "1.11.2" goto :1.11.2
if /I "%c%" EQU "1.12" goto :1.12
if /I "%c%" EQU "1.12.1" goto :1.12.1
if /I "%c%" EQU "1.12.2" goto :1.12.2
if /I "%c%" EQU "1.13" goto :1.13
if /I "%c%" EQU "1.13.1" goto :1.13.1
if /I "%c%" EQU "1.13.2" goto :1.13.2
if /I "%c%" EQU "1.14" goto :1.14
if /I "%c%" EQU "1.14.1" goto :1.14.1
if /I "%c%" EQU "1.14.2" goto :1.14.2
if /I "%c%" EQU "1.14.3" goto :1.14.3
if /I "%c%" EQU "1.14.4" goto :1.14.4
if /I "%c%" EQU "1.15" goto :1.15
if /I "%c%" EQU "1.15.1" goto :1.15.1
if /I "%c%" EQU "1.15.2" goto :1.15.2
if /I "%c%" EQU "1.16" goto :1.16
if /I "%c%" EQU "1.16.1" goto :1.16.1
if /I "%c%" EQU "1.16.2" goto :1.16.2
if /I "%c%" EQU "1.16.3" goto :1.16.3
if /I "%c%" EQU "1.16.4" goto :1.16.4
if /I "%c%" EQU "1.16.5" goto :1.16.5
goto :stablenull

:stablenull
echo(
echo Esa Version no esta disponible, es incorrecta o no corresponde a una de tipo Stable
set /P c=Vuelve a escribir la Version de Minecraft Stable para la que estara dedicado tu nuevo Servidor= 
if /I "%c%" EQU "1.2.1" goto :1.2.1
if /I "%c%" EQU "1.2.2" goto :1.2.2
if /I "%c%" EQU "1.2.3" goto :1.2.3
if /I "%c%" EQU "1.2.4" goto :1.2.4
if /I "%c%" EQU "1.2.5" goto :1.2.5
if /I "%c%" EQU "1.3.1" goto :1.3.1
if /I "%c%" EQU "1.3.2" goto :1.3.2
if /I "%c%" EQU "1.4.2" goto :1.4.2
if /I "%c%" EQU "1.4.4" goto :1.4.4
if /I "%c%" EQU "1.4.5" goto :1.4.5
if /I "%c%" EQU "1.4.6" goto :1.4.6
if /I "%c%" EQU "1.4.7" goto :1.4.7
if /I "%c%" EQU "1.5.1" goto :1.5.1
if /I "%c%" EQU "1.5.2" goto :1.5.2
if /I "%c%" EQU "1.6.1" goto :1.6.1
if /I "%c%" EQU "1.6.2" goto :1.6.2
if /I "%c%" EQU "1.6.4" goto :1.6.4
if /I "%c%" EQU "1.7.2" goto :1.7.2
if /I "%c%" EQU "1.7.3" goto :1.7.3
if /I "%c%" EQU "1.7.4" goto :1.7.4
if /I "%c%" EQU "1.7.5" goto :1.7.5
if /I "%c%" EQU "1.7.6" goto :1.7.6
if /I "%c%" EQU "1.7.7" goto :1.7.7
if /I "%c%" EQU "1.7.8" goto :1.7.8
if /I "%c%" EQU "1.7.9" goto :1.7.9
if /I "%c%" EQU "1.7.10" goto :1.7.10
if /I "%c%" EQU "1.8" goto :1.8
if /I "%c%" EQU "1.8.1" goto :1.8.1
if /I "%c%" EQU "1.8.2" goto :1.8.2
if /I "%c%" EQU "1.8.3" goto :1.8.3
if /I "%c%" EQU "1.8.4" goto :1.8.4
if /I "%c%" EQU "1.8.5" goto :1.8.5
if /I "%c%" EQU "1.8.6" goto :1.8.6
if /I "%c%" EQU "1.8.7" goto :1.8.7
if /I "%c%" EQU "1.8.8" goto :1.8.8
if /I "%c%" EQU "1.8.9" goto :1.8.9
if /I "%c%" EQU "1.9" goto :1.9
if /I "%c%" EQU "1.9.1" goto :1.9.1
if /I "%c%" EQU "1.9.2" goto :1.9.2
if /I "%c%" EQU "1.9.3" goto :1.9.3
if /I "%c%" EQU "1.9.4" goto :1.9.4
if /I "%c%" EQU "1.10" goto :1.10
if /I "%c%" EQU "1.10.1" goto :1.10.1
if /I "%c%" EQU "1.10.2" goto :1.10.2
if /I "%c%" EQU "1.11" goto :1.11
if /I "%c%" EQU "1.11.1" goto :1.11.1
if /I "%c%" EQU "1.11.2" goto :1.11.2
if /I "%c%" EQU "1.12" goto :1.12
if /I "%c%" EQU "1.12.1" goto :1.12.1
if /I "%c%" EQU "1.12.2" goto :1.12.2
if /I "%c%" EQU "1.13" goto :1.13
if /I "%c%" EQU "1.13.1" goto :1.13.1
if /I "%c%" EQU "1.13.2" goto :1.13.2
if /I "%c%" EQU "1.14" goto :1.14
if /I "%c%" EQU "1.14.1" goto :1.14.1
if /I "%c%" EQU "1.14.2" goto :1.14.2
if /I "%c%" EQU "1.14.3" goto :1.14.3
if /I "%c%" EQU "1.14.4" goto :1.14.4
if /I "%c%" EQU "1.15" goto :1.15
if /I "%c%" EQU "1.15.1" goto :1.15.1
if /I "%c%" EQU "1.15.2" goto :1.15.2
if /I "%c%" EQU "1.16" goto :1.16
if /I "%c%" EQU "1.16.1" goto :1.16.1
if /I "%c%" EQU "1.16.2" goto :1.16.2
if /I "%c%" EQU "1.16.3" goto :1.16.3
if /I "%c%" EQU "1.16.4" goto :1.16.4
if /I "%c%" EQU "1.16.5" goto :1.16.5
goto :stablenull

:1.2.1
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://assets.minecraft.net/1_2/minecraft_server.jar >C:\MCSSTools\NeededFiles\Server_1.2.1.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.2.1.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.2.2
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://assets.minecraft.net/1_2/minecraft_server.jar >C:\MCSSTools\NeededFiles\Server_1.2.2.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.2.2.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.2.3
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://assets.minecraft.net/1_2/minecraft_server.jar >C:\MCSSTools\NeededFiles\Server_1.2.3.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.2.3.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.2.4
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://assets.minecraft.net/1_2_5/minecraft_server.jar >C:\MCSSTools\NeededFiles\Server_1.2.4.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.2.4.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.2.5
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/d8321edc9470e56b8ad5c67bbd16beba25843336/server.jar >C:\MCSSTools\NeededFiles\Server_1.2.5.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.2.5.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.3.1
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/82563ce498bfc1fc8a2cb5bf236f7da86a390646/server.jar >C:\MCSSTools\NeededFiles\Server_1.3.1.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.3.1.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.3.2
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/3de2ae6c488135596e073a9589842800c9f53bfe/server.jar >C:\MCSSTools\NeededFiles\Server_1.3.2.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.3.2.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.4.2
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/5be700523a729bb78ef99206fb480a63dcd09825/server.jar >C:\MCSSTools\NeededFiles\Server_1.4.2.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.4.2.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.4.3
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/9be68adf6e80721975df12f2445fa24617328d18/server.jar >C:\MCSSTools\NeededFiles\Server_1.4.3.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.4.3.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.4.4
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/4215dcadb706508bf9d6d64209a0080b9cee9e71/server.jar >C:\MCSSTools\NeededFiles\Server_1.4.4.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.4.4.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.4.5
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/c12fd88a8233d2c517dbc8196ba2ae855f4d36ea/server.jar >C:\MCSSTools\NeededFiles\Server_1.4.5.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.4.5.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.4.6
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/a0aeb5709af5f2c3058c1cf0dc6b110a7a61278c/server.jar >C:\MCSSTools\NeededFiles\Server_1.4.6.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.4.6.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.4.7
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/2f0ec8efddd2f2c674c77be9ddb370b727dec676/server.jar >C:\MCSSTools\NeededFiles\Server_1.4.7.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.4.7.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.5.1
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/d07c71ee2767dabb79fb32dad8162e1b854d5324/server.jar >C:\MCSSTools\NeededFiles\Server_1.5.1.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.5.1.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.5.2
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/f9ae3f651319151ce99a0bfad6b34fa16eb6775f/server.jar >C:\MCSSTools\NeededFiles\Server_1.5.2.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.5.2.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.6.1
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/0252918a5f9d47e3c6eb1dfec02134d1374a89b4/server.jar >C:\MCSSTools\NeededFiles\Server_1.6.1.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.6.1.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.6.2
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/01b6ea555c6978e6713e2a2dfd7fe19b1449ca54/server.jar >C:\MCSSTools\NeededFiles\Server_1.6.2.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.6.2.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.6.4
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/050f93c1f3fe9e2052398f7bd6aca10c63d64a87/server.jar >C:\MCSSTools\NeededFiles\Server_1.6.4.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.6.4.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.7.2
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/3716cac82982e7c2eb09f83028b555e9ea606002/server.jar >C:\MCSSTools\NeededFiles\Server_1.7.2.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.7.2.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.7.3
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/707857a7bc7bf54fe60d557cca71004c34aa07bb/server.jar >C:\MCSSTools\NeededFiles\Server_1.7.3.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.7.3.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.7.4
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/61220311cef80aecc4cd8afecd5f18ca6b9461ff/server.jar >C:\MCSSTools\NeededFiles\Server_1.7.4.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.7.4.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.7.5
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/e1d557b2e31ea881404e41b05ec15c810415e060/server.jar >C:\MCSSTools\NeededFiles\Server_1.7.5.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.7.5.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.7.6
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/41ea7757d4d7f74b95fc1ac20f919a8e521e910c/server.jar >C:\MCSSTools\NeededFiles\Server_1.7.6.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.7.6.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.7.7
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/a6ffc1624da980986c6cc12a1ddc79ab1b025c62/server.jar >C:\MCSSTools\NeededFiles\Server_1.7.7.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.7.7.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.7.8
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/c69ebfb84c2577661770371c4accdd5f87b8b21d/server.jar >C:\MCSSTools\NeededFiles\Server_1.7.8.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.7.8.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.7.9
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/4cec86a928ec171fdc0c6b40de2de102f21601b5/server.jar >C:\MCSSTools\NeededFiles\Server_1.7.9.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.7.9.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.7.10
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/952438ac4e01b4d115c5fc38f891710c4941df29/server.jar >C:\MCSSTools\NeededFiles\Server_1.7.10.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.7.10.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.8
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/a028f00e678ee5c6aef0e29656dca091b5df11c7/server.jar >C:\MCSSTools\NeededFiles\Server_1.8.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.8.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.8.1
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/68bfb524888f7c0ab939025e07e5de08843dac0f/server.jar >C:\MCSSTools\NeededFiles\Server_1.8.1.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.8.1.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.8.2
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/a37bdd5210137354ed1bfe3dac0a5b77fe08fe2e/server.jar >C:\MCSSTools\NeededFiles\Server_1.8.2.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.8.2.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.8.3
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/163ba351cb86f6390450bb2a67fafeb92b6c0f2f/server.jar >C:\MCSSTools\NeededFiles\Server_1.8.3.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.8.3.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.8.4
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/dd4b5eba1c79500390e0b0f45162fa70d38f8a3d/server.jar >C:\MCSSTools\NeededFiles\Server_1.8.4.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.8.4.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.8.5
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/ea6dd23658b167dbc0877015d1072cac21ab6eee/server.jar >C:\MCSSTools\NeededFiles\Server_1.8.5.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.8.5.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.8.6
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/2bd44b53198f143fb278f8bec3a505dad0beacd2/server.jar >C:\MCSSTools\NeededFiles\Server_1.8.6.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.8.6.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.8.7
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/35c59e16d1f3b751cd20b76b9b8a19045de363a9/server.jar >C:\MCSSTools\NeededFiles\Server_1.8.7.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.8.7.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.8.8
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/5fafba3f58c40dc51b5c3ca72a98f62dfdae1db7/server.jar >C:\MCSSTools\NeededFiles\Server_1.8.8.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.8.8.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.8.9
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/b58b2ceb36e01bcd8dbf49c8fb66c55a9f0676cd/server.jar >C:\MCSSTools\NeededFiles\Server_1.8.9.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.8.9.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.9
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/b4d449cf2918e0f3bd8aa18954b916a4d1880f0d/server.jar >C:\MCSSTools\NeededFiles\Server_1.9.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.9.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.9.1
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/bf95d9118d9b4b827f524c878efd275125b56181/server.jar >C:\MCSSTools\NeededFiles\Server_1.9.1.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.9.1.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.9.2
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/2b95cc7b136017e064c46d04a5825fe4cfa1be30/server.jar >C:\MCSSTools\NeededFiles\Server_1.9.2.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.9.2.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.9.3
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/8e897b6b6d784f745332644f4d104f7a6e737ccf/server.jar >C:\MCSSTools\NeededFiles\Server_1.9.3.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.9.3.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.9.4
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/edbb7b1758af33d365bf835eb9d13de005b1e274/server.jar >C:\MCSSTools\NeededFiles\Server_1.9.4.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.9.4.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.10
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/a96617ffdf5dabbb718ab11a9a68e50545fc5bee/server.jar >C:\MCSSTools\NeededFiles\Server_1.10.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.10.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.10.1
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/cb4c6f9f51a845b09a8861cdbe0eea3ff6996dee/server.jar >C:\MCSSTools\NeededFiles\Server_1.10.1.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.10.1.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.10.2
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/3d501b23df53c548254f5e3f66492d178a48db63/server.jar >C:\MCSSTools\NeededFiles\Server_1.10.2.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.10.2.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.11
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/48820c84cb1ed502cb5b2fe23b8153d5e4fa61c0/server.jar >C:\MCSSTools\NeededFiles\Server_1.11.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.11.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.11.1
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/1f97bd101e508d7b52b3d6a7879223b000b5eba0/server.jar >C:\MCSSTools\NeededFiles\Server_1.11.1.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.11.1.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.11.2
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/f00c294a1576e03fddcac777c3cf4c7d404c4ba4/server.jar >C:\MCSSTools\NeededFiles\Server_1.11.2.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.11.2.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.12
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/8494e844e911ea0d63878f64da9dcc21f53a3463/server.jar >C:\MCSSTools\NeededFiles\Server_1.12.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.12.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.12.1
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/561c7b2d54bae80cc06b05d950633a9ac95da816/server.jar >C:\MCSSTools\NeededFiles\Server_1.12.1.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.12.1.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.12.2
echo ---------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/886945bfb2b978778c3a0288fd7fab09d315b25f/server.jar >C:\MCSSTools\NeededFiles\Server_1.12.2.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.12.2.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.13
echo --------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/d0caafb8438ebd206f99930cfaecfa6c9a13dca0/server.jar >C:\MCSSTools\NeededFiles\Server_1.13.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.13.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.13.1
echo --------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/fe123682e9cb30031eae351764f653500b7396c9/server.jar >C:\MCSSTools\NeededFiles\Server_1.13.1.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.13.1.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.13.2
echo --------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/3737db93722a9e39eeada7c27e7aca28b144ffa7/server.jar >C:\MCSSTools\NeededFiles\Server_1.13.2.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.13.2.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.14
echo --------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/f1a0073671057f01aa843443fef34330281333ce/server.jar >C:\MCSSTools\NeededFiles\Server_1.14.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.14.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.14.1
echo --------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/ed76d597a44c5266be2a7fcd77a8270f1f0bc118/server.jar >C:\MCSSTools\NeededFiles\Server_1.14.1.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.14.1.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.14.2
echo --------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/808be3869e2ca6b62378f9f4b33c946621620019/server.jar >C:\MCSSTools\NeededFiles\Server_1.14.2.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.14.2.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.14.3
echo --------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/d0d0fe2b1dc6ab4c65554cb734270872b72dadd6/server.jar >C:\MCSSTools\NeededFiles\Server_1.14.3.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.14.3.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.14.4
echo --------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/3dc3d84a581f14691199cf6831b71ed1296a9fdf/server.jar >C:\MCSSTools\NeededFiles\Server_1.14.4.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.14.4.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.15
echo --------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/e9f105b3c5c7e85c7b445249a93362a22f62442d/server.jar >C:\MCSSTools\NeededFiles\Server_1.15.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.15.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.15.1
echo --------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/4d1826eebac84847c71a77f9349cc22afd0cf0a1/server.jar >C:\MCSSTools\NeededFiles\Server_1.15.1.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.15.1.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.15.2
echo --------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/bb2b6b1aefcd70dfd1892149ac3a215f6c636b07/server.jar >C:\MCSSTools\NeededFiles\Server_1.15.2.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.15.2.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.16
echo --------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/a0d03225615ba897619220e256a266cb33a44b6b/server.jar >C:\MCSSTools\NeededFiles\Server_1.16.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.16.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.16.1
echo --------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/a412fd69db1f81db3f511c1463fd304675244077/server.jar >C:\MCSSTools\NeededFiles\Server_1.16.1.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.16.1.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.16.2
echo --------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/c5f6fb23c3876461d46ec380421e42b289789530/server.jar >C:\MCSSTools\NeededFiles\Server_1.16.2.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.16.2.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.16.3
echo --------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/f02f4473dbf152c23d7d484952121db0b36698cb/server.jar >C:\MCSSTools\NeededFiles\Server_1.16.3.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.16.3.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.16.4
echo --------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/35139deedbd5182953cf1caa23835da59ca3d7cd/server.jar >C:\MCSSTools\NeededFiles\Server_1.16.4.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.16.4.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

:1.16.5
echo --------------------------------------------
echo(
echo Se descargaran los archivos necesarios desde Internet
echo Luego se creara una carpeta en el Escritorio con los archivos de tu Servidor
pause
echo(
echo Espera un momento...
cd C:\
mkdir MCSSTools
cd C:\MCSSTools
mkdir NeededFiles
curl https://launcher.mojang.com/v1/objects/1b557e7b033b583cd9f66746b7a9ab1ec1673ced/server.jar >C:\MCSSTools\NeededFiles\Server_1.16.5.jar
cd %USERPROFILE%\Desktop
mkdir Servidor
copy C:\MCSSTools\NeededFiles\Server_1.16.5.jar %USERPROFILE%\Desktop\Servidor\
curl https://server.properties >C:\MCSSTools\NeededFiles\server.properties
copy C:\MCSSTools\NeededFiles\server.properties %USERPROFILE%\Desktop\Servidor\
rd /s /q C:\MCSSTools
goto :listo

REM Desde aquí comienza el listado de Versiones correspondientes a Snapshot
REM Esta anotación está hecha con el fin de hacer más ordenado este proceso y poder identificar de manera más fácil esta separación de contenido

:snapshot
echo ---------------------------------------------
echo(
echo Has seleccionado un Servidor de tipo Snapshot
:snapshotyn
echo(
set /P c=Es ese el tipo de Servidor que deseas instalar? [S/N]= 
if /I "%c%" EQU "S" goto :snapshoty
if /I "%c%" EQU "N" goto :tipo
goto :snapshotyn

:snapshoty
echo ---------------------------------------------
echo(
echo Perfecto, es un Servidor tipo Snapshot
:snapshotversion
echo(
set /P c=Escribe la Version de Minecraft Snapshot para la que estara dedicado tu nuevo Servidor= 
if /I "%c%" EQU "1.3" goto :1.3
if /I "%c%" EQU "1.4" goto :1.4
if /I "%c%" EQU "1.4.1" goto :1.4.1
if /I "%c%" EQU "1.4.3" goto :1.4.3
if /I "%c%" EQU "1.5" goto :1.5
if /I "%c%" EQU "13w16a" goto :13w16a
if /I "%c%" EQU "13w16b" goto :13w16b
if /I "%c%" EQU "13w17a" goto :13w17a
if /I "%c%" EQU "13w18a" goto :13w18a
if /I "%c%" EQU "13w18b" goto :13w18b
if /I "%c%" EQU "13w18c" goto :13w18c
if /I "%c%" EQU "13w19a" goto :13w19a
if /I "%c%" EQU "13w21a" goto :13w21a
if /I "%c%" EQU "13w21b" goto :13w21b
if /I "%c%" EQU "13w22a" goto :13w22a
if /I "%c%" EQU "13w23a" goto :13w23a
if /I "%c%" EQU "13w23b" goto :13w23b
if /I "%c%" EQU "13w24a" goto :13w24a
if /I "%c%" EQU "13w24b" goto :13w24b
if /I "%c%" EQU "13w25a" goto :13w25a
if /I "%c%" EQU "13w25b" goto :13w25b
if /I "%c%" EQU "13w25c" goto :13w25c
if /I "%c%" EQU "13w26a" goto :13w26a
if /I "%c%" EQU "1.6" goto :1.6
if /I "%c%" EQU "13w36a" goto :13w36a
if /I "%c%" EQU "13w36b" goto :13w36b
if /I "%c%" EQU "13w37a" goto :13w37a
if /I "%c%" EQU "13w37b" goto :13w37b
if /I "%c%" EQU "1.6.3" goto :1.6.3
if /I "%c%" EQU "13w38a" goto :13w38a
if /I "%c%" EQU "13w38b" goto :13w38b
if /I "%c%" EQU "13w38c" goto :13w38c
if /I "%c%" EQU "13w39a" goto :13w39a
if /I "%c%" EQU "13w39b" goto :13w39b
if /I "%c%" EQU "13w41a" goto :13w41a
if /I "%c%" EQU "13w41b" goto :13w41b
if /I "%c%" EQU "13w42a" goto :13w42a
if /I "%c%" EQU "13w42b" goto :13w42b
if /I "%c%" EQU "13w43a" goto :13w43a
if /I "%c%" EQU "1.7" goto :1.7
if /I "%c%" EQU "1.7.1" goto :1.7.1
if /I "%c%" EQU "13w47a" goto :13w47a
if /I "%c%" EQU "13w47b" goto :13w47b
if /I "%c%" EQU "13w47c" goto :13w47c
if /I "%c%" EQU "13w47d" goto :13w47d
if /I "%c%" EQU "13w47e" goto :13w47e
if /I "%c%" EQU "13w48a" goto :13w48a
if /I "%c%" EQU "13w48b" goto :13w48b
if /I "%c%" EQU "13w49a" goto :13w49a
if /I "%c%" EQU "14w02a" goto :14w02a
if /I "%c%" EQU "14w02b" goto :14w02b
if /I "%c%" EQU "14w02c" goto :14w02c
if /I "%c%" EQU "14w03a" goto :14w03a
if /I "%c%" EQU "14w03b" goto :14w03b
if /I "%c%" EQU "14w04a" goto :14w04a
if /I "%c%" EQU "14w04b" goto :14w04b
if /I "%c%" EQU "14w05a" goto :14w05a
if /I "%c%" EQU "14w05b" goto :14w05b
if /I "%c%" EQU "14w06a" goto :14w06a
if /I "%c%" EQU "14w06b" goto :14w06b
if /I "%c%" EQU "14w07a" goto :14w07a
if /I "%c%" EQU "14w08a" goto :14w08a
if /I "%c%" EQU "14w10a" goto :14w10a
if /I "%c%" EQU "14w10b" goto :14w10b
if /I "%c%" EQU "14w10c" goto :14w10c
if /I "%c%" EQU "1.7.6-pre1" goto :1.7.6-pre1
if /I "%c%" EQU "1.7.6-pre2" goto :1.7.6-pre2
if /I "%c%" EQU "14w11a" goto :14w11a
if /I "%c%" EQU "14w11b" goto :14w11b
if /I "%c%" EQU "14w17a" goto :14w17a
if /I "%c%" EQU "14w18a" goto :14w18a
if /I "%c%" EQU "14w18b" goto :14w18b
if /I "%c%" EQU "14w19a" goto :14w19a
if /I "%c%" EQU "1.7.10-pre1" goto :1.7.10-pre1
if /I "%c%" EQU "1.7.10-pre2" goto :1.7.10-pre2
if /I "%c%" EQU "1.7.10-pre3" goto :1.7.10-pre3
if /I "%c%" EQU "1.7.10-pre4" goto :1.7.10-pre4
if /I "%c%" EQU "14w20a" goto :14w20a
if /I "%c%" EQU "14w20b" goto :14w20b
if /I "%c%" EQU "14w21a" goto :14w21a
if /I "%c%" EQU "14w21b" goto :14w21b
if /I "%c%" EQU "14w25a" goto :14w25a
if /I "%c%" EQU "14w25b" goto :14w25b
if /I "%c%" EQU "14w26a" goto :14w26a
if /I "%c%" EQU "14w26b" goto :14w26b
if /I "%c%" EQU "14w26c" goto :14w26c
if /I "%c%" EQU "14w27a" goto :14w27a
if /I "%c%" EQU "14w27b" goto :14w27b
if /I "%c%" EQU "14w28a" goto :14w28a
if /I "%c%" EQU "14w28b" goto :14w28b
if /I "%c%" EQU "14w29a" goto :14w29a
if /I "%c%" EQU "14w29b" goto :14w29b
if /I "%c%" EQU "14w30a" goto :14w30a
if /I "%c%" EQU "14w30b" goto :14w30b
if /I "%c%" EQU "14w30c" goto :14w30c
if /I "%c%" EQU "14w31a" goto :14w31a
if /I "%c%" EQU "14w32a" goto :14w32a
if /I "%c%" EQU "14w32b" goto :14w32b
if /I "%c%" EQU "14w32c" goto :14w32c
if /I "%c%" EQU "14w32d" goto :14w32d
if /I "%c%" EQU "14w33a" goto :14w33a
if /I "%c%" EQU "14w33b" goto :14w33b
if /I "%c%" EQU "14w33c" goto :14w33c
if /I "%c%" EQU "14w34a" goto :14w34a
if /I "%c%" EQU "14w34b" goto :14w34b
if /I "%c%" EQU "14w34c" goto :14w34c
if /I "%c%" EQU "14w34d" goto :14w34d
if /I "%c%" EQU "1.8-pre1" goto :1.8-pre1
if /I "%c%" EQU "1.8-pre2" goto :1.8-pre2
if /I "%c%" EQU "1.8-pre3" goto :1.8-pre3
if /I "%c%" EQU "1.8.1-pre1" goto :1.8.1-pre1
if /I "%c%" EQU "1.8.1-pre2" goto :1.8.1-pre2
if /I "%c%" EQU "1.8.1-pre3" goto :1.8.1-pre3
if /I "%c%" EQU "1.8.1-pre4" goto :1.8.1-pre4
if /I "%c%" EQU "1.8.1-pre5" goto :1.8.1-pre5
if /I "%c%" EQU "1.8.2-pre1" goto :1.8.2-pre1
if /I "%c%" EQU "1.8.2-pre2" goto :1.8.2-pre2
if /I "%c%" EQU "1.8.2-pre3" goto :1.8.2-pre3
if /I "%c%" EQU "1.8.2-pre4" goto :1.8.2-pre4
if /I "%c%" EQU "1.8.2-pre5" goto :1.8.2-pre5
if /I "%c%" EQU "1.8.2-pre6" goto :1.8.2-pre6
if /I "%c%" EQU "1.8.2-pre7" goto :1.8.2-pre7
if /I "%c%" EQU "15w14a" goto :15w14a
if /I "%c%" EQU "15w31a" goto :15w31a
if /I "%c%" EQU "15w31b" goto :15w31b
if /I "%c%" EQU "15w31c" goto :15w31c
if /I "%c%" EQU "15w32a" goto :15w32a
if /I "%c%" EQU "15w32b" goto :15w32b
if /I "%c%" EQU "15w32c" goto :15w32c
if /I "%c%" EQU "15w33a" goto :15w33a
if /I "%c%" EQU "15w33b" goto :15w33b
if /I "%c%" EQU "15w33c" goto :15w33c
if /I "%c%" EQU "15w34a" goto :15w34a
if /I "%c%" EQU "15w34b" goto :15w34b
if /I "%c%" EQU "15w34c" goto :15w34c
if /I "%c%" EQU "15w34d" goto :15w34d
if /I "%c%" EQU "15w35a" goto :15w35a
if /I "%c%" EQU "15w35b" goto :15w35b
if /I "%c%" EQU "15w35c" goto :15w35c
if /I "%c%" EQU "15w35d" goto :15w35d
if /I "%c%" EQU "15w35e" goto :15w35e
if /I "%c%" EQU "15w36a" goto :15w36a
if /I "%c%" EQU "15w36b" goto :15w36b
if /I "%c%" EQU "15w36c" goto :15w36c
if /I "%c%" EQU "15w36d" goto :15w36d
if /I "%c%" EQU "15w37a" goto :15w37a
if /I "%c%" EQU "15w38a" goto :15w38a
if /I "%c%" EQU "15w38b" goto :15w38b
if /I "%c%" EQU "15w39a" goto :15w39a
if /I "%c%" EQU "15w39b" goto :15w39b
if /I "%c%" EQU "15w39c" goto :15w39c
if /I "%c%" EQU "15w40a" goto :15w40a
if /I "%c%" EQU "15w40b" goto :15w40b
if /I "%c%" EQU "15w41a" goto :14w41a
if /I "%c%" EQU "15w41b" goto :15w41b
if /I "%c%" EQU "15w42a" goto :15w42a
if /I "%c%" EQU "15w43a" goto :15w43a
if /I "%c%" EQU "15w43b" goto :15w43b
if /I "%c%" EQU "15w43c" goto :15w43c
if /I "%c%" EQU "15w44a" goto :15w44a
if /I "%c%" EQU "15w44b" goto :15w44b
if /I "%c%" EQU "15w45a" goto :15w45a
if /I "%c%" EQU "15w46a" goto :15w46a
if /I "%c%" EQU "15w47a" goto :15w47a
if /I "%c%" EQU "15w47b" goto :15w47b
if /I "%c%" EQU "15w49a" goto :15w49b
if /I "%c%" EQU "15w50a" goto :15w50a
if /I "%c%" EQU "15w51a" goto :15w51a
if /I "%c%" EQU "15w51b" goto :15w51b
if /I "%c%" EQU "16w02a" goto :16w02a
if /I "%c%" EQU "16w03a" goto :16w03a
if /I "%c%" EQU "16w04a" goto :16w04a
if /I "%c%" EQU "16w05a" goto :16w05a
if /I "%c%" EQU "16w05b" goto :16w05b
if /I "%c%" EQU "16w06a" goto :16w06a
if /I "%c%" EQU "16w07a" goto :16w07a
if /I "%c%" EQU "16w07b" goto :16w07b
if /I "%c%" EQU "1.9-pre1" goto :1.9-pre1
if /I "%c%" EQU "1.9-pre2" goto :1.9-pre2
if /I "%c%" EQU "1.9-pre3" goto :1.9-pre3
if /I "%c%" EQU "1.9-pre4" goto :1.9-pre4
if /I "%c%" EQU "1.9.1-pre1" goto :1.9.1-pre1
if /I "%c%" EQU "1.9.1-pre2" goto :1.9.1-pre2
if /I "%c%" EQU "1.9.1-pre3" goto :1.9.1-pre3
if /I "%c%" EQU "1.RV-Pre1" goto :1.RV-Pre1
if /I "%c%" EQU "16w14a" goto :16w14a
if /I "%c%" EQU "16w15a" goto :16w15a
if /I "%c%" EQU "16w15b" goto :16w15b
if /I "%c%" EQU "1.9.3-pre1" goto :1.9.3-pre1
if /I "%c%" EQU "1.9.3-pre2" goto :1.9.3-pre2
if /I "%c%" EQU "1.9.3-pre3" goto :1.9.3-pre3
if /I "%c%" EQU "16w20a" goto :16w20a
if /I "%c%" EQU "16w21a" goto :16w21a
if /I "%c%" EQU "16w21b" goto :16w21b
if /I "%c%" EQU "1.10-pre1" goto :1.10-pre1
if /I "%c%" EQU "1.10-pre2" goto :1.10-pre2
if /I "%c%" EQU "16w32a" goto :16w32a
if /I "%c%" EQU "16w32b" goto :16w32b
if /I "%c%" EQU "16w33a" goto :16w33a
if /I "%c%" EQU "16w35a" goto :16w35a
if /I "%c%" EQU "16w36a" goto :16w36a
if /I "%c%" EQU "16w38a" goto :16w38a
if /I "%c%" EQU "16w39a" goto :16w39a
if /I "%c%" EQU "16w39b" goto :16w39b
if /I "%c%" EQU "16w39c" goto :16w39c
if /I "%c%" EQU "16w40a" goto :16w40a
if /I "%c%" EQU "16w41a" goto :16w41a
if /I "%c%" EQU "16w42a" goto :16w42a
if /I "%c%" EQU "16w43a" goto :16w43a
if /I "%c%" EQU "16w44a" goto :16w44a
if /I "%c%" EQU "1.11-pre1" goto :1.11-pre1
if /I "%c%" EQU "16w50a" goto :16w50a
if /I "%c%" EQU "17w06a" goto :17w06a
if /I "%c%" EQU "17w13a" goto :17w13a
if /I "%c%" EQU "17w13b" goto :17w13b
if /I "%c%" EQU "17w14a" goto :17w14a
if /I "%c%" EQU "17w15a" goto :17w15a
if /I "%c%" EQU "17w16a" goto :17w16a
if /I "%c%" EQU "17w16b" goto :17w16b
if /I "%c%" EQU "17w17a" goto :17w17a
if /I "%c%" EQU "17w17b" goto :17w17b
if /I "%c%" EQU "17w18a" goto :17w18a
if /I "%c%" EQU "17w18b" goto :17w18b
if /I "%c%" EQU "1.12-pre1" goto :1.12-pre1
if /I "%c%" EQU "1.12-pre2" goto :1.12-pre2
if /I "%c%" EQU "1.12-pre3" goto :1.12-pre3
if /I "%c%" EQU "1.12-pre4" goto :1.12-pre4
if /I "%c%" EQU "1.12-pre5" goto :1.12-pre5
if /I "%c%" EQU "1.12-pre6" goto :1.12-pre6
if /I "%c%" EQU "1.12-pre7" goto :1.12-pre7
if /I "%c%" EQU "17w31a" goto :17w31a
if /I "%c%" EQU "1.12.1-pre1" goto :1.12.1-pre1
if /I "%c%" EQU "1.12.2-pre1" goto :1.12.2-pre1
if /I "%c%" EQU "1.12.2-pre2" goto :1.12.2-pre2
if /I "%c%" EQU "17w43a" goto :17w43a
if /I "%c%" EQU "17w43b" goto :17w43b
if /I "%c%" EQU "17w45a" goto :17w45a
if /I "%c%" EQU "17w45b" goto :17w45b
if /I "%c%" EQU "17w46a" goto :17w46a
if /I "%c%" EQU "17w47a" goto :17w47a
if /I "%c%" EQU "17w47b" goto :17w47b
if /I "%c%" EQU "17w48a" goto :17w48a
if /I "%c%" EQU "17w49a" goto :17w49a
if /I "%c%" EQU "17w49b" goto :17w49b
if /I "%c%" EQU "17w50a" goto :17w50a
if /I "%c%" EQU "18w01a" goto :18w01a
if /I "%c%" EQU "18w02a" goto :18w02a
if /I "%c%" EQU "18w03a" goto :18w03a
if /I "%c%" EQU "18w03b" goto :18w03b
if /I "%c%" EQU "18w05a" goto :18w05a
if /I "%c%" EQU "18w06a" goto :18w06a
if /I "%c%" EQU "18w07a" goto :18w07a
if /I "%c%" EQU "18w07b" goto :18w07b
if /I "%c%" EQU "18w07c" goto :18w07c
if /I "%c%" EQU "18w08a" goto :18w08a
if /I "%c%" EQU "18w08b" goto :18w08b
if /I "%c%" EQU "18w09a" goto :18w09a
if /I "%c%" EQU "18w10a" goto :18w10a
if /I "%c%" EQU "18w10b" goto :18w10b
if /I "%c%" EQU "18w10c" goto :18w10c
if /I "%c%" EQU "18w10d" goto :18w10d
if /I "%c%" EQU "18w11a" goto :18w11a
if /I "%c%" EQU "18w14a" goto :18w14a
if /I "%c%" EQU "18w14b" goto :18w14b
if /I "%c%" EQU "18w15a" goto :18w15a
if /I "%c%" EQU "18w16a" goto :18w16a
if /I "%c%" EQU "18w19a" goto :18w19a
if /I "%c%" EQU "18w19b" goto :18w19b
if /I "%c%" EQU "18w20a" goto :18w20a
if /I "%c%" EQU "18w20b" goto :18w20b
if /I "%c%" EQU "18w20c" goto :18w20c
if /I "%c%" EQU "18w21a" goto :18w21a
if /I "%c%" EQU "18w21b" goto :18w21b
if /I "%c%" EQU "18w22a" goto :18w22a
if /I "%c%" EQU "18w22b" goto :18w22b
if /I "%c%" EQU "18w22c" goto :18w22c
if /I "%c%" EQU "1.13-pre1" goto :1.13-pre1
if /I "%c%" EQU "1.13-pre2" goto :1.13-pre2
if /I "%c%" EQU "1.13-pre3" goto :1.13-pre3
if /I "%c%" EQU "1.13-pre4" goto :1.13-pre4
if /I "%c%" EQU "1.13-pre5" goto :1.13-pre5
if /I "%c%" EQU "1.13-pre6" goto :1.13-pre6
if /I "%c%" EQU "1.13-pre7" goto :1.13-pre7
if /I "%c%" EQU "1.13-pre8" goto :1.13-pre8
if /I "%c%" EQU "1.13-pre9" goto :1.13-pre9
if /I "%c%" EQU "1.13-pre10" goto :1.13-pre10
if /I "%c%" EQU "18w30a" goto :18w30a
if /I "%c%" EQU "18w30b" goto :18w30b
if /I "%c%" EQU "18w31a" goto :18w31a
if /I "%c%" EQU "18w32a" goto :18w32a
if /I "%c%" EQU "18w33a" goto :18w33a
if /I "%c%" EQU "1.13.1-pre1" goto :1.13.1-pre1
if /I "%c%" EQU "1.13.1-pre2" goto :1.13.1-pre2
if /I "%c%" EQU "1.13.2-pre1" goto :1.13.2-pre1
if /I "%c%" EQU "1.13.2-pre2" goto :1.13.2-pre2
if /I "%c%" EQU "18w43a" goto :18w43a
if /I "%c%" EQU "18w43b" goto :18w43b
if /I "%c%" EQU "18w43c" goto :18w43c
if /I "%c%" EQU "18w44a" goto :18w44a
if /I "%c%" EQU "18w45a" goto :18w45a
if /I "%c%" EQU "18w46a" goto :18w46a
if /I "%c%" EQU "18w47a" goto :18w47a
if /I "%c%" EQU "18w47b" goto :18w47b
if /I "%c%" EQU "18w48a" goto :18w48a
if /I "%c%" EQU "18w48b" goto :18w48b
if /I "%c%" EQU "18w49a" goto :18w49a
if /I "%c%" EQU "18w50a" goto :18w50a
if /I "%c%" EQU "19w02a" goto :19w03a
if /I "%c%" EQU "19w03a" goto :19w03a
if /I "%c%" EQU "19w03b" goto :19w03b
if /I "%c%" EQU "19w03c" goto :19w03c
if /I "%c%" EQU "19w04a" goto :19w04a
if /I "%c%" EQU "19w04b" goto :19w04b
if /I "%c%" EQU "19w05a" goto :19w05a
if /I "%c%" EQU "19w06a" goto :19w06a
if /I "%c%" EQU "19w07a" goto :19w07a
if /I "%c%" EQU "19w08a" goto :19w08a
if /I "%c%" EQU "19w08b" goto :19w08b
if /I "%c%" EQU "19w09a" goto :19w09a
if /I "%c%" EQU "19w11a" goto :19w11a
if /I "%c%" EQU "19w11b" goto :19w11b
if /I "%c%" EQU "19w12a" goto :19w12a
if /I "%c%" EQU "19w12b" goto :19w12b
if /I "%c%" EQU "19w13a" goto :19w13a
if /I "%c%" EQU "19w13b" goto :19w13b
if /I "%c%" EQU "3D Shareware v1.34" goto :3D Shareware v1.34

REM Desde aquí comienza el proceso post-descarga y copia a directorios específicos de los archivos, independientemente de su versión.
REM Esta anotación está hecha con el fin de hacer más ordenado este proceso y poder identificar de manera más fácil esta separación de contenido

:listo
echo -------------------------------------------
echo(
echo Se han descargado todos los archivos necesarios.
:listo.1
echo Te invitamos a leer el CLUF (o EULA) en el siguiente link
echo(
echo https://account.mojang.com/documents/minecraft_eula
echo(
set /P c=Cuando lo hayas leido, escribe "ACEPTO" para poder continuar= 
if /I "%c%" EQU "ACEPTO" goto :eula
goto :listo.1

:eula
cd %USERPROFILE%\Desktop\Servidor\
echo eula=true>eula.txt
goto :preconfig

:preconfig
echo -------------------------------------------
echo(
echo Ahora debes configurar los parametros de tu Servidor. Se abrira un Bloc de Notas.
echo Cuando lo cierres, tu Servidor estara configurado y listo para ser iniciado.
echo Se recomienda visitar la Wiki que explica detalladamente cada uno de los parametros disponibles
echo(
echo https://minecraft.fandom.com/wiki/Server.properties
echo(
pause
cd %USERPROFILE%\Desktop\Servidor\
server.properties
echo --------------------------------------------
echo(
echo Listo, ya tienes instalado tu nuevo Servidor
echo Recuerda cambiar el nombre o la ubicacion de la carpeta de tu Servidor
echo --------------------------------------------
echo(
echo Muchas Gracias por usar esta Herramienta
echo MIT License - Copyright 2021 NGDPL Nk.
echo --------------------------------------------
pause
exit