# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/Expr.g 2013-06-10 20:24:11

import sys
from antlr3 import *
from antlr3.compat import set, frozenset
  
import sys
import traceback
import os
import antlr3

from ExprLexer import ExprLexer
  



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
WS=7
NEWLINE=4
T__12=12
T__11=11
T__13=13
T__10=10
INT=6
ID=5
EOF=-1
T__9=9
T__8=8

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "NEWLINE", "ID", "INT", "WS", "'='", "'+'", "'-'", "'*'", "'('", "')'"
]




class ExprParser(Parser):
    grammarFileName = "/media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/Expr.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 17, 2009 19:23:44")
    antlr_version_str = "3.1.3 Mar 17, 2009 19:23:44"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(ExprParser, self).__init__(input, state, *args, **kwargs)



         
        self.value_dictionary = dict()




                


        



    # $ANTLR start "prog"
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/Expr.g:22:1: prog : ( stat )+ ;
    def prog(self, ):

        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/Expr.g:22:5: ( ( stat )+ )
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/Expr.g:22:9: ( stat )+
                pass 
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/Expr.g:22:9: ( stat )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((NEWLINE <= LA1_0 <= INT) or LA1_0 == 12) :
                        alt1 = 1


                    if alt1 == 1:
                        # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/Expr.g:22:9: stat
                        pass 
                        self._state.following.append(self.FOLLOW_stat_in_prog40)
                        self.stat()

                        self._state.following.pop()


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "prog"


    # $ANTLR start "stat"
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/Expr.g:24:1: stat : ( expr NEWLINE | ID '=' expr NEWLINE | NEWLINE );
    def stat(self, ):

        ID2 = None
        expr1 = None

        expr3 = None


        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/Expr.g:24:5: ( expr NEWLINE | ID '=' expr NEWLINE | NEWLINE )
                alt2 = 3
                LA2 = self.input.LA(1)
                if LA2 == INT or LA2 == 12:
                    alt2 = 1
                elif LA2 == ID:
                    LA2_2 = self.input.LA(2)

                    if (LA2_2 == 8) :
                        alt2 = 2
                    elif (LA2_2 == NEWLINE or (9 <= LA2_2 <= 11)) :
                        alt2 = 1
                    else:
                        nvae = NoViableAltException("", 2, 2, self.input)

                        raise nvae

                elif LA2 == NEWLINE:
                    alt2 = 3
                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae

                if alt2 == 1:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/Expr.g:24:9: expr NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_stat51)
                    expr1 = self.expr()

                    self._state.following.pop()
                    self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stat53)
                    #action start
                    print 'result: ' + str( expr1 ) 
                    #action end


                elif alt2 == 2:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/Expr.g:25:9: ID '=' expr NEWLINE
                    pass 
                    ID2=self.match(self.input, ID, self.FOLLOW_ID_in_stat65)
                    self.match(self.input, 8, self.FOLLOW_8_in_stat67)
                    self._state.following.append(self.FOLLOW_expr_in_stat69)
                    expr3 = self.expr()

                    self._state.following.pop()
                    self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stat71)
                    #action start
                    self.value_dictionary[ID2.text] = int( expr3 ) 
                    #action end


                elif alt2 == 3:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/Expr.g:28:9: NEWLINE
                    pass 
                    self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stat105)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "stat"


    # $ANTLR start "expr"
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/Expr.g:31:1: expr returns [int value] : e= multExpr ( '+' e= multExpr | '-' e= multExpr )* ;
    def expr(self, ):

        value = None

        e = None


        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/Expr.g:32:5: (e= multExpr ( '+' e= multExpr | '-' e= multExpr )* )
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/Expr.g:33:8: e= multExpr ( '+' e= multExpr | '-' e= multExpr )*
                pass 
                self._state.following.append(self.FOLLOW_multExpr_in_expr135)
                e = self.multExpr()

                self._state.following.pop()
                #action start
                value = e 
                #action end
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/Expr.g:34:9: ( '+' e= multExpr | '-' e= multExpr )*
                while True: #loop3
                    alt3 = 3
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == 9) :
                        alt3 = 1
                    elif (LA3_0 == 10) :
                        alt3 = 2


                    if alt3 == 1:
                        # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/Expr.g:34:13: '+' e= multExpr
                        pass 
                        self.match(self.input, 9, self.FOLLOW_9_in_expr151)
                        self._state.following.append(self.FOLLOW_multExpr_in_expr155)
                        e = self.multExpr()

                        self._state.following.pop()
                        #action start
                        value = value + e  
                        #action end


                    elif alt3 == 2:
                        # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/Expr.g:35:13: '-' e= multExpr
                        pass 
                        self.match(self.input, 10, self.FOLLOW_10_in_expr171)
                        self._state.following.append(self.FOLLOW_multExpr_in_expr175)
                        e = self.multExpr()

                        self._state.following.pop()
                        #action start
                        value = value - e  
                        #action end


                    else:
                        break #loop3




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return value

    # $ANTLR end "expr"


    # $ANTLR start "multExpr"
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/Expr.g:39:1: multExpr returns [int value] : e= atom ( '*' e= atom )* ;
    def multExpr(self, ):

        value = None

        e = None


        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/Expr.g:40:5: (e= atom ( '*' e= atom )* )
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/Expr.g:41:6: e= atom ( '*' e= atom )*
                pass 
                self._state.following.append(self.FOLLOW_atom_in_multExpr223)
                e = self.atom()

                self._state.following.pop()
                #action start
                value = e 
                #action end
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/Expr.g:41:35: ( '*' e= atom )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == 11) :
                        alt4 = 1


                    if alt4 == 1:
                        # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/Expr.g:41:36: '*' e= atom
                        pass 
                        self.match(self.input, 11, self.FOLLOW_11_in_multExpr228)
                        self._state.following.append(self.FOLLOW_atom_in_multExpr232)
                        e = self.atom()

                        self._state.following.pop()
                        #action start
                        value = value * e 
                        #action end


                    else:
                        break #loop4




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return value

    # $ANTLR end "multExpr"


    # $ANTLR start "atom"
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/Expr.g:44:1: atom returns [int value] : ( INT | ID | '(' expr ')' );
    def atom(self, ):

        value = None

        INT4 = None
        ID5 = None
        expr6 = None


        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/Expr.g:45:5: ( INT | ID | '(' expr ')' )
                alt5 = 3
                LA5 = self.input.LA(1)
                if LA5 == INT:
                    alt5 = 1
                elif LA5 == ID:
                    alt5 = 2
                elif LA5 == 12:
                    alt5 = 3
                else:
                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae

                if alt5 == 1:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/Expr.g:46:9: INT
                    pass 
                    INT4=self.match(self.input, INT, self.FOLLOW_INT_in_atom275)
                    #action start
                                  
                    value = int( INT4.text )               
                                
                    #action end


                elif alt5 == 2:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/Expr.g:49:9: ID
                    pass 
                    ID5=self.match(self.input, ID, self.FOLLOW_ID_in_atom287)
                    #action start
                                  
                    try:
                      value = int( self.value_dictionary[ID5.text] )
                    except KeyError as err:
                      print 'error , key not found in dictionary , variable undefined->  ' , ID5.text            
                                
                    #action end


                elif alt5 == 3:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/Expr.g:55:9: '(' expr ')'
                    pass 
                    self.match(self.input, 12, self.FOLLOW_12_in_atom300)
                    self._state.following.append(self.FOLLOW_expr_in_atom302)
                    expr6 = self.expr()

                    self._state.following.pop()
                    self.match(self.input, 13, self.FOLLOW_13_in_atom304)
                    #action start
                    value =  expr6 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return value

    # $ANTLR end "atom"


    # Delegated rules


 

    FOLLOW_stat_in_prog40 = frozenset([1, 4, 5, 6, 12])
    FOLLOW_expr_in_stat51 = frozenset([4])
    FOLLOW_NEWLINE_in_stat53 = frozenset([1])
    FOLLOW_ID_in_stat65 = frozenset([8])
    FOLLOW_8_in_stat67 = frozenset([5, 6, 12])
    FOLLOW_expr_in_stat69 = frozenset([4])
    FOLLOW_NEWLINE_in_stat71 = frozenset([1])
    FOLLOW_NEWLINE_in_stat105 = frozenset([1])
    FOLLOW_multExpr_in_expr135 = frozenset([1, 9, 10])
    FOLLOW_9_in_expr151 = frozenset([5, 6, 12])
    FOLLOW_multExpr_in_expr155 = frozenset([1, 9, 10])
    FOLLOW_10_in_expr171 = frozenset([5, 6, 12])
    FOLLOW_multExpr_in_expr175 = frozenset([1, 9, 10])
    FOLLOW_atom_in_multExpr223 = frozenset([1, 11])
    FOLLOW_11_in_multExpr228 = frozenset([5, 6, 12])
    FOLLOW_atom_in_multExpr232 = frozenset([1, 11])
    FOLLOW_INT_in_atom275 = frozenset([1])
    FOLLOW_ID_in_atom287 = frozenset([1])
    FOLLOW_12_in_atom300 = frozenset([5, 6, 12])
    FOLLOW_expr_in_atom302 = frozenset([13])
    FOLLOW_13_in_atom304 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ExprLexer", ExprParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
