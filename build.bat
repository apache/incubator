@echo off

rem Change to containing directory. Allows script to be executed from explorer/IDEs
cd /d %~dp0

for %%i in (.\lib\*.jar) do call cpappend.bat %%i

echo CLASSPATH="%_CP%"

java -classpath "%_CP%" org.apache.tools.ant.Main -Dant.home=%_AH% %1 %2 %3

SET _CP=
