'''

#----------------------------------------------------------------------------------------------------------
#chromatic_imap_client_impl.py     William K. Johnson 2013
#----------------------------------------------------------------------------------------------------------

'''

import chromatic_imap_ext
import sys
import traceback
import datetime
import threading
import Ice
from utils.ice_python_utils import *


constants = { 
             'default_domain'           : 'default -p 10000',
             'default_directory_name'   : 'root_dir' ,
             'application_str'          : 'chromatic_imap_file_system' ,
             'client_boilerplate'       : '--------------------------------------------------------------------------------------\n' +
                                          '\t\t   chromatic_imap_client->internet communication engine\n' +
                                          '\t\t<debug prototype> 0.01 copyright Chromatic Universe 2013\n' +
                                          '--------------------------------------------------------------------------------------'        
            }

pyout = ostream()   

'''---------------------------------------------------------------------------------------------------------'''
class chromatic_ice_client( Ice.Application ):
    
    #constructor and operations here...        
    def __init__( self , domain_str ):
        
        pyout << constants['client_boilerplate'] << endl             
        self.domain_str = domain_str
        
    def __str__( self ):    
        return 'chromatic_ice_client'   
    
    __repr__ = __str__ 
    
    #upcall
    def run( self, args ):     
        
        pass
        
    '''--------------------------------------------------------------------------------------------------------'''
    #attributes 
    @property    
    def client_domain_str( self ):
        return self.domain_str  
    

'''---------------------------------------------------------------------------------------------------------''' 
class chromatic_imap_client( chromatic_ice_client ):
    
    #constructor and operations here...        
    def __init__( self , domain_str = constants['default_domain'] ):
        
        super( chromatic_imap_client , self ).__init__( domain_str )            
            
    def list_recursive( self , dir , depth ):
        
        indent = ''
        depth = depth + 1
        for i in range( depth ):
            indent = indent + '\t'
        try:
            
            contents = dir.list()
            
            for node in contents:
                subdir = chromatic_imap_ext.chromatic_directoryPrx.checkedCast( node )
                file = chromatic_imap_ext.chromatic_filePrx.uncheckedCast( node )
                print indent + node.name(),
                
                if subdir:
                    print "(directory):"
                    self.list_recursive( subdir , depth )
                else:                
                    print "(file):"
                    text = file.read()
                    for line in text:
                        print indent + "\t" + line
                        
        except Ice.OperationNotExistException:
            pass
        except Ice.ObjectNotExistException:
            pass
                
    def __str__( self ):    
            return constants['client_boilerplate'] + '...imap client...'   
    
    __repr__ = __str__ 
    
    #upcall
    def run( self, args ):           
        
        try:
            #create a communicator              
            pyout << 'runtime initialized....' << endl
            
            #create a proxy for the root directory
            obj =  self.communicator().stringToProxy( constants['default_directory_name']
                                                       + ':' 
                                                       + self.client_domain_str )             
            
            #down-cast the proxy to a directory proxy            
            root_dir = chromatic_imap_ext.chromatic_directoryPrx.checkedCast( obj )
            pyout << 'proxy initialized...' << endl
            
            #recursively list the contents of the root directory
            pyout << 'contents of root directory: '
            self.list_recursive( root_dir , 0 )
            
            #wait until we are done
            self.communicator().waitForShutdown()
            if self.interrupted():
                pyout << '\n' << tstamp << self.appName() << ': terminating....' << endl
                                             
            
        except chromatic_imap_ext.chromatic_file_exception as e :        
            pyout << tstamp << 'file exception...'\
                  << e.reason \
                  << endl    
        except:
            pyout << tstamp << 'unexpected error:\n\t' \
                  << sys.exc_info()[0]\
                  << endl            
            traceback.print_exc()    
            
        finally:       
            pyout << tstamp << 'client shutting down...' << endl
            
    '''--------------------------------------------------------------------------------------------------------'''
    #attributes 
    @property
    def client_domain_str( self ):
        return self.domain_str


'''---------------------------------------------------------------------------------------------------------'''
sys.stdout.flush()
app = chromatic_imap_client()
sys.exit( app.main( sys.argv ) )   
