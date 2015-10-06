SUBMISSION OF ASSIGNMENT-2 
COURSE : Language Processing for e-learning (ET61002)
----------------------------------------------------------------------------

NAME : SAI SRIVATSA R
ROLL NO : 12EE10059
DEPARTMENT OF ELECTRICAL ENGINEERING
IIT KHARAGPUR
Email : saisrivatsan12@gmail.com
Web : saisrivatsan.github.io

----------------------------------------------------------------------------
GRAMMATICAL ERROR CORRECTION BASED ON ROUND-TRIP MACHINE TRANSLATION (RTMT)
----------------------------------------------------------------------------

PRE-REQUISITES
--------------
1. OPENFST
LINK:http://www.openfst.org/twiki/bin/view/FST/FstDownload
2. TERCOM
(Installation not required)

INSTRUCTION FOR RUNNING THE CODE
--------------------------------

DEMO
----
1. From Terminal, run: cd Assignment-2/Data_and_Code/"
2. run: chmod +x ./fst.sh
3. run: ./fst.sh
4. Check the binary.pdf file for fst

Running with new data
---------------------
1. Place the incorrect sentence in ./Assignment-2/Data_and_Code/hyp.txt
2. Place the round trip machine translations in ./Assignment-2/Data_and_Code/ref.txt
3. Follow instructions in Demo

To obtain the shortestpath fst
------------------------------
1. From terminal, run: fstshortestpath [--shortest = $n] binary.fst shortest.fst
2. run: fstdraw --isymbols=fst.isyms --osymbols=fst.osyms shortest.fst shortest.dot
3. run dot -Tps shortest.dot >shortest.pdf


