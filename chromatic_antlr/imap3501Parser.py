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
ESCAPE_SEQUENCE=13
T__30=30
QUOTE=18
TWO_DIGIT=4
ESCAPE=9
SP=10
PLUS=5
DIGIT=19
CR=15
CTL=11
LF=16

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "TWO_DIGIT", "PLUS", "FOUR_DIGIT", "MINUS", "DQUOTE", "ESCAPE", "SP", 
    "CTL", "DOUBLEQUOTED_STRING", "ESCAPE_SEQUENCE", "TAB", "CR", "LF", 
    "CRLF", "QUOTE", "DIGIT", "ALPHA", "NUMBER", "WHITESPACE", "'['", "']'", 
    "','", "'%'", "'*'", "'('", "')'", "'{'"
]




class imap3501Parser(Parser):
    grammarFileName = "/media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 17, 2009 19:23:44")
    antlr_version_str = "3.1.3 Mar 17, 2009 19:23:44"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(imap3501Parser, self).__init__(input, state, *args, **kwargs)






                


        



    # $ANTLR start "prog"
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:8:1: prog : ( stat )+ ;
    def prog(self, ):

        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:8:17: ( ( stat )+ )
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:8:19: ( stat )+
                pass 
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:8:19: ( stat )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == 23) :
                        alt1 = 1


                    if alt1 == 1:
                        # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:8:19: stat
                        pass 
                        self._state.following.append(self.FOLLOW_stat_in_prog35)
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
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:9:1: stat : list ;
    def stat(self, ):

        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:9:17: ( list )
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:9:19: list
                pass 
                self._state.following.append(self.FOLLOW_list_in_stat60)
                self.list()

                self._state.following.pop()




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "stat"


    # $ANTLR start "list"
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:11:1: list : '[' elements ']' ;
    def list(self, ):

        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:11:17: ( '[' elements ']' )
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:11:21: '[' elements ']'
                pass 
                self.match(self.input, 23, self.FOLLOW_23_in_list96)
                self._state.following.append(self.FOLLOW_elements_in_list98)
                self.elements()

                self._state.following.pop()
                self.match(self.input, 24, self.FOLLOW_24_in_list100)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "list"


    # $ANTLR start "elements"
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:12:1: elements : element ( ',' element )* ;
    def elements(self, ):

        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:12:17: ( element ( ',' element )* )
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:12:19: element ( ',' element )*
                pass 
                self._state.following.append(self.FOLLOW_element_in_elements116)
                self.element()

                self._state.following.pop()
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:12:27: ( ',' element )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == 25) :
                        alt2 = 1


                    if alt2 == 1:
                        # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:12:29: ',' element
                        pass 
                        self.match(self.input, 25, self.FOLLOW_25_in_elements120)
                        self._state.following.append(self.FOLLOW_element_in_elements122)
                        self.element()

                        self._state.following.pop()


                    else:
                        break #loop2




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "elements"


    # $ANTLR start "element"
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:13:1: element : TWO_DIGIT ;
    def element(self, ):

        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:13:17: ( TWO_DIGIT )
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:13:19: TWO_DIGIT
                pass 
                self.match(self.input, TWO_DIGIT, self.FOLLOW_TWO_DIGIT_in_element141)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "element"


    # $ANTLR start "zone"
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:16:1: zone : ( PLUS FOUR_DIGIT | MINUS FOUR_DIGIT );
    def zone(self, ):

        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:16:17: ( PLUS FOUR_DIGIT | MINUS FOUR_DIGIT )
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == PLUS) :
                    alt3 = 1
                elif (LA3_0 == MINUS) :
                    alt3 = 2
                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae

                if alt3 == 1:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:16:19: PLUS FOUR_DIGIT
                    pass 
                    self.match(self.input, PLUS, self.FOLLOW_PLUS_in_zone161)
                    self.match(self.input, FOUR_DIGIT, self.FOLLOW_FOUR_DIGIT_in_zone163)


                elif alt3 == 2:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:16:37: MINUS FOUR_DIGIT
                    pass 
                    self.match(self.input, MINUS, self.FOLLOW_MINUS_in_zone167)
                    self.match(self.input, FOUR_DIGIT, self.FOLLOW_FOUR_DIGIT_in_zone169)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "zone"


    # $ANTLR start "list_wildcards"
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:17:1: list_wildcards : ( '%' | '*' );
    def list_wildcards(self, ):

        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:17:17: ( '%' | '*' )
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:
                pass 
                if (26 <= self.input.LA(1) <= 27):
                    self.input.consume()
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "list_wildcards"


    # $ANTLR start "quoted_specials"
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:18:1: quoted_specials : ( DQUOTE | ESCAPE );
    def quoted_specials(self, ):

        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:18:17: ( DQUOTE | ESCAPE )
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:
                pass 
                if (DQUOTE <= self.input.LA(1) <= ESCAPE):
                    self.input.consume()
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "quoted_specials"


    # $ANTLR start "resp_specials"
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:19:1: resp_specials : ']' ;
    def resp_specials(self, ):

        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:19:17: ( ']' )
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:19:19: ']'
                pass 
                self.match(self.input, 24, self.FOLLOW_24_in_resp_specials206)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "resp_specials"


    # $ANTLR start "atom_specials"
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:20:1: atom_specials : ( '(' | ')' | '{' | SP | CTL | list_wildcards | quoted_specials | resp_specials );
    def atom_specials(self, ):

        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:20:17: ( '(' | ')' | '{' | SP | CTL | list_wildcards | quoted_specials | resp_specials )
                alt4 = 8
                LA4 = self.input.LA(1)
                if LA4 == 28:
                    alt4 = 1
                elif LA4 == 29:
                    alt4 = 2
                elif LA4 == 30:
                    alt4 = 3
                elif LA4 == SP:
                    alt4 = 4
                elif LA4 == CTL:
                    alt4 = 5
                elif LA4 == 26 or LA4 == 27:
                    alt4 = 6
                elif LA4 == DQUOTE or LA4 == ESCAPE:
                    alt4 = 7
                elif LA4 == 24:
                    alt4 = 8
                else:
                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae

                if alt4 == 1:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:20:19: '('
                    pass 
                    self.match(self.input, 28, self.FOLLOW_28_in_atom_specials215)


                elif alt4 == 2:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:20:25: ')'
                    pass 
                    self.match(self.input, 29, self.FOLLOW_29_in_atom_specials219)


                elif alt4 == 3:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:20:31: '{'
                    pass 
                    self.match(self.input, 30, self.FOLLOW_30_in_atom_specials223)


                elif alt4 == 4:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:20:37: SP
                    pass 
                    self.match(self.input, SP, self.FOLLOW_SP_in_atom_specials227)


                elif alt4 == 5:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:20:42: CTL
                    pass 
                    self.match(self.input, CTL, self.FOLLOW_CTL_in_atom_specials231)


                elif alt4 == 6:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:21:21: list_wildcards
                    pass 
                    self._state.following.append(self.FOLLOW_list_wildcards_in_atom_specials254)
                    self.list_wildcards()

                    self._state.following.pop()


                elif alt4 == 7:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:22:21: quoted_specials
                    pass 
                    self._state.following.append(self.FOLLOW_quoted_specials_in_atom_specials276)
                    self.quoted_specials()

                    self._state.following.pop()


                elif alt4 == 8:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/imap3501.g:23:21: resp_specials
                    pass 
                    self._state.following.append(self.FOLLOW_resp_specials_in_atom_specials298)
                    self.resp_specials()

                    self._state.following.pop()



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "atom_specials"


    # Delegated rules


 

    FOLLOW_stat_in_prog35 = frozenset([1, 23])
    FOLLOW_list_in_stat60 = frozenset([1])
    FOLLOW_23_in_list96 = frozenset([4])
    FOLLOW_elements_in_list98 = frozenset([24])
    FOLLOW_24_in_list100 = frozenset([1])
    FOLLOW_element_in_elements116 = frozenset([1, 25])
    FOLLOW_25_in_elements120 = frozenset([4])
    FOLLOW_element_in_elements122 = frozenset([1, 25])
    FOLLOW_TWO_DIGIT_in_element141 = frozenset([1])
    FOLLOW_PLUS_in_zone161 = frozenset([6])
    FOLLOW_FOUR_DIGIT_in_zone163 = frozenset([1])
    FOLLOW_MINUS_in_zone167 = frozenset([6])
    FOLLOW_FOUR_DIGIT_in_zone169 = frozenset([1])
    FOLLOW_set_in_list_wildcards0 = frozenset([1])
    FOLLOW_set_in_quoted_specials0 = frozenset([1])
    FOLLOW_24_in_resp_specials206 = frozenset([1])
    FOLLOW_28_in_atom_specials215 = frozenset([1])
    FOLLOW_29_in_atom_specials219 = frozenset([1])
    FOLLOW_30_in_atom_specials223 = frozenset([1])
    FOLLOW_SP_in_atom_specials227 = frozenset([1])
    FOLLOW_CTL_in_atom_specials231 = frozenset([1])
    FOLLOW_list_wildcards_in_atom_specials254 = frozenset([1])
    FOLLOW_quoted_specials_in_atom_specials276 = frozenset([1])
    FOLLOW_resp_specials_in_atom_specials298 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("imap3501Lexer", imap3501Parser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
