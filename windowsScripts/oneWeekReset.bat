#!\bin\bash

#resets all text files in order to run oneWeek test

cd ..

: > oneWeekTest\summary1.txt
: > oneWeekTest\summary2.txt
: > oneWeekTest\summary3.txt
: > oneDayTest\summary.txt
echo '0000000' > validAcctsListFile.txt
: > oneWeekTest\masterAccts.txt

cd windowsScripts
