# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/backtrack.g 2013-06-10 20:24:04

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
NAME=4
WS=6
LETTER=5
T__10=10
EOF=-1
T__9=9
T__8=8
T__7=7

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "NAME", "LETTER", "WS", "'='", "'['", "']'", "','"
]




class backtrackParser(Parser):
    grammarFileName = "/media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/backtrack.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 17, 2009 19:23:44")
    antlr_version_str = "3.1.3 Mar 17, 2009 19:23:44"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(backtrackParser, self).__init__(input, state, *args, **kwargs)






                


        



    # $ANTLR start "stat"
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/backtrack.g:9:1: stat : ( list EOF | assign EOF );
    def stat(self, ):

        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/backtrack.g:9:10: ( list EOF | assign EOF )
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == 8) :
                    LA1_1 = self.input.LA(2)

                    if (self.synpred1_backtrack()) :
                        alt1 = 1
                    elif (True) :
                        alt1 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 1, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 1, 0, self.input)

                    raise nvae

                if alt1 == 1:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/backtrack.g:9:12: list EOF
                    pass 
                    self._state.following.append(self.FOLLOW_list_in_stat35)
                    self.list()

                    self._state.following.pop()
                    self.match(self.input, EOF, self.FOLLOW_EOF_in_stat37)


                elif alt1 == 2:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/backtrack.g:9:23: assign EOF
                    pass 
                    self._state.following.append(self.FOLLOW_assign_in_stat41)
                    self.assign()

                    self._state.following.pop()
                    self.match(self.input, EOF, self.FOLLOW_EOF_in_stat43)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "stat"


    # $ANTLR start "assign"
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/backtrack.g:10:1: assign : list '=' list ;
    def assign(self, ):

        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/backtrack.g:10:10: ( list '=' list )
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/backtrack.g:10:12: list '=' list
                pass 
                self._state.following.append(self.FOLLOW_list_in_assign53)
                self.list()

                self._state.following.pop()
                self.match(self.input, 7, self.FOLLOW_7_in_assign55)
                self._state.following.append(self.FOLLOW_list_in_assign57)
                self.list()

                self._state.following.pop()




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "assign"


    # $ANTLR start "list"
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/backtrack.g:11:1: list : '[' elements ']' ;
    def list(self, ):

        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/backtrack.g:11:10: ( '[' elements ']' )
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/backtrack.g:11:12: '[' elements ']'
                pass 
                self.match(self.input, 8, self.FOLLOW_8_in_list69)
                self._state.following.append(self.FOLLOW_elements_in_list71)
                self.elements()

                self._state.following.pop()
                self.match(self.input, 9, self.FOLLOW_9_in_list73)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "list"


    # $ANTLR start "elements"
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/backtrack.g:12:1: elements : element ( ',' element )* ;
    def elements(self, ):

        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/backtrack.g:12:10: ( element ( ',' element )* )
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/backtrack.g:12:12: element ( ',' element )*
                pass 
                self._state.following.append(self.FOLLOW_element_in_elements89)
                self.element()

                self._state.following.pop()
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/backtrack.g:12:20: ( ',' element )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == 10) :
                        alt2 = 1


                    if alt2 == 1:
                        # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/backtrack.g:12:21: ',' element
                        pass 
                        self.match(self.input, 10, self.FOLLOW_10_in_elements92)
                        self._state.following.append(self.FOLLOW_element_in_elements94)
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
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/backtrack.g:13:1: element : ( NAME '=' NAME | NAME | list );
    def element(self, ):

        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/backtrack.g:13:10: ( NAME '=' NAME | NAME | list )
                alt3 = 3
                LA3_0 = self.input.LA(1)

                if (LA3_0 == NAME) :
                    LA3_1 = self.input.LA(2)

                    if (LA3_1 == 7) :
                        alt3 = 1
                    elif (LA3_1 == EOF or (9 <= LA3_1 <= 10)) :
                        alt3 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 3, 1, self.input)

                        raise nvae

                elif (LA3_0 == 8) :
                    alt3 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae

                if alt3 == 1:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/backtrack.g:13:12: NAME '=' NAME
                    pass 
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_element107)
                    self.match(self.input, 7, self.FOLLOW_7_in_element109)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_element111)


                elif alt3 == 2:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/backtrack.g:13:28: NAME
                    pass 
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_element115)


                elif alt3 == 3:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/backtrack.g:13:35: list
                    pass 
                    self._state.following.append(self.FOLLOW_list_in_element119)
                    self.list()

                    self._state.following.pop()



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "element"

    # $ANTLR start "synpred1_backtrack"
    def synpred1_backtrack_fragment(self, ):
        # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/backtrack.g:9:12: ( list EOF )
        # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/backtrack.g:9:12: list EOF
        pass 
        self._state.following.append(self.FOLLOW_list_in_synpred1_backtrack35)
        self.list()

        self._state.following.pop()
        self.match(self.input, EOF, self.FOLLOW_EOF_in_synpred1_backtrack37)


    # $ANTLR end "synpred1_backtrack"




    # Delegated rules

    def synpred1_backtrack(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred1_backtrack_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



 

    FOLLOW_list_in_stat35 = frozenset([])
    FOLLOW_EOF_in_stat37 = frozenset([1])
    FOLLOW_assign_in_stat41 = frozenset([])
    FOLLOW_EOF_in_stat43 = frozenset([1])
    FOLLOW_list_in_assign53 = frozenset([7])
    FOLLOW_7_in_assign55 = frozenset([8])
    FOLLOW_list_in_assign57 = frozenset([1])
    FOLLOW_8_in_list69 = frozenset([4, 8])
    FOLLOW_elements_in_list71 = frozenset([9])
    FOLLOW_9_in_list73 = frozenset([1])
    FOLLOW_element_in_elements89 = frozenset([1, 10])
    FOLLOW_10_in_elements92 = frozenset([4, 8])
    FOLLOW_element_in_elements94 = frozenset([1, 10])
    FOLLOW_NAME_in_element107 = frozenset([7])
    FOLLOW_7_in_element109 = frozenset([4])
    FOLLOW_NAME_in_element111 = frozenset([1])
    FOLLOW_NAME_in_element115 = frozenset([1])
    FOLLOW_list_in_element119 = frozenset([1])
    FOLLOW_list_in_synpred1_backtrack35 = frozenset([])
    FOLLOW_EOF_in_synpred1_backtrack37 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("backtrackLexer", backtrackParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
