'''

#----------------------------------------------------------------------------------------------------------
#chromatic_imap_ext_impl.py     William K. Johnson 2013
#----------------------------------------------------------------------------------------------------------

'''

import chromatic_imap_ext
import sys
import datetime
import threading
import Ice
from utils.ice_python_utils import *


Ice.loadSlice( '-I' + str( Ice.getSliceDir() ) + ' --underscore ./chromatic_imap_ext.ice' )

constants = { 
             'default_domain'           : 'default -p 8000',
             'default_directory_name'   : 'root_dir' ,
             'application_str'          : 'chromatic_imap_file_system' ,
             'server_boilerplate'       : '--------------------------------------------------------------------------------------\n' +
                                          '\t\t   chromatic_imap_ext->internet communication engine\n' +
                                          '\t\t<debug prototype> 0.01 copyright Chromatic Universe 2013\n' +
                                          '--------------------------------------------------------------------------------------'        
            }


pyout = ostream()

'''---------------------------------------------------------------------------------------------------------'''
class chromatic_directory_i( chromatic_imap_ext.chromatic_directory ):
    
    #constructor and operations here...    
    def __init__( self , communicator , name , parent ):
        
        self._name = name
        self._parent = parent
        self._contents = []
        
        #create an identity. the parent has the fixed identity "root_dir"
        self.chromatic_id_dir = Ice.Identity()                
        if( self._parent ):
            self.chromatic_id_dir.name = Ice.generateUUID()
        else:
            self.chromatic_id_dir.name = constants['default_directory_name']   
            
        pyout << tstamp << 'chromatic_directory servant instantiated...' << endl 
            
         
    def __eq__( self , other ) :        
        
        if other == None:
            return False
        
        try:
            return self._name == other._name and self.parent == other.parent
        except AttributeError:
            return False    
        
    def __neq__( self , other ) :
        
        if other == None:
            return True
        
        try:
            return self._name != other._name or self.parent != other.parent
        except AttributeError:
            return True        
            
    def addChild( self, child ):
        
        self._contents.append( child )
        
    def name( self , current=None ):
        
        pyout << tstamp << 'listing directory contents...' << endl             
        return self._name
        
    def list( self, current=None ):
        
        return self._contents
    
    #add servant to ASM and parent's _contents map.
    def activate( self, a ):
        
        thisNode = chromatic_imap_ext.chromatic_directoryPrx.uncheckedCast( a.add( self, self.chromatic_id_dir ) )
        if self._parent:
            self._parent.addChild( thisNode )
            
    def __str__( self ):    
        return constants['server_boilerplate'] + '...directory...'

    __repr__ = __str__ 


'''---------------------------------------------------------------------------------------------------------'''    
class chromatic_file_i( chromatic_imap_ext.chromatic_file ):
    
    #constructor and operations here...
    _adapter = None
    
    def __init__( self , communicator , name , parent ):
        
        self._name = name
        self._parent = parent
        self._lines = []
        self._mutex = threading.Lock()
        
        assert( self._parent != None )
    
        #create an identity
        self.chromatic_id_file = Ice.Identity()
        self.chromatic_id_file.name = Ice.generateUUID()          
        
        
    def __eq__( self , other ) :
        
        if other == None:
            return False
        
        try:
            return self._name == other._name and self.parent == other.parent
        except AttributeError:
            return False    
        
    def __neq__( self , other ) :
        
        if other == None:
            return True
        
        try:
            return self._name != other._name and self.parent != other.parent
        except AttributeError:
            return True  
        
    def __str__( self ):    
        
        return constants['server_boilerplate'] + '...file...'

    __repr__ = __str__ 
    
    
    #add servant to ASM and parent's _contents map
    def activate( self , a ):
        
        thisNode = chromatic_imap_ext.chromatic_filePrx.uncheckedCast( a.add (self , self.chromatic_id_file ) )
        self._parent.addChild( thisNode )
        
    #virtual overrides
    def name( self , current=None ):
        
        return self._name        
    
    def read( self , current=None ):
        
        self._mutex.acquire()
        #copy the list
        lines = self._lines[:]
        self._mutex.release()
        
        return lines    
        
    def write( self , text , current=None ):
        
        self._mutex.acquire()
        self._lines = text
        self._mutex.release()
              
    
'''--------------------------------------------------------------------------------------------------------'''    
class chromatic_imap_ext_server( Ice.Application ):
    
    #ctor
    def __init__( self ):
        
        pyout << constants['server_boilerplate'] << endl
        self.domain_str = constants['default_domain']  
        
    #dtor   
    def __del__( self ):
        
         pass     
        
    #stream repr
    def __str__( self ):
        
        return 'chromatic_imap_ext->application->Internet Communication Engine server'
    
    __repr__ = __str__
    
    #upcall
    def run( self  , args ):
        
        try:
            
            pyout = ostream()
            
            #terminate cleanly on receipt of a signal
            self.shutdownOnInterrupt()
            
            #created an object adapter ( stored in the _adapter static members )
            adapter = self.communicator().createObjectAdapterWithEndpoints( constants['application_str'] ,
                                                                            constants['default_domain'] )
            
            #created the root directory ( with name "/" and no parent )
            root = chromatic_directory_i( self.communicator() , '/', None )
            root.activate( adapter )       
            
            pyout    << tstamp \
                     << 'initializing server at ' \
                     << self.server_domain_str \
                     << '....\n' \
                     << tstamp << 'created root directory....'\
                     << endl    
                 
            #created a file called "README" in the root directory
            file = chromatic_file_i( self.communicator(), 'README' , root )
            text = [ 'This file system contains a collection of poetry.' ]
            try:
                file.write( text )
            except  chromatic_imap_ext.chromatic_file_exception , e :
                pyout <<  e.reason << endl
                raise
            file.activate( adapter )        
            pyout << tstamp << 'created local README file at root......' << endl
            
            #created a directory called "coleridge" in the root directory        #
            coleridge = chromatic_directory_i( self.communicator() ,
                                               "coleridge" ,
                                               root )
            coleridge.activate( adapter )
            pyout << tstamp << 'created local directory at root......' << endl
            
            
            #created a file called "Kubla_Khan" in the coleridge directory
            file = chromatic_file_i( self.communicator() , "Kubla_Khan", coleridge )
            text = [ "In Xanadu did Kubla Khan",
                     "A stately pleasure-dome decree:",
                     "Where Alph, the sacred river, ran",
                     "Through caverns measureless to man",
                     "Down to a sunless sea." ]
            try:
                file.write( text )
            except chromatic_imap_ext.chromatic_file_exception , e :
                pyout <<  e.reason << endl
                raise
            file.activate( adapter )
            pyout << tstamp << 'created local file in directory->coleridge......' << endl
                 
            #all objects are created, allow client requests now        
            adapter.activate()
            
            
            #wait until we are done
            self.communicator().waitForShutdown()
            if self.interrupted():
                pyout << '\n' << tstamp << self.appName() << ': terminating....' << endl
                     
        except chromatic_imap_ext.chromatic_file_exception as e :        
            pyout << tstamp << 'file exception...'\
                  << e.reason \
                  << endl
        except Ice.Exception as e :
            pyout << tstamp << 'transport exception...'\
                  << e.reason \
                  << endl                
        except:        
            pyout << tstamp << 'unexpected error: '\
                  << sys.exc_info()[0]\
                  << endl 
            raise   
    
        finally:       
            pyout << tstamp << 'shutting down...' << endl
        
        return 0    
    
    '''--------------------------------------------------------------------------------------------------------'''
    #attributes 
    @property
    def server_domain_str( self ):
        return self.domain_str
    @property
    def log_directory_str( self ):
        return self.log_dir_str   
    


    
'''--------------------------------------------------------------------------------------------------------'''        
sys.stdout.flush()
app = chromatic_imap_ext_server()
sys.exit( app.main( sys.argv ) )      
    
