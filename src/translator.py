import urllib2
import goslate

def set_proxy_handler(http_proxy = None):
	if http_proxy is None:
		gs = goslate.Goslate()
		return gs;
	proxy_handler = urllib2.ProxyHandler({"http" : http_proxy})
	proxy_opener = urllib2.build_opener(urllib2.HTTPHandler(proxy_handler),urllib2.HTTPSHandler(proxy_handler))
	gs_with_proxy = goslate.Goslate(opener=proxy_opener)
	return gs_with_proxy

def write_ref(input_txt,language_set):
	f = open("data/ref.txt","w");
	n = len(language_set)
	for i in range(n):
		f.write(input_txt + " (" + str(i+1) + ")\n")
	f.close();

def write_hyp(input_txt,language_set,gs):
	f = open("data/hyp.txt","w");
	n = len(language_set)
	for i in range(n):
	    # Round tripconversion
	    translation = gs.translate(input_txt,language_set[i])
	    RT_trans = gs.translate(translation,"en")
	    RT_trans = RT_trans.replace('.'," .")
	    f.write(RT_trans + " (" + str(i+1) + ")\n")
	f.close();


def main():
	gs = set_proxy_handler("http://10.3.100.207:8080")
	input_txt = "I going to school for learning ."
	language_set = ['ta','de','fr','hi','it','es','zh','ru'];
	write_ref(input_txt,language_set)
	write_hyp(input_txt,language_set,gs)
		
if __name__ == "__main__":
    main()




