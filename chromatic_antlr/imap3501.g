grammar imap3501;

options
{
  language = Python;
}

prog            : stat+      ;
stat            : list               ;

list            :   '[' elements ']'  ;
elements        : element ( ',' element )* ;
element         : TWO_DIGIT;


zone            : PLUS FOUR_DIGIT | MINUS FOUR_DIGIT ;  
list_wildcards  : '%' | '*';
quoted_specials : DQUOTE | ESCAPE  ;
resp_specials   : ']';
atom_specials   : '(' | ')' | '{' | SP | CTL 
                  | list_wildcards
                  | quoted_specials
                  | resp_specials
                  ;
fragment
DOUBLEQUOTED_STRING  : '"' ( ~('"') )* '"';
fragment
ESCAPE          : '\\';
fragment
ESCAPE_SEQUENCE : '\\' ('b'|'t'|'n'|'f'|'r'|'\"'|'\''|'\\');
CTL             : ( '\u0002'..'\u001f')+ | '\u007F'+;
SP              : '\u0020';
fragment
TAB             : '\t';
fragment
CRLF            : CR LF;
fragment
CR              : '\r';
fragment
LF              : '\n';
QUOTE           : '\'';
DQUOTE          : '"';
PLUS            : '+' ;
MINUS           : '-' ;
FOUR_DIGIT      : TWO_DIGIT  TWO_DIGIT ;
TWO_DIGIT       : DIGIT DIGIT;  
ALPHA           : 'a'..'z'|'A'..'Z';        
NUMBER          : DIGIT+ ('.' DIGIT*)?;
WHITESPACE      : ('\t' | ' ' | '\r' | '\n' |  '\u000C' )+ {$channel = HIDDEN;};
fragment DIGIT  : '0'..'9';