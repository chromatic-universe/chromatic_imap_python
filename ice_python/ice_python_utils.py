'''ice_python_utils William K. Johnson 2012'''
import datetime

'''---------------------------------------------------------------------------'''
def today():
    return datetime.datetime.now().isoformat()

'''---------------------------------------------------------------------------'''
class io_manipulator( object ):
    
    def __init__( self , function=None ):
        self.function = function
    
    def do( self , output ):
        self.function( output )
'''---------------------------------------------------------------------------'''   
def do_endl( stream ):
        stream.output.write( '\n' )
        stream.output.flush()
endl = io_manipulator( do_endl )

'''---------------------------------------------------------------------------'''
def do_timestamp( stream ):
        stream.output.write( today() )
        stream.output.write( ' ')
        stream.output.flush()
tstamp = io_manipulator( do_timestamp )

'''---------------------------------------------------------------------------'''
def do_hex( stream ):
        stream.format = '%x'
hex_i = io_manipulator( do_hex )

'''---------------------------------------------------------------------------'''
class ostream( object ):    
    def __init__(self , output = None ):
        if output is None:
            import sys
            output = sys.stdout
        self.output = output
        self.format = '%s'
        
    def __lshift__( self , thing ):
        if isinstance( thing , io_manipulator ):
            thing.do( self )
        else:
            self.output.write( self.format % thing )
            self.format = '%s'
        return self
    
'''---------------------------------------------------------------------------'''
def example_main():
    cout = ostream()
    cout<< 'foo' << endl

if __name__ == '__main__':
    example_main()
    