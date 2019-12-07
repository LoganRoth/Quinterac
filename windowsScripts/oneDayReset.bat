#!\bin\bash

#resets all text files to needed values to run 1 day test

cd ..

: > oneDayTest\summary1.txt
: > oneDayTest\summary2.txt
: > oneDayTest\summary3.txt
: > oneDayTest\summary.txt
echo '1234567
7654321
0000000' > validAcctsListFile.txt
echo '7654321 000 aaa
1234567 20000 cba' > oneDayTest\masterAccts.txt

cd windowsScripts
