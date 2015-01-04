'''
Created on Jun 8, 2013

@author: wiljoh
'''
import sys
import antlr3



from ExprAstLexer  import ExprAstLexer
from ExprAstParser import ExprAstParser
  

if __name__ == '__main__':
       
        char_stream = antlr3.ANTLRInputStream( sys.stdin )
        lexer = ExprAstLexer( char_stream )
        tokens = antlr3.CommonTokenStream( lexer )
        parser = ExprAstParser( tokens )
        r = parser.prog()
        