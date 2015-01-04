# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g 2013-06-10 20:24:09

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *

 
import sys
import antlr3
import antlr3.tree



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




class ExprAstParser(Parser):
    grammarFileName = "/media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 17, 2009 19:23:44")
    antlr_version_str = "3.1.3 Mar 17, 2009 19:23:44"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(ExprAstParser, self).__init__(input, state, *args, **kwargs)



         
        self.value_dictionary = dict()




        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()
                


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class prog_return(ParserRuleReturnScope):
        def __init__(self):
            super(ExprAstParser.prog_return, self).__init__()

            self.tree = None




    # $ANTLR start "prog"
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g:22:1: prog : ( stat )+ ;
    def prog(self, ):

        retval = self.prog_return()
        retval.start = self.input.LT(1)

        root_0 = None

        stat1 = None



        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g:22:5: ( ( stat )+ )
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g:22:8: ( stat )+
                pass 
                root_0 = self._adaptor.nil()

                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g:22:8: ( stat )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((NEWLINE <= LA1_0 <= INT) or LA1_0 == 12) :
                        alt1 = 1


                    if alt1 == 1:
                        # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g:22:10: stat
                        pass 
                        self._state.following.append(self.FOLLOW_stat_in_prog56)
                        stat1 = self.stat()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, stat1.tree)
                        #action start
                        if stat1.tree == None:
                           print 'null' 
                        else:
                           print stat1.tree.toStringTree()
                                        
                        #action end


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "prog"

    class stat_return(ParserRuleReturnScope):
        def __init__(self):
            super(ExprAstParser.stat_return, self).__init__()

            self.tree = None




    # $ANTLR start "stat"
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g:29:1: stat : ( expr NEWLINE -> expr | ID '=' expr NEWLINE -> ^( '=' ID expr ) | NEWLINE ->);
    def stat(self, ):

        retval = self.stat_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NEWLINE3 = None
        ID4 = None
        char_literal5 = None
        NEWLINE7 = None
        NEWLINE8 = None
        expr2 = None

        expr6 = None


        NEWLINE3_tree = None
        ID4_tree = None
        char_literal5_tree = None
        NEWLINE7_tree = None
        NEWLINE8_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_8 = RewriteRuleTokenStream(self._adaptor, "token 8")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g:29:5: ( expr NEWLINE -> expr | ID '=' expr NEWLINE -> ^( '=' ID expr ) | NEWLINE ->)
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
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g:29:9: expr NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_stat80)
                    expr2 = self.expr()

                    self._state.following.pop()
                    stream_expr.add(expr2.tree)
                    NEWLINE3=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stat82) 
                    stream_NEWLINE.add(NEWLINE3)

                    # AST Rewrite
                    # elements: expr
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 29:31: -> expr
                    self._adaptor.addChild(root_0, stream_expr.nextTree())



                    retval.tree = root_0


                elif alt2 == 2:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g:30:9: ID '=' expr NEWLINE
                    pass 
                    ID4=self.match(self.input, ID, self.FOLLOW_ID_in_stat105) 
                    stream_ID.add(ID4)
                    char_literal5=self.match(self.input, 8, self.FOLLOW_8_in_stat107) 
                    stream_8.add(char_literal5)
                    self._state.following.append(self.FOLLOW_expr_in_stat109)
                    expr6 = self.expr()

                    self._state.following.pop()
                    stream_expr.add(expr6.tree)
                    NEWLINE7=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stat111) 
                    stream_NEWLINE.add(NEWLINE7)

                    # AST Rewrite
                    # elements: expr, 8, ID
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 30:31: -> ^( '=' ID expr )
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g:30:34: ^( '=' ID expr )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_8.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_ID.nextNode())
                    self._adaptor.addChild(root_1, stream_expr.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt2 == 3:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g:31:9: NEWLINE
                    pass 
                    NEWLINE8=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stat135) 
                    stream_NEWLINE.add(NEWLINE8)

                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 31:31: ->
                    root_0 = None


                    retval.tree = root_0


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "stat"

    class expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(ExprAstParser.expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "expr"
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g:34:1: expr : multExpr ( ( '+' | '-' ) multExpr )* ;
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal10 = None
        char_literal11 = None
        multExpr9 = None

        multExpr12 = None


        char_literal10_tree = None
        char_literal11_tree = None

        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g:34:5: ( multExpr ( ( '+' | '-' ) multExpr )* )
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g:34:9: multExpr ( ( '+' | '-' ) multExpr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_multExpr_in_expr165)
                multExpr9 = self.multExpr()

                self._state.following.pop()
                self._adaptor.addChild(root_0, multExpr9.tree)
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g:34:18: ( ( '+' | '-' ) multExpr )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if ((9 <= LA4_0 <= 10)) :
                        alt4 = 1


                    if alt4 == 1:
                        # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g:34:20: ( '+' | '-' ) multExpr
                        pass 
                        # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g:34:20: ( '+' | '-' )
                        alt3 = 2
                        LA3_0 = self.input.LA(1)

                        if (LA3_0 == 9) :
                            alt3 = 1
                        elif (LA3_0 == 10) :
                            alt3 = 2
                        else:
                            nvae = NoViableAltException("", 3, 0, self.input)

                            raise nvae

                        if alt3 == 1:
                            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g:34:21: '+'
                            pass 
                            char_literal10=self.match(self.input, 9, self.FOLLOW_9_in_expr170)

                            char_literal10_tree = self._adaptor.createWithPayload(char_literal10)
                            root_0 = self._adaptor.becomeRoot(char_literal10_tree, root_0)



                        elif alt3 == 2:
                            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g:34:26: '-'
                            pass 
                            char_literal11=self.match(self.input, 10, self.FOLLOW_10_in_expr173)

                            char_literal11_tree = self._adaptor.createWithPayload(char_literal11)
                            root_0 = self._adaptor.becomeRoot(char_literal11_tree, root_0)




                        self._state.following.append(self.FOLLOW_multExpr_in_expr178)
                        multExpr12 = self.multExpr()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, multExpr12.tree)


                    else:
                        break #loop4



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "expr"

    class multExpr_return(ParserRuleReturnScope):
        def __init__(self):
            super(ExprAstParser.multExpr_return, self).__init__()

            self.tree = None




    # $ANTLR start "multExpr"
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g:37:1: multExpr : atom ( '*' atom )* ;
    def multExpr(self, ):

        retval = self.multExpr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal14 = None
        atom13 = None

        atom15 = None


        char_literal14_tree = None

        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g:38:5: ( atom ( '*' atom )* )
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g:38:9: atom ( '*' atom )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_atom_in_multExpr201)
                atom13 = self.atom()

                self._state.following.pop()
                self._adaptor.addChild(root_0, atom13.tree)
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g:38:14: ( '*' atom )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == 11) :
                        alt5 = 1


                    if alt5 == 1:
                        # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g:38:15: '*' atom
                        pass 
                        char_literal14=self.match(self.input, 11, self.FOLLOW_11_in_multExpr204)

                        char_literal14_tree = self._adaptor.createWithPayload(char_literal14)
                        root_0 = self._adaptor.becomeRoot(char_literal14_tree, root_0)

                        self._state.following.append(self.FOLLOW_atom_in_multExpr207)
                        atom15 = self.atom()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, atom15.tree)


                    else:
                        break #loop5



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "multExpr"

    class atom_return(ParserRuleReturnScope):
        def __init__(self):
            super(ExprAstParser.atom_return, self).__init__()

            self.tree = None




    # $ANTLR start "atom"
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g:41:1: atom : ( INT | ID | '(' expr ')' );
    def atom(self, ):

        retval = self.atom_return()
        retval.start = self.input.LT(1)

        root_0 = None

        INT16 = None
        ID17 = None
        char_literal18 = None
        char_literal20 = None
        expr19 = None


        INT16_tree = None
        ID17_tree = None
        char_literal18_tree = None
        char_literal20_tree = None

        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g:41:5: ( INT | ID | '(' expr ')' )
                alt6 = 3
                LA6 = self.input.LA(1)
                if LA6 == INT:
                    alt6 = 1
                elif LA6 == ID:
                    alt6 = 2
                elif LA6 == 12:
                    alt6 = 3
                else:
                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae

                if alt6 == 1:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g:41:9: INT
                    pass 
                    root_0 = self._adaptor.nil()

                    INT16=self.match(self.input, INT, self.FOLLOW_INT_in_atom224)

                    INT16_tree = self._adaptor.createWithPayload(INT16)
                    self._adaptor.addChild(root_0, INT16_tree)



                elif alt6 == 2:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g:42:9: ID
                    pass 
                    root_0 = self._adaptor.nil()

                    ID17=self.match(self.input, ID, self.FOLLOW_ID_in_atom235)

                    ID17_tree = self._adaptor.createWithPayload(ID17)
                    self._adaptor.addChild(root_0, ID17_tree)



                elif alt6 == 3:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr_def/ExprAst.g:43:9: '(' expr ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal18=self.match(self.input, 12, self.FOLLOW_12_in_atom245)
                    self._state.following.append(self.FOLLOW_expr_in_atom248)
                    expr19 = self.expr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expr19.tree)
                    char_literal20=self.match(self.input, 13, self.FOLLOW_13_in_atom250)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "atom"


    # Delegated rules


 

    FOLLOW_stat_in_prog56 = frozenset([1, 4, 5, 6, 12])
    FOLLOW_expr_in_stat80 = frozenset([4])
    FOLLOW_NEWLINE_in_stat82 = frozenset([1])
    FOLLOW_ID_in_stat105 = frozenset([8])
    FOLLOW_8_in_stat107 = frozenset([5, 6, 12])
    FOLLOW_expr_in_stat109 = frozenset([4])
    FOLLOW_NEWLINE_in_stat111 = frozenset([1])
    FOLLOW_NEWLINE_in_stat135 = frozenset([1])
    FOLLOW_multExpr_in_expr165 = frozenset([1, 9, 10])
    FOLLOW_9_in_expr170 = frozenset([5, 6, 12])
    FOLLOW_10_in_expr173 = frozenset([5, 6, 12])
    FOLLOW_multExpr_in_expr178 = frozenset([1, 9, 10])
    FOLLOW_atom_in_multExpr201 = frozenset([1, 11])
    FOLLOW_11_in_multExpr204 = frozenset([5, 6, 12])
    FOLLOW_atom_in_multExpr207 = frozenset([1, 11])
    FOLLOW_INT_in_atom224 = frozenset([1])
    FOLLOW_ID_in_atom235 = frozenset([1])
    FOLLOW_12_in_atom245 = frozenset([5, 6, 12])
    FOLLOW_expr_in_atom248 = frozenset([13])
    FOLLOW_13_in_atom250 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ExprAstLexer", ExprAstParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
