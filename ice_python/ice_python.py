'''
Created on Dec 31, 2012

@author: wiljoh
'''
import sys 
import traceback 
import Ice
import chromatic
from ice_python_utils import ostream , endl

class printerI( chromatic.printer ):
    def printString( self , s , current=None ):
        print s

cout = ostream()
cout << "ice_python...Internet Communication Engine....2012" << endl
status = 0
ic = None

try:    
    ic = Ice.initialize( sys.argv )
    adapter = ic.createObjectAdapterWithEndpoints( "SimplePrinterAdapter", "default -p 10000" )
    object = printerI()
    adapter.add(object, ic.stringToIdentity( "SimplePrinter" ) )
    adapter.activate()
    
    cout << "Internet Communication Engine initialized....printer adapter ready..." << endl
    
    ic.waitForShutdown()
    
except:
    traceback.print_exc()
    status = 1

if ic:
    # Clean up
    try:
        ic.destroy()
    except: 
        traceback.print_exc()
        status = 1

sys.exit( status )



    

   
    