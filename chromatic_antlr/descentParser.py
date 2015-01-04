# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/descent.g 2013-06-10 20:23:59

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
NAME=4
EOF=-1
T__7=7
T__6=6
T__5=5

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "NAME", "'['", "']'", "','"
]




class descentParser(Parser):
    grammarFileName = "/media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/descent.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 17, 2009 19:23:44")
    antlr_version_str = "3.1.3 Mar 17, 2009 19:23:44"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(descentParser, self).__init__(input, state, *args, **kwargs)






                


        



    # $ANTLR start "prog"
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/descent.g:9:1: prog : ( stat )+ ;
    def prog(self, ):

        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/descent.g:9:15: ( ( stat )+ )
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/descent.g:9:17: ( stat )+
                pass 
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/descent.g:9:17: ( stat )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == 5) :
                        alt1 = 1


                    if alt1 == 1:
                        # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/descent.g:9:17: stat
                        pass 
                        self._state.following.append(self.FOLLOW_stat_in_prog34)
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
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/descent.g:12:1: stat : list ;
    def stat(self, ):

        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/descent.g:12:17: ( list )
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/descent.g:12:21: list
                pass 
                self._state.following.append(self.FOLLOW_list_in_stat77)
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
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/descent.g:13:1: list : '[' elements ']' ;
    def list(self, ):

        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/descent.g:13:17: ( '[' elements ']' )
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/descent.g:13:21: '[' elements ']'
                pass 
                self.match(self.input, 5, self.FOLLOW_5_in_list99)
                self._state.following.append(self.FOLLOW_elements_in_list101)
                self.elements()

                self._state.following.pop()
                self.match(self.input, 6, self.FOLLOW_6_in_list103)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "list"


    # $ANTLR start "elements"
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/descent.g:14:1: elements : element ( ',' element )* ;
    def elements(self, ):

        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/descent.g:14:17: ( element ( ',' element )* )
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/descent.g:14:21: element ( ',' element )*
                pass 
                self._state.following.append(self.FOLLOW_element_in_elements121)
                self.element()

                self._state.following.pop()
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/descent.g:14:29: ( ',' element )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == 7) :
                        alt2 = 1


                    if alt2 == 1:
                        # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/descent.g:14:31: ',' element
                        pass 
                        self.match(self.input, 7, self.FOLLOW_7_in_elements125)
                        self._state.following.append(self.FOLLOW_element_in_elements127)
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
    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/descent.g:15:1: element : ( NAME | list );
    def element(self, ):

        try:
            try:
                # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/descent.g:15:17: ( NAME | list )
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == NAME) :
                    alt3 = 1
                elif (LA3_0 == 5) :
                    alt3 = 2
                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae

                if alt3 == 1:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/descent.g:15:21: NAME
                    pass 
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_element148)


                elif alt3 == 2:
                    # /media/wiljoh/55FE-3B01/chromatic_universe/trunk/python/antlr/workspace/chromatic_antlr/descent.g:15:28: list
                    pass 
                    self._state.following.append(self.FOLLOW_list_in_element152)
                    self.list()

                    self._state.following.pop()



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "element"


    # Delegated rules


 

    FOLLOW_stat_in_prog34 = frozenset([1, 5])
    FOLLOW_list_in_stat77 = frozenset([1])
    FOLLOW_5_in_list99 = frozenset([4, 5])
    FOLLOW_elements_in_list101 = frozenset([6])
    FOLLOW_6_in_list103 = frozenset([1])
    FOLLOW_element_in_elements121 = frozenset([1, 7])
    FOLLOW_7_in_elements125 = frozenset([4, 5])
    FOLLOW_element_in_elements127 = frozenset([1, 7])
    FOLLOW_NAME_in_element148 = frozenset([1])
    FOLLOW_list_in_element152 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("descentLexer", descentParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
