grammar ExprAst;

options
{
  language = Python;
  output = AST;
  ASTLabelType = CommonTree;
}
@header
{
  import sys
  import antlr3
  import antlr3.tree
}
@init
{
   self.value_dictionary = dict()
}



prog:  ( stat  { if $stat.tree == None:
                    print 'null' 
                 else:
                    print $stat.tree.toStringTree()
                }
        )+ ;

stat:   expr NEWLINE          -> expr
    |   ID '=' expr NEWLINE   -> ^( '=' ID expr )
    |   NEWLINE               ->
    ;

expr:   multExpr ( ('+'^|'-'^ ) multExpr )*
    ; 

multExpr
    :   atom ('*'^ atom)*
    ; 

atom:   INT 
    |   ID
    |   '('! expr ')'!
    ;
// END:expr

// START:tokens
ID  :   ('a'..'z'|'A'..'Z')+ ;
INT :   '0'..'9'+ ;
NEWLINE:'\r'? '\n' ;
WS  :   (' '|'\t')+ {skip();} ;
// END:tokens
