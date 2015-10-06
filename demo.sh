#!/bin/bash
python src/translator.py
java -jar TERCOM/tercom.jar -r data/ref.txt -h data/hyp.txt -o xml -n data/out
python data/fst_code.py
fstcompile --isymbols=fst.isyms --osymbols=fst.osyms fst.txt binary.fst
fstdraw --isymbols=fst.isyms --osymbols=fst.osyms binary.fst binary.dot
dot -Tps binary.dot >binary.pdf
echo "Complete. Check binary.pdf"

