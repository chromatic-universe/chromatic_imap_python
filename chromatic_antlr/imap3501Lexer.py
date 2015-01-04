# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g 2013-06-10 20:23:58

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
FOUR_DIGIT=6
T__29=29
T__28=28
T__27=27
T__26=26
T__25=25
CRLF=17
T__24=24
DOUBLEQUOTED_STRING=12
T__23=23
NUMBER=21
TAB=14
WHITESPACE=22
DQUOTE=8
MINUS=7
EOF=-1
ALPHA=20
T__30=30
ESCAPE_SEQUENCE=13
QUOTE=18
TWO_DIGIT=4
ESCAPE=9
SP=10
PLUS=5
DIGIT=19
CR=15
CTL=11
LF=16


class imap3501Lexer(Lexer):

    grammarFileName = "/media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 17, 2009 19:23:44")
    antlr_version_str = "3.1.3 Mar 17, 2009 19:23:44"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(imap3501Lexer, self).__init__(input, state)


        self.dfa9 = self.DFA9(
            self, 9,
            eot = self.DFA9_eot,
            eof = self.DFA9_eof,
            min = self.DFA9_min,
            max = self.DFA9_max,
            accept = self.DFA9_accept,
            special = self.DFA9_special,
            transition = self.DFA9_transition
            )






    # $ANTLR start "T__23"
    def mT__23(self, ):

        try:
            _type = T__23
            _channel = DEFAULT_CHANNEL

            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:7:7: ( '[' )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:7:9: '['
            pass 
            self.match(91)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__23"



    # $ANTLR start "T__24"
    def mT__24(self, ):

        try:
            _type = T__24
            _channel = DEFAULT_CHANNEL

            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:8:7: ( ']' )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:8:9: ']'
            pass 
            self.match(93)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__24"



    # $ANTLR start "T__25"
    def mT__25(self, ):

        try:
            _type = T__25
            _channel = DEFAULT_CHANNEL

            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:9:7: ( ',' )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:9:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__25"



    # $ANTLR start "T__26"
    def mT__26(self, ):

        try:
            _type = T__26
            _channel = DEFAULT_CHANNEL

            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:10:7: ( '%' )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:10:9: '%'
            pass 
            self.match(37)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__26"



    # $ANTLR start "T__27"
    def mT__27(self, ):

        try:
            _type = T__27
            _channel = DEFAULT_CHANNEL

            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:11:7: ( '*' )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:11:9: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__27"



    # $ANTLR start "T__28"
    def mT__28(self, ):

        try:
            _type = T__28
            _channel = DEFAULT_CHANNEL

            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:12:7: ( '(' )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:12:9: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__28"



    # $ANTLR start "T__29"
    def mT__29(self, ):

        try:
            _type = T__29
            _channel = DEFAULT_CHANNEL

            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:13:7: ( ')' )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:13:9: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__29"



    # $ANTLR start "T__30"
    def mT__30(self, ):

        try:
            _type = T__30
            _channel = DEFAULT_CHANNEL

            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:14:7: ( '{' )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:14:9: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__30"



    # $ANTLR start "DOUBLEQUOTED_STRING"
    def mDOUBLEQUOTED_STRING(self, ):

        try:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:26:22: ( '\"' (~ ( '\"' ) )* '\"' )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:26:24: '\"' (~ ( '\"' ) )* '\"'
            pass 
            self.match(34)
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:26:28: (~ ( '\"' ) )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((0 <= LA1_0 <= 33) or (35 <= LA1_0 <= 65535)) :
                    alt1 = 1


                if alt1 == 1:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:26:30: ~ ( '\"' )
                    pass 
                    if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop1
            self.match(34)




        finally:

            pass

    # $ANTLR end "DOUBLEQUOTED_STRING"



    # $ANTLR start "ESCAPE"
    def mESCAPE(self, ):

        try:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:28:17: ( '\\\\' )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:28:19: '\\\\'
            pass 
            self.match(92)




        finally:

            pass

    # $ANTLR end "ESCAPE"



    # $ANTLR start "ESCAPE_SEQUENCE"
    def mESCAPE_SEQUENCE(self, ):

        try:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:30:17: ( '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' ) )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:30:19: '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' )
            pass 
            self.match(92)
            if self.input.LA(1) == 34 or self.input.LA(1) == 39 or self.input.LA(1) == 92 or self.input.LA(1) == 98 or self.input.LA(1) == 102 or self.input.LA(1) == 110 or self.input.LA(1) == 114 or self.input.LA(1) == 116:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "ESCAPE_SEQUENCE"



    # $ANTLR start "CTL"
    def mCTL(self, ):

        try:
            _type = CTL
            _channel = DEFAULT_CHANNEL

            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:31:17: ( ( '\\u0002' .. '\\u001f' )+ | ( '\\u007F' )+ )
            alt4 = 2
            LA4_0 = self.input.LA(1)

            if ((2 <= LA4_0 <= 31)) :
                alt4 = 1
            elif (LA4_0 == 127) :
                alt4 = 2
            else:
                nvae = NoViableAltException("", 4, 0, self.input)

                raise nvae

            if alt4 == 1:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:31:19: ( '\\u0002' .. '\\u001f' )+
                pass 
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:31:19: ( '\\u0002' .. '\\u001f' )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((2 <= LA2_0 <= 31)) :
                        alt2 = 1


                    if alt2 == 1:
                        # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:31:21: '\\u0002' .. '\\u001f'
                        pass 
                        self.matchRange(2, 31)


                    else:
                        if cnt2 >= 1:
                            break #loop2

                        eee = EarlyExitException(2, self.input)
                        raise eee

                    cnt2 += 1


            elif alt4 == 2:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:31:44: ( '\\u007F' )+
                pass 
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:31:44: ( '\\u007F' )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == 127) :
                        alt3 = 1


                    if alt3 == 1:
                        # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:31:44: '\\u007F'
                        pass 
                        self.match(127)


                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CTL"



    # $ANTLR start "SP"
    def mSP(self, ):

        try:
            _type = SP
            _channel = DEFAULT_CHANNEL

            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:32:17: ( '\\u0020' )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:32:19: '\\u0020'
            pass 
            self.match(32)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SP"



    # $ANTLR start "TAB"
    def mTAB(self, ):

        try:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:34:17: ( '\\t' )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:34:19: '\\t'
            pass 
            self.match(9)




        finally:

            pass

    # $ANTLR end "TAB"



    # $ANTLR start "CRLF"
    def mCRLF(self, ):

        try:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:36:17: ( CR LF )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:36:19: CR LF
            pass 
            self.mCR()
            self.mLF()




        finally:

            pass

    # $ANTLR end "CRLF"



    # $ANTLR start "CR"
    def mCR(self, ):

        try:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:38:17: ( '\\r' )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:38:19: '\\r'
            pass 
            self.match(13)




        finally:

            pass

    # $ANTLR end "CR"



    # $ANTLR start "LF"
    def mLF(self, ):

        try:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:40:17: ( '\\n' )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:40:19: '\\n'
            pass 
            self.match(10)




        finally:

            pass

    # $ANTLR end "LF"



    # $ANTLR start "QUOTE"
    def mQUOTE(self, ):

        try:
            _type = QUOTE
            _channel = DEFAULT_CHANNEL

            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:41:17: ( '\\'' )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:41:19: '\\''
            pass 
            self.match(39)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "QUOTE"



    # $ANTLR start "DQUOTE"
    def mDQUOTE(self, ):

        try:
            _type = DQUOTE
            _channel = DEFAULT_CHANNEL

            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:42:17: ( '\"' )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:42:19: '\"'
            pass 
            self.match(34)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DQUOTE"



    # $ANTLR start "PLUS"
    def mPLUS(self, ):

        try:
            _type = PLUS
            _channel = DEFAULT_CHANNEL

            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:43:17: ( '+' )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:43:19: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PLUS"



    # $ANTLR start "MINUS"
    def mMINUS(self, ):

        try:
            _type = MINUS
            _channel = DEFAULT_CHANNEL

            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:44:17: ( '-' )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:44:19: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MINUS"



    # $ANTLR start "FOUR_DIGIT"
    def mFOUR_DIGIT(self, ):

        try:
            _type = FOUR_DIGIT
            _channel = DEFAULT_CHANNEL

            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:45:17: ( TWO_DIGIT TWO_DIGIT )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:45:19: TWO_DIGIT TWO_DIGIT
            pass 
            self.mTWO_DIGIT()
            self.mTWO_DIGIT()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FOUR_DIGIT"



    # $ANTLR start "TWO_DIGIT"
    def mTWO_DIGIT(self, ):

        try:
            _type = TWO_DIGIT
            _channel = DEFAULT_CHANNEL

            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:46:17: ( DIGIT DIGIT )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:46:19: DIGIT DIGIT
            pass 
            self.mDIGIT()
            self.mDIGIT()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TWO_DIGIT"



    # $ANTLR start "ALPHA"
    def mALPHA(self, ):

        try:
            _type = ALPHA
            _channel = DEFAULT_CHANNEL

            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:47:17: ( 'a' .. 'z' | 'A' .. 'Z' )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ALPHA"



    # $ANTLR start "NUMBER"
    def mNUMBER(self, ):

        try:
            _type = NUMBER
            _channel = DEFAULT_CHANNEL

            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:48:17: ( ( DIGIT )+ ( '.' ( DIGIT )* )? )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:48:19: ( DIGIT )+ ( '.' ( DIGIT )* )?
            pass 
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:48:19: ( DIGIT )+
            cnt5 = 0
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((48 <= LA5_0 <= 57)) :
                    alt5 = 1


                if alt5 == 1:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:48:19: DIGIT
                    pass 
                    self.mDIGIT()


                else:
                    if cnt5 >= 1:
                        break #loop5

                    eee = EarlyExitException(5, self.input)
                    raise eee

                cnt5 += 1
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:48:26: ( '.' ( DIGIT )* )?
            alt7 = 2
            LA7_0 = self.input.LA(1)

            if (LA7_0 == 46) :
                alt7 = 1
            if alt7 == 1:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:48:27: '.' ( DIGIT )*
                pass 
                self.match(46)
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:48:31: ( DIGIT )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if ((48 <= LA6_0 <= 57)) :
                        alt6 = 1


                    if alt6 == 1:
                        # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:48:31: DIGIT
                        pass 
                        self.mDIGIT()


                    else:
                        break #loop6






            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NUMBER"



    # $ANTLR start "WHITESPACE"
    def mWHITESPACE(self, ):

        try:
            _type = WHITESPACE
            _channel = DEFAULT_CHANNEL

            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:49:17: ( ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+ )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:49:19: ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+
            pass 
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:49:19: ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+
            cnt8 = 0
            while True: #loop8
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if ((9 <= LA8_0 <= 10) or (12 <= LA8_0 <= 13) or LA8_0 == 32) :
                    alt8 = 1


                if alt8 == 1:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:
                    pass 
                    if (9 <= self.input.LA(1) <= 10) or (12 <= self.input.LA(1) <= 13) or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt8 >= 1:
                        break #loop8

                    eee = EarlyExitException(8, self.input)
                    raise eee

                cnt8 += 1
            #action start
            _channel = HIDDEN;
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WHITESPACE"



    # $ANTLR start "DIGIT"
    def mDIGIT(self, ):

        try:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:50:17: ( '0' .. '9' )
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:50:19: '0' .. '9'
            pass 
            self.matchRange(48, 57)




        finally:

            pass

    # $ANTLR end "DIGIT"



    def mTokens(self):
        # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:1:8: ( T__23 | T__24 | T__25 | T__26 | T__27 | T__28 | T__29 | T__30 | CTL | SP | QUOTE | DQUOTE | PLUS | MINUS | FOUR_DIGIT | TWO_DIGIT | ALPHA | NUMBER | WHITESPACE )
        alt9 = 19
        alt9 = self.dfa9.predict(self.input)
        if alt9 == 1:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:1:10: T__23
            pass 
            self.mT__23()


        elif alt9 == 2:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:1:16: T__24
            pass 
            self.mT__24()


        elif alt9 == 3:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:1:22: T__25
            pass 
            self.mT__25()


        elif alt9 == 4:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:1:28: T__26
            pass 
            self.mT__26()


        elif alt9 == 5:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:1:34: T__27
            pass 
            self.mT__27()


        elif alt9 == 6:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:1:40: T__28
            pass 
            self.mT__28()


        elif alt9 == 7:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:1:46: T__29
            pass 
            self.mT__29()


        elif alt9 == 8:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:1:52: T__30
            pass 
            self.mT__30()


        elif alt9 == 9:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:1:58: CTL
            pass 
            self.mCTL()


        elif alt9 == 10:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:1:62: SP
            pass 
            self.mSP()


        elif alt9 == 11:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:1:65: QUOTE
            pass 
            self.mQUOTE()


        elif alt9 == 12:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:1:71: DQUOTE
            pass 
            self.mDQUOTE()


        elif alt9 == 13:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:1:78: PLUS
            pass 
            self.mPLUS()


        elif alt9 == 14:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:1:83: MINUS
            pass 
            self.mMINUS()


        elif alt9 == 15:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:1:89: FOUR_DIGIT
            pass 
            self.mFOUR_DIGIT()


        elif alt9 == 16:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:1:100: TWO_DIGIT
            pass 
            self.mTWO_DIGIT()


        elif alt9 == 17:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:1:110: ALPHA
            pass 
            self.mALPHA()


        elif alt9 == 18:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:1:116: NUMBER
            pass 
            self.mNUMBER()


        elif alt9 == 19:
            # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:1:123: WHITESPACE
            pass 
            self.mWHITESPACE()







    # lookup tables for DFA #9

    DFA9_eot = DFA.unpack(
        u"\11\uffff\1\12\1\uffff\1\23\4\uffff\1\24\4\uffff\1\26\1\uffff\1"
        u"\24\1\31\1\uffff"
        )

    DFA9_eof = DFA.unpack(
        u"\32\uffff"
        )

    DFA9_min = DFA.unpack(
        u"\1\2\10\uffff\1\11\1\uffff\1\11\4\uffff\1\60\4\uffff\1\56\1\uffff"
        u"\1\60\1\56\1\uffff"
        )

    DFA9_max = DFA.unpack(
        u"\1\177\10\uffff\1\40\1\uffff\1\40\4\uffff\1\71\4\uffff\1\71\1\uffff"
        u"\2\71\1\uffff"
        )

    DFA9_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\uffff\1\11\1\uffff"
        u"\1\13\1\14\1\15\1\16\1\uffff\1\21\1\23\1\12\1\22\1\uffff\1\20\2"
        u"\uffff\1\17"
        )

    DFA9_special = DFA.unpack(
        u"\32\uffff"
        )

            
    DFA9_transition = [
        DFA.unpack(u"\7\12\2\11\1\12\2\11\22\12\1\13\1\uffff\1\15\2\uffff"
        u"\1\4\1\uffff\1\14\1\6\1\7\1\5\1\16\1\3\1\17\2\uffff\12\20\7\uffff"
        u"\32\21\1\1\1\uffff\1\2\3\uffff\32\21\1\10\3\uffff\1\12"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\11\1\uffff\2\11\22\uffff\1\22"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\22\1\uffff\2\22\22\uffff\1\22"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\25"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\24\1\uffff\12\27"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\30"),
        DFA.unpack(u"\1\24\1\uffff\12\24"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #9

    class DFA9(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(imap3501Lexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
