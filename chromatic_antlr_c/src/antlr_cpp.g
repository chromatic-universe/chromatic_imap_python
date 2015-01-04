grammar antlr_cpp;

options {
  language = C;
  backtrack=true;
}

prog     : list EOF | assign EOF ;
assign   : list '=' list ;
list     : '[' elements ']' ;        // match bracketed list
elements : element (',' element)* ;  // match comma-separated list
element  : NAME '=' NAME | NAME | list ; //element is name, nested list


NAME     : LETTER+ ;                 // name is sequence of >=1 letter
fragment
LETTER   : 'a'..'z'|'A'..'Z';        // define what a letter is (\w)
WS       : (' '|'\t'|'\n'|'\r')+ {SKIP();} ; // throw out whitespace

