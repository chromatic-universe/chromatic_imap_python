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
	from ExprParser import ExprParser
}
@members
{
  value_dictionary = dict()
}

prog
    :   stat+ ;
        
stat
    :
       expr NEWLINE {  print $expr.value  }
        
    |   ID '=' expr NEWLINE
        { value_dictionary[$ID.text] = int( $expr.value ) }

       
    |   NEWLINE
    ;
    

expr returns [int value]
    :   e=multExpr { $value = $e.value }
        (   '+' e=multExpr { $value = $value + $e.value  }
        |   '-' e=multExpr { $value = $value - $e.value  }
        )*
        
       {  print 'expr=' + s }
    ;

multExpr returns [int value]
    :   e=atom { $value = $e.value } ('*' e=atom { $value = $value * $e.value } )*
        { print 'multiexpr' }
    ; 

atom returns [int value]
    :   // value of an INT is the int computed from char sequence
        INT
        { 
            $value = int( $INT.text ) 
        }

   |   ID // variable referenceS
        {	
        	
          try:           
            $value = int( value_dictionary[$ID.text] )
          except KeyError , e:             
            print 'error undefined variable ' + $ID.text
         } 
       
    |   '(' expr ')' { $value = $expr.value }
    ;


ID  :   ('a'..'z'|'A'..'Z')+ ;
INT :   '0'..'9'+ ;
NEWLINE:'\r'? '\n' ;
WS  :   (' '|'\t')+ {skip();} ;
