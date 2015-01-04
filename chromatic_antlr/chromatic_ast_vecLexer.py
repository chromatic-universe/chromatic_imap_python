# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g 2013-06-10 20:24:03

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


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


class chromatic_ast_vecLexer(Lexer):

    grammarFileName = "/media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 17, 2009 19:23:44")
    antlr_version_str = "3.1.3 Mar 17, 2009 19:23:44"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(chromatic_ast_vecLexer, self).__init__(input, state)


        self.dfa4 = self.DFA4(
            self, 4,
            eot = self.DFA4_eot,
            eof = self.DFA4_eof,
            min = self.DFA4_min,
            max = self.DFA4_max,
            accept = self.DFA4_accept,
            special = self.DFA4_special,
            transition = self.DFA4_transition
            )






    # $ANTLR start "T__8"
    def mT__8(self, ):

        try:
            _type = T__8
            _channel = DEFAULT_CHANNEL

            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:7:6: ( '=' )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:7:8: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__8"



    # $ANTLR start "T__9"
    def mT__9(self, ):

        try:
            _type = T__9
            _channel = DEFAULT_CHANNEL

            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:8:6: ( 'print' )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:8:8: 'print'
            pass 
            self.match("print")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__9"



    # $ANTLR start "T__10"
    def mT__10(self, ):

        try:
            _type = T__10
            _channel = DEFAULT_CHANNEL

            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:9:7: ( '+' )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:9:9: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__10"



    # $ANTLR start "T__11"
    def mT__11(self, ):

        try:
            _type = T__11
            _channel = DEFAULT_CHANNEL

            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:10:7: ( '*' )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:10:9: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__11"



    # $ANTLR start "T__12"
    def mT__12(self, ):

        try:
            _type = T__12
            _channel = DEFAULT_CHANNEL

            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:11:7: ( '.' )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:11:9: '.'
            pass 
            self.match(46)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__12"



    # $ANTLR start "T__13"
    def mT__13(self, ):

        try:
            _type = T__13
            _channel = DEFAULT_CHANNEL

            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:12:7: ( '[' )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:12:9: '['
            pass 
            self.match(91)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__13"



    # $ANTLR start "T__14"
    def mT__14(self, ):

        try:
            _type = T__14
            _channel = DEFAULT_CHANNEL

            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:13:7: ( ',' )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:13:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__14"



    # $ANTLR start "T__15"
    def mT__15(self, ):

        try:
            _type = T__15
            _channel = DEFAULT_CHANNEL

            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:14:7: ( ']' )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:14:9: ']'
            pass 
            self.match(93)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__15"



    # $ANTLR start "ID"
    def mID(self, ):

        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:32:5: ( ( 'a' .. 'z' )+ )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:32:9: ( 'a' .. 'z' )+
            pass 
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:32:9: ( 'a' .. 'z' )+
            cnt1 = 0
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((97 <= LA1_0 <= 122)) :
                    alt1 = 1


                if alt1 == 1:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:32:9: 'a' .. 'z'
                    pass 
                    self.matchRange(97, 122)


                else:
                    if cnt1 >= 1:
                        break #loop1

                    eee = EarlyExitException(1, self.input)
                    raise eee

                cnt1 += 1



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ID"



    # $ANTLR start "INT"
    def mINT(self, ):

        try:
            _type = INT
            _channel = DEFAULT_CHANNEL

            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:33:5: ( ( '0' .. '9' )+ )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:33:9: ( '0' .. '9' )+
            pass 
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:33:9: ( '0' .. '9' )+
            cnt2 = 0
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((48 <= LA2_0 <= 57)) :
                    alt2 = 1


                if alt2 == 1:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:33:9: '0' .. '9'
                    pass 
                    self.matchRange(48, 57)


                else:
                    if cnt2 >= 1:
                        break #loop2

                    eee = EarlyExitException(2, self.input)
                    raise eee

                cnt2 += 1



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INT"



    # $ANTLR start "WS"
    def mWS(self, ):

        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:34:5: ( ( ' ' | '\\r' | '\\n' )+ )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:34:9: ( ' ' | '\\r' | '\\n' )+
            pass 
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:34:9: ( ' ' | '\\r' | '\\n' )+
            cnt3 = 0
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == 10 or LA3_0 == 13 or LA3_0 == 32) :
                    alt3 = 1


                if alt3 == 1:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:
                    pass 
                    if self.input.LA(1) == 10 or self.input.LA(1) == 13 or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt3 >= 1:
                        break #loop3

                    eee = EarlyExitException(3, self.input)
                    raise eee

                cnt3 += 1
            #action start
            skip();
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WS"



    def mTokens(self):
        # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:1:8: ( T__8 | T__9 | T__10 | T__11 | T__12 | T__13 | T__14 | T__15 | ID | INT | WS )
        alt4 = 11
        alt4 = self.dfa4.predict(self.input)
        if alt4 == 1:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:1:10: T__8
            pass 
            self.mT__8()


        elif alt4 == 2:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:1:15: T__9
            pass 
            self.mT__9()


        elif alt4 == 3:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:1:20: T__10
            pass 
            self.mT__10()


        elif alt4 == 4:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:1:26: T__11
            pass 
            self.mT__11()


        elif alt4 == 5:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:1:32: T__12
            pass 
            self.mT__12()


        elif alt4 == 6:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:1:38: T__13
            pass 
            self.mT__13()


        elif alt4 == 7:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:1:44: T__14
            pass 
            self.mT__14()


        elif alt4 == 8:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:1:50: T__15
            pass 
            self.mT__15()


        elif alt4 == 9:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:1:56: ID
            pass 
            self.mID()


        elif alt4 == 10:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:1:59: INT
            pass 
            self.mINT()


        elif alt4 == 11:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/chromatic_ast_vec.g:1:63: WS
            pass 
            self.mWS()







    # lookup tables for DFA #4

    DFA4_eot = DFA.unpack(
        u"\2\uffff\1\11\11\uffff\3\11\1\20\1\uffff"
        )

    DFA4_eof = DFA.unpack(
        u"\21\uffff"
        )

    DFA4_min = DFA.unpack(
        u"\1\12\1\uffff\1\162\11\uffff\1\151\1\156\1\164\1\141\1\uffff"
        )

    DFA4_max = DFA.unpack(
        u"\1\172\1\uffff\1\162\11\uffff\1\151\1\156\1\164\1\172\1\uffff"
        )

    DFA4_accept = DFA.unpack(
        u"\1\uffff\1\1\1\uffff\1\3\1\4\1\5\1\6\1\7\1\10\1\11\1\12\1\13\4"
        u"\uffff\1\2"
        )

    DFA4_special = DFA.unpack(
        u"\21\uffff"
        )

            
    DFA4_transition = [
        DFA.unpack(u"\1\13\2\uffff\1\13\22\uffff\1\13\11\uffff\1\4\1\3\1"
        u"\7\1\uffff\1\5\1\uffff\12\12\3\uffff\1\1\35\uffff\1\6\1\uffff\1"
        u"\10\3\uffff\17\11\1\2\12\11"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\14"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\15"),
        DFA.unpack(u"\1\16"),
        DFA.unpack(u"\1\17"),
        DFA.unpack(u"\32\11"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #4

    class DFA4(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(chromatic_ast_vecLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
