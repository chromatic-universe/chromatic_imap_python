'''Created on Jan 19, 2013 @author: William K. Johnson'''

from abc import ABCMeta , \
                abstractmethod , \
                abstractproperty
from utils.ice_python_utils import ostream ,\
                                   endl 
import StringIO 
                  

'''--------------------------------------------------------------------------------------------------'''
class chromatic_lex_exception( Exception ):
    
    def __init__( self , message , error_type = 0 ):

        #call the base class constructor with the parameters it needs
        Exception.__init__( self , message )

        self.tk = error_type
        
    @property
    def token_type( self ):
        return self.tk
    
'''--------------------------------------------------------------------------------------------------'''
class chromatic_parse_exception( Exception ):
    
    def __init__( self , message , error_type = 0 ):

        #call the base class constructor with the parameters it needs
        Exception.__init__( self , message )

        self.tk = error_type
        
    @property
    def token_type( self ):
        return self.tk
    
    
'''--------------------------------------------------------------------------------------------------'''
class chromatic_token( object ):
    
    #constructor and operations here...
    def __init__( self , token_type , text , token_lst = None ):
        
        self.token_type = token_type
        self.text = text
        self.token_lst = token_lst
        
    #helpers
    def type_to_str( self ):
        
        str_name = self.token_lst[self.token_type]
        
        pystr = '<text=\'{0}\' name={1}>\n'
        pystr = pystr.format( self.text , str_name )       
              
        return pystr
    
    def __str__( self ):    
        return 'chromatic_token'   
    
    __repr__ = __str__ 
    
    '''--------------------------------------------------------------------------------------------------------'''
    #attributes 
    @property
    def type( self ):
        return self.token_type
    @type.setter
    def type( self , value ):
        self.token = value
    
    
'''--------------------------------------------------------------------------------------------------'''
class chromatic_parser_abs( object ):
    
    __metaclass__ = ABCMeta  
    
    @abstractmethod
    def consume( self ):         
        pass
    
    @abstractmethod
    def match( self , look ):        
        pass
    
    @classmethod
    def __subclasshook__( cls , c ):
        
        #any class which implements 'match' and 'consume' is derived interface
        if cls is chromatic_lexer_abs:
            if any( "consume" in b.__dict__ for b in c.__mro__ ) :
                if any( "match" in b.__dict__ for b in c.__mro__ ) :
                    return True
        return NotImplemented
    
    '''--------------------------------------------------------------------------------------------------------'''
    #attributes 
    @abstractproperty
    def token_lookahead( self ):            
        pass   
    @abstractproperty
    def lex( self ):
        pass  
    
    
    
        
'''--------------------------------------------------------------------------------------------------'''
class chromatic_lexer_abs( object ):
    
    __metaclass__ = ABCMeta 
    
    def __init__( self ):        
        pass
    
    @abstractmethod
    def next_token( self ):        
        pass
    
    @abstractmethod
    def get_token_name( self , token_type ):         
        pass
    
    @abstractmethod
    def consume( self ):         
        pass
    
    @abstractmethod
    def match( self , char ):        
        pass
    
    @classmethod
    def __subclasshook__( cls , c ):
        
        #any class which implements 'next_token' is derived interface
        if cls is chromatic_lexer_abs:
            if any( "next_token" in b.__dict__ for b in c.__mro__ ):
                return True
        return NotImplemented
    
         
    '''--------------------------------------------------------------------------------------------------------'''
    #attributes      
    @abstractproperty
    def istr( self ):       
        pass     
    @abstractproperty  
    def ostr( self ):      
        pass       
    @abstractproperty
    def current( self ):        
        pass   
    @abstractproperty   
    def current_idx( self ):
        pass 
    @abstractproperty
    def end_of_file( self ):
        pass 
    @abstractproperty      
    def end_of_file_type( self ):
        pass    
    @abstractproperty   
    def token_lst( self ):
        pass   
   
    
'''--------------------------------------------------------------------------------------------------'''
class chromatic_nn_list_lexer( chromatic_lexer_abs ):
    
    #constructor and operations here...
    def __init__( self ,                   
                  stream_output = ostream() , 
                  stream_input = None ):
        
        super( chromatic_nn_list_lexer , self ).__init__() 
        
        self.EOF = -1
        self.EOF_Type = 1       
        self.NA = 0
        self.current_pos = 0
        self.current_ref = None        
        self._stream_in = stream_input
        self._stream_out = stream_output
        
        #prime lookahead
        if len( self._stream_in ) !=  0 :
            self.current_ref = self._stream_in[0]
        
        self.tk_name = 2
        self.tk_comma = 3
        self.tk_lbracket = 4
        self.tk_rbracket = 5
        self.tk_equals = 6
         
        self.token_names = ['n/a/' ,
                            '<EOF>' , 
                            'NAME' , 
                            ',' , 
                            '[' ,
                            ']' ,
                            '=']
        
        
    #helpers
    def is_letter( self ):
        
              
        return ( ( self.current_ref >= 'a' and self.current_ref <= 'z' )
                                           or  ( self.current_ref >= 'A'
                                                 and self.current_ref <= 'Z' ) )
        
    #services
    def NAME( self ):
        '''NAME : ('a'..'z'|'A'..'Z')+; // NAME is sequence of >=1 letter'''
        str_name  = ''
        while True:
            str_name += self.current_ref
            self.consume()
            if self.is_letter() == False:
                break
        
        return chromatic_token( self.tk_name , str , self.token_names )
    
   
    def WS( self ):
        #(' '|'\t'|'\n'|'\r')* ignore any whitespace 
            while ( c==' ' or c=='\t' or c=='\n' or c=='\r' ):
                self.consume()       
         
    def __str__( self ):    
        
        return 'chromatic_nn_list_lexer'   
    
    __repr__ = __str__ 
    
    '''--------------------------------------------------------------------------------------------------------'''
    #virtual services
    def next_token( self ):
        
            c = self.current_ref
            while ( c != self.EOF ):
                if c == ' '  or c == '\t' or c == '\n' or c == '\r': 
                    WS()                 
                    continue
                elif c == ',':
                    self.consume()
                    return chromatic_token( self.tk_comma , ',', self.token_names )
                elif c == '[':
                    self.consume()
                    return chromatic_token( self.tk_lbracket , "[" , self.token_names )
                elif c == ']' :
                    self.consume()
                    return  chromatic_token( self.tk_rbracket , "]" , self.token_names )
                elif c == '=' :
                    self.consume()
                    return  chromatic_token( self.tk_equals , "=" , self.token_names )
                else:
                    if self.is_letter():
                        return self.NAME();
                pystr = 'invalid character {0}\n'
                pystr = pystr.format( c )                       
                  
            raise chromatic_lex_exception( pystr )                
            
    
            return chromatic_token( self.EOF_Type ,'<EOF>' , self.token_names );

    
    def get_token_name( self , token_type ):
         
        return self.token_names[token_type]
    
    def consume( self ):
        
        self.current_pos += 1
        if self.current_pos >= len( self._stream_in ):
            self.current_ref = self.EOF
        else:
            self.current_ref = self._stream_in[self.current_pos]
            
    def match( self , char ):        
    
        if self.current_ref == char:
            self.consume()
        else:
            pyout = 'expecting {0} , found {1}\n' 
            pyout = pyout.format( char  , self.current_ref )
                  
            raise chromatic_lex_exception( pyout )
            
    
    
    '''--------------------------------------------------------------------------------------------------------'''
    #attributes  - properties and abstract properties are mutually exclusive  
    def istr( self ):
        return self.stream_input
    def ostr( self ):
        return self.stream_output    
   
    def current( self ):
        return self.current_ref
    def current_idx( self ):
        return self.current_pos
    def end_of_file( self ):
        return self.EOF
    def end_of_file_type( self ):
        return self.EOF_Type
    def token_lst( self ):
        return self.token_names
    
'''--------------------------------------------------------------------------------------------------'''
class chromatic_nn_list_parser( chromatic_parser_abs ):
    
   
    def __init__( self , lexer ):        
        
        self.lexer = lexer
        assert( self.lexer.current() )       
       
        self.consume()   
        
    '''--------------------------------------------------------------------------------------------------------'''
    #services    
    #list            :   '[' elements ']'  ;
    def list( self ):
        
        self.match( self.lexer.tk_lbracket )
        self.elements()
        self.match( self.lexer.tk_rbracket )
    
    #elements        :   element ( ',' element )* ;
    def elements( self ):
        
        self.element()
        while( self.token.type == self.lexer.tk_comma ):
            self.match( self.lexer.tk_comma )
            self.element()
            
    #element         :   NAME | list ;
    def element( self ):
        
        if self.token.type == self.lexer.tk_name:
            self.match( self.lexer.tk_name )
        elif self.token.type == self.lexer.tk_lbracket:
            self.list()
        else:
            pyout = 'expecting name or list , found \'{0}\'' 
            pyout = pyout.format( self.token.type_to_str() )
                  
            raise chromatic_parse_exception( pyout )   
    
    def __str__( self ):    
        
        return 'chromatic_nn_list_parser'   
    
    __repr__ = __str__ 
    
      
    '''--------------------------------------------------------------------------------------------------------'''   
    #virtual services
    def consume( self ):     
        
        print self.lex.current()
        self.token = self.lexer.next_token()         
    
    def match( self , look ):        
       
        if self.token.type == look:
            self.consume()
        else:
            pyout = 'expecting {0} , found {1}' 
            pyout = pyout.format( self.lexer.get_token_name( self.token.type )  ,
                                  self.lexer.get_token_name( look ) )
                  
            raise chromatic_parse_exception( pyout )
     
    
    '''--------------------------------------------------------------------------------------------------------'''
    #attributes    
    @property
    def token_lookahead( self ):            
        return self.token   
    @property    
    def lex( self ):
        return self.lexer   
    
'''--------------------------------------------------------------------------------------------------'''
class chromatic_nn_list_parser_2x( chromatic_parser_abs ):    
   
    def __init__( self , lexer , dw_look = 1 ):        
        
        self.lexer = lexer
        
        #index of ring buffer
        self.circle_idx = 0  
        
        #input stream
        assert( self.lexer.current() )  
        
        #amount of lookahead
        self.look_range = dw_look
        
        #lookahead buffer
        self.tokens = list()   
        i = 1
        while i <= self.look_range:
            
            #initialize tokenizer
            x = chromatic_token( 0 , '' , None )
            x.attr = i
            self.tokens.append( x )
            
            self.consume() 
            i += 1         
        
        
    '''--------------------------------------------------------------------------------------------------------'''
    #services
    def lt( self , idx ):
        
        #circular fetch        
        return self.tokens[( self.circle_idx + idx - 1 ) % self.look_range]
    
    def la( self , idx ):
        
        return self.lt( idx ).type
    
    #list            :   '[' elements ']'  ;
    def list( self ):
        
        self.match( self.lexer.tk_lbracket )
        self.elements()
        self.match( self.lexer.tk_rbracket )
    
    #elements        :   element ( ',' element )* ;
    def elements( self ):
        
        self.element()
        while self.la( 1 ) == self.lexer.tk_comma:
            self.match( self.lexer.tk_comma )
            self.element()
            
    #element         :   NAME = '=' NAME | NAME | list ; assignment  , NAME or list
    def element( self ):        
                 
        if ( self.la( 1 ) == self.lexer.tk_name ) and ( self.la( 2 ) == self.lexer.tk_equals ):
            self.match( self.lexer.tk_name )
            self.match( self.lexer.tk_equals )
            self.match( self.lexer.tk_name )         
        elif self.la( 1 ) == self.lexer.tk_name:
            self.match( self.lexer.tk_name )
        elif self.la( 1 ) == self.lexer.tk_lbracket:
            self.list()            
        else:
            pyout = 'expecting name or list , found \'{0}\'' 
            pyout = pyout.format( self.lexer.get_token_name( self.la( 1 ) ) )
                  
            raise chromatic_parse_exception( pyout )   
            
    def __str__( self ):    
        
        return 'chromatic_nn_list_parser_2x'   
    
    __repr__ = __str__ 
    
        
    '''--------------------------------------------------------------------------------------------------------'''   
    #virtual services
    def consume( self ):     
        
        print self.lex.current()
        self.tokens[ self.circle_idx ] = self.lexer.next_token()          
        self.circle_idx = ( self.circle_idx + 1 ) % ( self.look_range ) 
        
    
    def match( self , look ):      
        
        if self.la( 1 ) == look:
            self.consume()
        else:
            pyout = 'expecting {0} , found {1}' 
            pyout = pyout.format( self.lexer.get_token_name( self.tokens[self.la( 1 )].type )  ,
                                  self.lexer.get_token_name( look ) )
                  
            raise chromatic_parse_exception( pyout )
        
    '''--------------------------------------------------------------------------------------------------------'''
    #attributes    
    @property
    def token_lookahead( self ):            
        return self.tokens   
    @property    
    def lex( self ):
        return self.lexer   
        
    
    
'''--------------------------------------------------------------------------------------------------'''
if __name__ == '__main__':
    
  
    pyout = ostream()
    pyin = '[a,b=c,[d,e]]'    
        
    cn_lst = chromatic_nn_list_lexer( pyout , pyin )
    cn_parse =  chromatic_nn_list_parser_2x( cn_lst , 2 )
    #cn_parse =  chromatic_nn_list_parser( cn_lst )
    
    cn_parse.list()
    
    '''cn_token = cn_lst.next_token()      
    
    while cn_token.type != cn_lst.EOF_Type :
        print cn_token.type_to_str().strip()
        cn_token = cn_lst.next_token()
    
    print cn_token.type_to_str().strip()'''
   
    




