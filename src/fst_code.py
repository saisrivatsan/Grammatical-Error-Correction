import xml.etree.ElementTree as ET

#Reads the XML file and gets the required output
def parse_xml():
	tree = ET.parse('data/out.xml')
	root = tree.getroot()
	text_arr = []
	for tag in root.iter('hyp'):
		text_1 = tag.text;
		text_1= text_1.replace('"','')
		clean_text = text_1.replace('\n','')
		clean_text = clean_text.split()
		clean_text = [clean_text[i].split(',') for i in range(len(clean_text))]
		text_arr.append(clean_text)
	return text_arr

#Generates the Graph
def gen_graph(text_array):
	
	#Node[i] stores the word which is incident from i  
	#Graph stores the list of edges 

	Node = [[]]
	Graph = [] 

	file = open("data/ref.txt","r")
	input_text = file.readline()

	input_text = input_text.lower()
	input_text = input_text[0:-4]
	input_text = input_text.split()
	file.close()
	Node[0] = "<eps>"
	for i in range(0,len(input_text)):
		Node.append(input_text[i]);
		Graph.append(tuple([i,i+1]))
	Node.append("<end>")


	start_no = 0
	terminal_no = len(Node)-1

	BackBone = Node

	# Iterate over the list for creating the graph. We search for the Node in Backbone
	# in case of a match and the connect the edges accordingly, otherwise we create
	# a new Node
	for i in range(0,len(text_array)):
		prevNode = start_no
		for j in range(0,len(text_array[i])):
			if text_array[i][j][2]=='C':
				u=BackBone.index(text_array[i][j][1])
				Graph.append(tuple([prevNode,u]))
				prevNode = u
			else:
				if text_array[i][j][1]=='':
					continue;
				Node.append(text_array[i][j][1])
				Graph.append(tuple([prevNode,len(Node)-1]))
				prevNode = len(Node)-1
		Graph.append(tuple([prevNode,terminal_no]))
	return [Graph,Node]

#Generates the isyms and osyms file
def gen_isysms_and_osyms(Node):

	symsDict = {}
	syms = list(set(Node))
	for i in range(0,len(syms)):
		symsDict[syms[i]] = i
		
	isyms_file = open("data/fst.isyms","w")
	osyms_file = open("data/fst.osyms","w")
	for key in symsDict:
		isyms_file.write("%s %s\n"%(key,symsDict[key]))
		osyms_file.write("%s %s\n"%(key,symsDict[key]))
	isyms_file.close()
	osyms_file.close()

def gen_FST(Graph,Node):
	FST = []
	T = list(set(Graph))
	fst_file = open("data/fst.txt", "w")
	for edge in T:
		FST.append([edge[0],edge[1],Node[edge[0]],Node[edge[0]],Graph.count(edge)])
		fst_file.write("%s %s %s %s %s\n"%(edge[0],edge[1],Node[edge[0]],Node[edge[0]],Graph.count(edge)))   
	fst_file.close()
	    
def main():
	
	#Parse XML
	text_array = parse_xml()

	#Generate Graph
	[Graph,Node] = gen_graph(text_array)

	#Generate isyms and osyms
	gen_isysms_and_osyms(Node)
	print("\nISYMS and OSYMS generated")

	#To generate FST
	gen_FST(Graph,Node)
	print("FST generated\n")
	
if __name__ == "__main__":
    main()




