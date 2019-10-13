import os

filename1 = "links.txt"
filename2 = "names.txt"

class WgetDownloader(object):

    def open_files(self,filename1,filename2):
        '''Open files and read them into lists'''
        #open links file and read lines into list
        print("opening links file")
        with open(filename1) as f:
            links = f.read().splitlines()
            #print(links)
        #open names file and read lines into list
        print("opening name file")
        with open(filename2) as f:
            names = f.read().splitlines()
            #print(names)
        return names, links

    def clean_lists(self,names):
        '''clean the lists of strings'''
        #strip ['\\', '"', "'", '<', '>', '[',']',':','/','|', '?', '*']  from names
        print("stripping undesirable characters")
        #bad_characters = ['\\', '"', "'", '<', '>', '[',']',':','/','|', '?', '*']
        bad_characters = str.maketrans('\\"\'<>[]:/|?*.-', "______________")
        names = [x.translate(bad_characters) for x in names]
        #print(names)

    def check_len(self,list1, list2):
        #len of lists test
        if(len(list1)!=len(list2)):
            print("The length of the lists do not match. Check the data.")
            exit()

    def query_builder(self,names, links):
        #build query list
        queries = []
        print("building query list")
        for i in range(len(links)):
            folder_name = names[i]
            folder_name = '"' + folder_name + '"'
            link_name = links[i]
            init_query = "wget -E -H -k -K -p -e robots=off -nH -nd -P" + folder_name+ "\ "+ link_name
            queries.append(init_query)
            #print(init_query)
        #print(queries)

    def wget_execution(self,queries):
        #loop wget execution
        print("About to start looping")
        for i in range(len(queries)):
            os.system(queries[i])
            print("finished no.{} loop".format(i))
#exit
print("done")
#check if the number of queriees is the same as the number of links and names: