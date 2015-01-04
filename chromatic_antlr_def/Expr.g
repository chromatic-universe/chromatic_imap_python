grammar Expr;

options 
{  
  language = Python;  
}
@header
 {
  import sys
  import traceback
  import os
  import antlr3

  from ExprLexer import ExprLexer
  
}
@init
{
   self.value_dictionary = dict()
}

prog:   stat+ ;

stat:   expr NEWLINE { print 'result: ' + str( $expr.value ) }
    |   ID '=' expr NEWLINE
        { self.value_dictionary[$ID.text] = int( $expr.value ) }     
        
    |   NEWLINE
    ;

expr returns [int value]
    :
       e=multExpr { $value = $e.value }
        (   '+' e=multExpr { $value = $value + $e.value  }
        |   '-' e=multExpr { $value = $value - $e.value  }
        )*       
    ;

multExpr returns [int value]
    :
     e=atom { $value = $e.value } ('*' e=atom { $value = $value * $e.value } )*        
    ; 

atom returns [int value]
    :
        INT { 
                $value = int( $INT.text )               
            }
    |   ID  { 
                try:
                  $value = int( self.value_dictionary[$ID.text] )
                except KeyError as err:
                  print 'error , key not found in dictionary , variable undefined->  ' , $ID.text            
            }
    |   '(' expr ')' { $value = $expr.value; }  
    ;



ID  :   ('a'..'z'|'A'..'Z')+ ;
INT :   '0'..'9'+ ;
NEWLINE:'\r'? '\n' ;
WS  :   (' '|'\t')+ {skip();} ;

