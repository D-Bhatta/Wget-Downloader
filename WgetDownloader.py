'''Downloads a list of links and stores them in folders from a list of folder names'''
class WgetDownloader(object):
    def __init__(self,filename1, filename2):
        self.filename1 = filename1
        self.filename2 = filename2
        self.names = []
        self.links = []
        self.queries = []
    def open_files(self):
        '''Open files and read them into lists'''

        #check if file is empty
        #
        #Define exceptions
        class Error(Exception):
            """Base class for other exceptions"""
            pass

        class FileIsEmptyError(Error):
            """Raised when file is empty"""
            pass

        #open links file and read lines into list
        print("opening links file")
        try:
            with open(self.filename1) as f:
                self.links = f.read().splitlines()
                if not self.links:
                    raise FileIsEmptyError("links.txt is empty")
                #print(self.links)
        except FileNotFoundError:
            print("file not found")
            self.exit_function(status=3)
        
        #open names file and read lines into list
        print("opening name file")
        try:
            with open(self.filename2) as f:
                self.names = f.read().splitlines()
                if not self.names:
                    raise FileIsEmptyError("names.txt is empty")
                #print(self.names)
        except FileNotFoundError:
            print("file not found")
            self.exit_function(status=3)
        



    def clean_lists(self):
        '''clean the lists of strings'''
        #strip ['\\', '"', "'", '<', '>', '[',']',':','/','|', '?', '*']  from names
        print("stripping undesirable characters")
        #bad_characters = ['\\', '"', "'", '<', '>', '[',']',':','/','|', '?', '*']
        bad_characters = str.maketrans('\\"\'<>[]:/|?*.-', "______________")
        self.names = [x.translate(bad_characters) for x in self.names]
        #print(self.names)

    def check_len(self):
        '''len of lists test'''
        if(len(self.names)!=len(self.links)):
            print("The length of the lists do not match. Check the data.",
            "names :{}".format(len(self.names)), 
            "links : {}".format(len(self.links)))
            self.exit_function(status=1)
    
    def check_list_empty(self):
        '''check if lists are empty'''
        if len(self.names)==0:
            print("The names list is empty")
            self.exit_function(status=1)
        if len(self.links)==0:
            print("The links list is empty")
            self.exit_function(status=1)

    def query_builder(self):
        '''build query list'''
        print("building query list")
        for i in range(len(self.links)):
            folder_name = self.names[i]
            folder_name = '"' + folder_name + '"'
            link_name = self.links[i]
            init_query = "wget -E -H -k -K -p -e robots=off -nH -nd -P" + folder_name+ "\ "+ link_name # pylint: disable=anomalous-backslash-in-string
            self.queries.append(init_query)
            #print(init_query)
        #print(queries)
        self.queries
    
    def check_network(self):
        '''check network connection'''
        class Error(Exception):
            "Base class for all errors"
            pass
        
        class NoInternetAvailableError(Error):
            "No internet connection is available"
            pass

        import socket

        def internet(host="8.8.8.8", port=53, timeout=3):
            """
            Host: 8.8.8.8 (google-public-dns-a.google.com)
            OpenPort: 53/tcp
            Service: domain (DNS/TCP)
            """
            try:
                socket.setdefaulttimeout(timeout)
                socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
                return True
            except socket.error as ex:
                print(ex)
                raise NoInternetAvailableError("No internet is available")
        
        try:
            internet_status = internet()
        except NoInternetAvailableError:        
            if internet_status() != True:
                print("Network not available. Cannot connect ot 8.8.8.8")
                self.exit_function(status=4)

    def wget_execution(self):
        '''executes the queries: calls wget with link and folder name along with flags"-E -H -k -K -p -e robots=off -nH -nd -P" and link is stored in folder'''

        #Define Exceptions
        class Error(Exception):
            """Base class for other exceptions"""
            pass

        class WgetError(Error):
            """Raised when wget can't execute the query and returned status is non-zero(!0)"""
            pass


        from os import system
        #loop wget execution
        print("About to start looping")
        for i in range(len(self.queries)):
            try:
                status = system(self.queries[i])
                print("finished no.{} loop".format(i))
                if status != 0:
                    raise WgetError("Wget error")
            except WgetError:
                print("Wget couldn't download the link and returned status {}".format(status))
        #check if the number of queriees is the same as the number of links and names
        print("expected loops:{}".format(len(self.queries)-1))
    
    def exit_function(self, status):
        '''exit'''
        from sys import exit
        if status == 0:
            print("done")
            exit(status)
        else:
            print("error as status is{}".format(status))
            exit(status)

    
    def download(self):
        '''downloads the files'''
        #get the lists
        self.open_files()
        #check if lists are empty
        self.check_list_empty()
        self.check_len()
        self.clean_lists()
        self.query_builder()
        self.check_network()
        self.wget_execution()
        self.exit_function(status=0)
        