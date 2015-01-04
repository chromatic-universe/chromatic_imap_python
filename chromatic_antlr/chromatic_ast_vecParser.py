# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g 2013-06-10 20:24:03

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
VEC=4
WS=7
T__15=15
T__12=12
T__11=11
T__14=14
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
    "VEC", "ID", "INT", "WS", "'='", "'print'", "'+'", "'*'", "'.'", "'['", 
    "','", "']'"
]




class chromatic_ast_vecParser(Parser):
    grammarFileName = "/media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 17, 2009 19:23:44")
    antlr_version_str = "3.1.3 Mar 17, 2009 19:23:44"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(chromatic_ast_vecParser, self).__init__(input, state, *args, **kwargs)






        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()
                


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class statlist_return(ParserRuleReturnScope):
        def __init__(self):
            super(chromatic_ast_vecParser.statlist_return, self).__init__()

            self.tree = None




    # $ANTLR start "statlist"
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:16:1: statlist : ( stat )+ ;
    def statlist(self, ):

        retval = self.statlist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        stat1 = None



        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:16:10: ( ( stat )+ )
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:16:12: ( stat )+
                pass 
                root_0 = self._adaptor.nil()

                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:16:12: ( stat )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == ID or LA1_0 == 9) :
                        alt1 = 1


                    if alt1 == 1:
                        # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:16:12: stat
                        pass 
                        self._state.following.append(self.FOLLOW_stat_in_statlist60)
                        stat1 = self.stat()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, stat1.tree)


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

    # $ANTLR end "statlist"

    class stat_return(ParserRuleReturnScope):
        def __init__(self):
            super(chromatic_ast_vecParser.stat_return, self).__init__()

            self.tree = None




    # $ANTLR start "stat"
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:17:1: stat : ( ID '=' expr -> ^( '=' ID expr ) | 'print' expr -> ^( 'print' expr ) );
    def stat(self, ):

        retval = self.stat_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID2 = None
        char_literal3 = None
        string_literal5 = None
        expr4 = None

        expr6 = None


        ID2_tree = None
        char_literal3_tree = None
        string_literal5_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_9 = RewriteRuleTokenStream(self._adaptor, "token 9")
        stream_8 = RewriteRuleTokenStream(self._adaptor, "token 8")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:17:5: ( ID '=' expr -> ^( '=' ID expr ) | 'print' expr -> ^( 'print' expr ) )
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == ID) :
                    alt2 = 1
                elif (LA2_0 == 9) :
                    alt2 = 2
                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae

                if alt2 == 1:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:17:7: ID '=' expr
                    pass 
                    ID2=self.match(self.input, ID, self.FOLLOW_ID_in_stat88) 
                    stream_ID.add(ID2)
                    char_literal3=self.match(self.input, 8, self.FOLLOW_8_in_stat90) 
                    stream_8.add(char_literal3)
                    self._state.following.append(self.FOLLOW_expr_in_stat92)
                    expr4 = self.expr()

                    self._state.following.pop()
                    stream_expr.add(expr4.tree)

                    # AST Rewrite
                    # elements: expr, ID, 8
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
                    # 17:20: -> ^( '=' ID expr )
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:17:23: ^( '=' ID expr )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_8.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_ID.nextNode())
                    self._adaptor.addChild(root_1, stream_expr.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt2 == 2:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:18:7: 'print' expr
                    pass 
                    string_literal5=self.match(self.input, 9, self.FOLLOW_9_in_stat113) 
                    stream_9.add(string_literal5)
                    self._state.following.append(self.FOLLOW_expr_in_stat115)
                    expr6 = self.expr()

                    self._state.following.pop()
                    stream_expr.add(expr6.tree)

                    # AST Rewrite
                    # elements: 9, expr
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
                    # 18:20: -> ^( 'print' expr )
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:18:23: ^( 'print' expr )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_9.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_expr.nextTree())

                    self._adaptor.addChild(root_0, root_1)



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
            super(chromatic_ast_vecParser.expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "expr"
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:23:1: expr : multExpr ( '+' multExpr )* ;
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal8 = None
        multExpr7 = None

        multExpr9 = None


        char_literal8_tree = None

        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:23:5: ( multExpr ( '+' multExpr )* )
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:23:9: multExpr ( '+' multExpr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_multExpr_in_expr140)
                multExpr7 = self.multExpr()

                self._state.following.pop()
                self._adaptor.addChild(root_0, multExpr7.tree)
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:23:18: ( '+' multExpr )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == 10) :
                        alt3 = 1


                    if alt3 == 1:
                        # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:23:19: '+' multExpr
                        pass 
                        char_literal8=self.match(self.input, 10, self.FOLLOW_10_in_expr143)

                        char_literal8_tree = self._adaptor.createWithPayload(char_literal8)
                        root_0 = self._adaptor.becomeRoot(char_literal8_tree, root_0)

                        self._state.following.append(self.FOLLOW_multExpr_in_expr146)
                        multExpr9 = self.multExpr()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, multExpr9.tree)


                    else:
                        break #loop3



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
            super(chromatic_ast_vecParser.multExpr_return, self).__init__()

            self.tree = None




    # $ANTLR start "multExpr"
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:24:1: multExpr : primary ( ( '*' | '.' ) primary )* ;
    def multExpr(self, ):

        retval = self.multExpr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal11 = None
        char_literal12 = None
        primary10 = None

        primary13 = None


        char_literal11_tree = None
        char_literal12_tree = None

        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:24:9: ( primary ( ( '*' | '.' ) primary )* )
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:24:11: primary ( ( '*' | '.' ) primary )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_primary_in_multExpr163)
                primary10 = self.primary()

                self._state.following.pop()
                self._adaptor.addChild(root_0, primary10.tree)
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:24:19: ( ( '*' | '.' ) primary )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if ((11 <= LA5_0 <= 12)) :
                        alt5 = 1


                    if alt5 == 1:
                        # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:24:20: ( '*' | '.' ) primary
                        pass 
                        # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:24:20: ( '*' | '.' )
                        alt4 = 2
                        LA4_0 = self.input.LA(1)

                        if (LA4_0 == 11) :
                            alt4 = 1
                        elif (LA4_0 == 12) :
                            alt4 = 2
                        else:
                            nvae = NoViableAltException("", 4, 0, self.input)

                            raise nvae

                        if alt4 == 1:
                            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:24:21: '*'
                            pass 
                            char_literal11=self.match(self.input, 11, self.FOLLOW_11_in_multExpr167)

                            char_literal11_tree = self._adaptor.createWithPayload(char_literal11)
                            root_0 = self._adaptor.becomeRoot(char_literal11_tree, root_0)



                        elif alt4 == 2:
                            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:24:26: '.'
                            pass 
                            char_literal12=self.match(self.input, 12, self.FOLLOW_12_in_multExpr170)

                            char_literal12_tree = self._adaptor.createWithPayload(char_literal12)
                            root_0 = self._adaptor.becomeRoot(char_literal12_tree, root_0)




                        self._state.following.append(self.FOLLOW_primary_in_multExpr174)
                        primary13 = self.primary()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, primary13.tree)


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

    class primary_return(ParserRuleReturnScope):
        def __init__(self):
            super(chromatic_ast_vecParser.primary_return, self).__init__()

            self.tree = None




    # $ANTLR start "primary"
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:25:1: primary : ( INT | ID | '[' expr ( ',' expr )* ']' -> ^( VEC ( expr )+ ) );
    def primary(self, ):

        retval = self.primary_return()
        retval.start = self.input.LT(1)

        root_0 = None

        INT14 = None
        ID15 = None
        char_literal16 = None
        char_literal18 = None
        char_literal20 = None
        expr17 = None

        expr19 = None


        INT14_tree = None
        ID15_tree = None
        char_literal16_tree = None
        char_literal18_tree = None
        char_literal20_tree = None
        stream_15 = RewriteRuleTokenStream(self._adaptor, "token 15")
        stream_13 = RewriteRuleTokenStream(self._adaptor, "token 13")
        stream_14 = RewriteRuleTokenStream(self._adaptor, "token 14")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:26:5: ( INT | ID | '[' expr ( ',' expr )* ']' -> ^( VEC ( expr )+ ) )
                alt7 = 3
                LA7 = self.input.LA(1)
                if LA7 == INT:
                    alt7 = 1
                elif LA7 == ID:
                    alt7 = 2
                elif LA7 == 13:
                    alt7 = 3
                else:
                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae

                if alt7 == 1:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:26:9: INT
                    pass 
                    root_0 = self._adaptor.nil()

                    INT14=self.match(self.input, INT, self.FOLLOW_INT_in_primary191)

                    INT14_tree = self._adaptor.createWithPayload(INT14)
                    self._adaptor.addChild(root_0, INT14_tree)



                elif alt7 == 2:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:27:9: ID
                    pass 
                    root_0 = self._adaptor.nil()

                    ID15=self.match(self.input, ID, self.FOLLOW_ID_in_primary204)

                    ID15_tree = self._adaptor.createWithPayload(ID15)
                    self._adaptor.addChild(root_0, ID15_tree)



                elif alt7 == 3:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:28:9: '[' expr ( ',' expr )* ']'
                    pass 
                    char_literal16=self.match(self.input, 13, self.FOLLOW_13_in_primary218) 
                    stream_13.add(char_literal16)
                    self._state.following.append(self.FOLLOW_expr_in_primary220)
                    expr17 = self.expr()

                    self._state.following.pop()
                    stream_expr.add(expr17.tree)
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:28:18: ( ',' expr )*
                    while True: #loop6
                        alt6 = 2
                        LA6_0 = self.input.LA(1)

                        if (LA6_0 == 14) :
                            alt6 = 1


                        if alt6 == 1:
                            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:28:19: ',' expr
                            pass 
                            char_literal18=self.match(self.input, 14, self.FOLLOW_14_in_primary223) 
                            stream_14.add(char_literal18)
                            self._state.following.append(self.FOLLOW_expr_in_primary225)
                            expr19 = self.expr()

                            self._state.following.pop()
                            stream_expr.add(expr19.tree)


                        else:
                            break #loop6
                    char_literal20=self.match(self.input, 15, self.FOLLOW_15_in_primary229) 
                    stream_15.add(char_literal20)

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
                    # 28:34: -> ^( VEC ( expr )+ )
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:28:37: ^( VEC ( expr )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VEC, "VEC"), root_1)

                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:28:43: ( expr )+
                    if not (stream_expr.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_expr.hasNext():
                        self._adaptor.addChild(root_1, stream_expr.nextTree())


                    stream_expr.reset()

                    self._adaptor.addChild(root_0, root_1)



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

    # $ANTLR end "primary"


    # Delegated rules


 

    FOLLOW_stat_in_statlist60 = frozenset([1, 5, 9])
    FOLLOW_ID_in_stat88 = frozenset([8])
    FOLLOW_8_in_stat90 = frozenset([5, 6, 13])
    FOLLOW_expr_in_stat92 = frozenset([1])
    FOLLOW_9_in_stat113 = frozenset([5, 6, 13])
    FOLLOW_expr_in_stat115 = frozenset([1])
    FOLLOW_multExpr_in_expr140 = frozenset([1, 10])
    FOLLOW_10_in_expr143 = frozenset([5, 6, 13])
    FOLLOW_multExpr_in_expr146 = frozenset([1, 10])
    FOLLOW_primary_in_multExpr163 = frozenset([1, 11, 12])
    FOLLOW_11_in_multExpr167 = frozenset([5, 6, 13])
    FOLLOW_12_in_multExpr170 = frozenset([5, 6, 13])
    FOLLOW_primary_in_multExpr174 = frozenset([1, 11, 12])
    FOLLOW_INT_in_primary191 = frozenset([1])
    FOLLOW_ID_in_primary204 = frozenset([1])
    FOLLOW_13_in_primary218 = frozenset([5, 6, 13])
    FOLLOW_expr_in_primary220 = frozenset([14, 15])
    FOLLOW_14_in_primary223 = frozenset([5, 6, 13])
    FOLLOW_expr_in_primary225 = frozenset([14, 15])
    FOLLOW_15_in_primary229 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("chromatic_ast_vecLexer", chromatic_ast_vecParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
