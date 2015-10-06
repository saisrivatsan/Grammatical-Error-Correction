import os

execfile('src/translator.py')
os.system('java -jar TERCOM/tercom.jar -r data/ref.txt -h data/hyp.txt -o xml -n data/out')
execfile('src/fst_code.py')
os.system('fstcompile --isymbols=data/fst.isyms --osymbols=data/fst.osyms data/fst.txt data/binary.fst')
os.system('fstdraw --isymbols=data/fst.isyms --osymbols=data/fst.osyms data/binary.fst data/binary.dot')
os.system('dot -Tps data/binary.dot > data/binary.pdf')


