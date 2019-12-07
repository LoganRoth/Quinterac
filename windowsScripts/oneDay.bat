#!\bin\bash

#script simulates one working day for the quinterac banking system
#Ensure oneDayReset is run before running this

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

echo 'login
machine
deposit
1234567
20000
logout' | python3 -m frontend validAcctsListFile.txt oneDayTest\summary1.txt

echo 'login
machine
withdraw
1234567
10000
transfer
1234567
30000
7654321
logout' | python3 -m frontend validAcctsListFile.txt oneDayTest\summary2.txt

echo 'login
agent
createacct
8888888
abc
deposit
7654321
20000
deleteacct
1234567
cba
logout' | python3 -m frontend validAcctsListFile.txt oneDayTest\summary3.txt

type oneDayTest\summary1.txt oneDayTest\summary2.txt oneDayTest\summary3.txt > oneDayTest\summary.txt

python3 -m backoffice oneDayTest\masterAccts.txt oneDayTest\summary.txt oneDayTest\masterAccts.txt validAcctsListFile.txt

cd windowsScripts
