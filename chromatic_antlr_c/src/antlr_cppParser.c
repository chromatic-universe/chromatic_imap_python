/** \file
 *  This C source file was generated by $ANTLR version 3.1.3 Mar 18, 2009 10:09:25
 *
 *     -  From the grammar source file : antlr_cpp.g
 *     -                            On : 2013-01-31 12:28:01
 *     -                for the parser : antlr_cppParserParser *
 * Editing it, at least manually, is not wise. 
 *
 * C language generator and runtime by Jim Idle, jimi|hereisanat|idle|dotgoeshere|ws.
 *
 *
*/
// [The "BSD licence"]
// Copyright (c) 2005-2009 Jim Idle, Temporal Wave LLC
// http://www.temporal-wave.com
// http://www.linkedin.com/in/jimidle
//
// All rights reserved.
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions
// are met:
// 1. Redistributions of source code must retain the above copyright
//    notice, this list of conditions and the following disclaimer.
// 2. Redistributions in binary form must reproduce the above copyright
//    notice, this list of conditions and the following disclaimer in the
//    documentation and/or other materials provided with the distribution.
// 3. The name of the author may not be used to endorse or promote products
//    derived from this software without specific prior written permission.
//
// THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
// IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
// OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
// IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
// INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
// NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
// DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
// THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
// THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

/* -----------------------------------------
 * Include the ANTLR3 generated header file.
 */
#include    "antlr_cppParser.h"
/* ----------------------------------------- */





/* MACROS that hide the C interface implementations from the
 * generated code, which makes it a little more understandable to the human eye.
 * I am very much against using C pre-processor macros for function calls and bits
 * of code as you cannot see what is happening when single stepping in debuggers
 * and so on. The exception (in my book at least) is for generated code, where you are
 * not maintaining it, but may wish to read and understand it. If you single step it, you know that input()
 * hides some indirect calls, but is always referring to the input stream. This is
 * probably more readable than ctx->input->istream->input(snarfle0->blarg) and allows me to rejig
 * the runtime interfaces without changing the generated code too often, without
 * confusing the reader of the generated output, who may not wish to know the gory
 * details of the interface inheritance.
 */
 
#define		CTX	ctx

/* Aids in accessing scopes for grammar programmers
 */
#undef	SCOPE_TYPE
#undef	SCOPE_STACK
#undef	SCOPE_TOP
#define	SCOPE_TYPE(scope)   pantlr_cppParser_##scope##_SCOPE
#define SCOPE_STACK(scope)  pantlr_cppParser_##scope##Stack
#define	SCOPE_TOP(scope)    ctx->pantlr_cppParser_##scope##Top
#define	SCOPE_SIZE(scope)			(ctx->SCOPE_STACK(scope)->size(ctx->SCOPE_STACK(scope)))
#define SCOPE_INSTANCE(scope, i)	(ctx->SCOPE_STACK(scope)->get(ctx->SCOPE_STACK(scope),i))

/* Macros for accessing things in the parser
 */
 
#undef	    PARSER		    
#undef	    RECOGNIZER		    
#undef	    HAVEPARSEDRULE
#undef		MEMOIZE
#undef	    INPUT
#undef	    STRSTREAM
#undef	    HASEXCEPTION
#undef	    EXCEPTION
#undef	    MATCHT
#undef	    MATCHANYT
#undef	    FOLLOWSTACK
#undef	    FOLLOWPUSH
#undef	    FOLLOWPOP
#undef	    PRECOVER
#undef	    PREPORTERROR
#undef	    LA
#undef	    LT
#undef	    CONSTRUCTEX
#undef	    CONSUME
#undef	    MARK
#undef	    REWIND
#undef	    REWINDLAST
#undef	    PERRORRECOVERY
#undef	    HASFAILED
#undef	    FAILEDFLAG
#undef	    RECOVERFROMMISMATCHEDSET
#undef	    RECOVERFROMMISMATCHEDELEMENT
#undef		INDEX
#undef      ADAPTOR
#undef		SEEK
#undef	    RULEMEMO		    
#undef		DBG

#define	    PARSER							ctx->pParser  
#define	    RECOGNIZER						PARSER->rec
#define		PSRSTATE						RECOGNIZER->state
#define	    HAVEPARSEDRULE(r)				RECOGNIZER->alreadyParsedRule(RECOGNIZER, r)
#define		MEMOIZE(ri,si)					RECOGNIZER->memoize(RECOGNIZER, ri, si)
#define	    INPUT							PARSER->tstream
#define	    STRSTREAM						INPUT
#define		ISTREAM							INPUT->istream
#define		INDEX()							ISTREAM->index(INPUT->istream)
#define	    HASEXCEPTION()					(PSRSTATE->error == ANTLR3_TRUE)
#define	    EXCEPTION						PSRSTATE->exception
#define	    MATCHT(t, fs)					RECOGNIZER->match(RECOGNIZER, t, fs)
#define	    MATCHANYT()						RECOGNIZER->matchAny(RECOGNIZER)
#define	    FOLLOWSTACK					    PSRSTATE->following
#define	    FOLLOWPUSH(x)					FOLLOWSTACK->push(FOLLOWSTACK, ((void *)(&(x))), NULL)
#define	    FOLLOWPOP()						FOLLOWSTACK->pop(FOLLOWSTACK)
#define	    PRECOVER()						RECOGNIZER->recover(RECOGNIZER)
#define	    PREPORTERROR()					RECOGNIZER->reportError(RECOGNIZER)
#define	    LA(n)							INPUT->istream->_LA(ISTREAM, n)
#define	    LT(n)							INPUT->_LT(INPUT, n)
#define	    CONSTRUCTEX()					RECOGNIZER->exConstruct(RECOGNIZER)
#define	    CONSUME()						ISTREAM->consume(ISTREAM)
#define	    MARK()							ISTREAM->mark(ISTREAM)
#define	    REWIND(m)						ISTREAM->rewind(ISTREAM, m)
#define	    REWINDLAST()					ISTREAM->rewindLast(ISTREAM)
#define		SEEK(n)							ISTREAM->seek(ISTREAM, n)
#define	    PERRORRECOVERY					PSRSTATE->errorRecovery
#define	    FAILEDFLAG						PSRSTATE->failed
#define	    HASFAILED()						(FAILEDFLAG == ANTLR3_TRUE)
#define	    BACKTRACKING					PSRSTATE->backtracking
#define	    RECOVERFROMMISMATCHEDSET(s)		RECOGNIZER->recoverFromMismatchedSet(RECOGNIZER, s)
#define	    RECOVERFROMMISMATCHEDELEMENT(e)	RECOGNIZER->recoverFromMismatchedElement(RECOGNIZER, s)
#define     ADAPTOR                         ctx->adaptor
#define		RULEMEMO						PSRSTATE->ruleMemo
#define		DBG								RECOGNIZER->debugger

#define		TOKTEXT(tok, txt)				tok, (pANTLR3_UINT8)txt

/* The 4 tokens defined below may well clash with your own #defines or token types. If so
 * then for the present you must use different names for your defines as these are hard coded
 * in the code generator. It would be better not to use such names internally, and maybe
 * we can change this in a forthcoming release. I deliberately do not #undef these
 * here as this will at least give you a redefined error somewhere if they clash.
 */
#define	    UP	    ANTLR3_TOKEN_UP
#define	    DOWN    ANTLR3_TOKEN_DOWN
#define	    EOR	    ANTLR3_TOKEN_EOR
#define	    INVALID ANTLR3_TOKEN_INVALID


/* =============================================================================
 * Functions to create and destroy scopes. First come the rule scopes, followed
 * by the global declared scopes.
 */



/* ============================================================================= */

/* =============================================================================
 * Start of recognizer
 */



/** \brief Table of all token names in symbolic order, mainly used for
 *         error reporting.
 */
pANTLR3_UINT8   antlr_cppParserTokenNames[7+4]
     = {
        (pANTLR3_UINT8) "<invalid>",       /* String to print to indicate an invalid token */
        (pANTLR3_UINT8) "<EOR>",
        (pANTLR3_UINT8) "<DOWN>", 
        (pANTLR3_UINT8) "<UP>", 
        (pANTLR3_UINT8) "NAME",
        (pANTLR3_UINT8) "LETTER",
        (pANTLR3_UINT8) "WS",
        (pANTLR3_UINT8) "'='",
        (pANTLR3_UINT8) "'['",
        (pANTLR3_UINT8) "']'",
        (pANTLR3_UINT8) "','"
       };

        

// Forward declare the locally static matching functions we have generated.
//
static void	prog    (pantlr_cppParser ctx);
static void	assign    (pantlr_cppParser ctx);
static void	list    (pantlr_cppParser ctx);
static void	elements    (pantlr_cppParser ctx);
static void	element    (pantlr_cppParser ctx);
static ANTLR3_BOOLEAN	synpred1_antlr_cpp    (pantlr_cppParser ctx);
static void	antlr_cppParserFree(pantlr_cppParser ctx);
/* For use in tree output where we are accumulating rule labels via label += ruleRef
 * we need a function that knows how to free a return scope when the list is destroyed. 
 * We cannot just use ANTLR3_FREE because in debug tracking mode, this is a macro.
 */
static	void ANTLR3_CDECL freeScope(void * scope)
{
    ANTLR3_FREE(scope);
}

/** \brief Name of the grammar file that generated this code
 */
static const char fileName[] = "antlr_cpp.g";

/** \brief Return the name of the grammar file that generated this code.
 */
static const char * getGrammarFileName()
{
	return fileName;
}
/** \brief Create a new antlr_cppParser parser and return a context for it.
 *
 * \param[in] instream Pointer to an input stream interface.
 *
 * \return Pointer to new parser context upon success.
 */
ANTLR3_API pantlr_cppParser
antlr_cppParserNew   (pANTLR3_COMMON_TOKEN_STREAM instream)
{
	// See if we can create a new parser with the standard constructor
	//
	return antlr_cppParserNewSSD(instream, NULL);
}

/** \brief Create a new antlr_cppParser parser and return a context for it.
 *
 * \param[in] instream Pointer to an input stream interface.
 *
 * \return Pointer to new parser context upon success.
 */
ANTLR3_API pantlr_cppParser
antlr_cppParserNewSSD   (pANTLR3_COMMON_TOKEN_STREAM instream, pANTLR3_RECOGNIZER_SHARED_STATE state)
{
    pantlr_cppParser ctx;	    /* Context structure we will build and return   */
    
    ctx	= (pantlr_cppParser) ANTLR3_CALLOC(1, sizeof(antlr_cppParser));
    
    if	(ctx == NULL)
    {
		// Failed to allocate memory for parser context
		//
        return  NULL;
    }
    
    /* -------------------------------------------------------------------
     * Memory for basic structure is allocated, now to fill in
     * the base ANTLR3 structures. We initialize the function pointers
     * for the standard ANTLR3 parser function set, but upon return
     * from here, the programmer may set the pointers to provide custom
     * implementations of each function. 
     *
     * We don't use the macros defined in antlr_cppParser.h here, in order that you can get a sense
     * of what goes where.
     */

    /* Create a base parser/recognizer, using the supplied token stream
     */
    ctx->pParser	    = antlr3ParserNewStream(ANTLR3_SIZE_HINT, instream->tstream, state);
    /* Install the implementation of our antlr_cppParser interface
     */
    ctx->prog	= prog;
    ctx->assign	= assign;
    ctx->list	= list;
    ctx->elements	= elements;
    ctx->element	= element;
    ctx->synpred1_antlr_cpp	= synpred1_antlr_cpp;
    ctx->free			= antlr_cppParserFree;
    ctx->getGrammarFileName	= getGrammarFileName;
    
    /* Install the scope pushing methods.
     */

        
    

	
    /* Install the token table
     */
    PSRSTATE->tokenNames   = antlr_cppParserTokenNames;
    
    
    /* Return the newly built parser to the caller
     */
    return  ctx;
}

/** Free the parser resources
 */
 static void
 antlr_cppParserFree(pantlr_cppParser ctx)
 {
    /* Free any scope memory
     */
    
        
	// Free this parser
	//
    ctx->pParser->free(ctx->pParser);
    ANTLR3_FREE(ctx);

    /* Everything is released, so we can return
     */
    return;
 }
 
/** Return token names used by this parser
 *
 * The returned pointer is used as an index into the token names table (using the token 
 * number as the index).
 * 
 * \return Pointer to first char * in the table.
 */
static pANTLR3_UINT8    *getTokenNames() 
{
        return antlr_cppParserTokenNames; 
}

    
/* Declare the bitsets
 */

/** Bitset defining follow set for error recovery in rule state: FOLLOW_list_in_prog35  */
static	ANTLR3_BITWORD FOLLOW_list_in_prog35_bits[]	= { ANTLR3_UINT64_LIT(0x0000000000000000) };
static  ANTLR3_BITSET_LIST FOLLOW_list_in_prog35	= { FOLLOW_list_in_prog35_bits, 1	};
/** Bitset defining follow set for error recovery in rule state: FOLLOW_EOF_in_prog37  */
static	ANTLR3_BITWORD FOLLOW_EOF_in_prog37_bits[]	= { ANTLR3_UINT64_LIT(0x0000000000000002) };
static  ANTLR3_BITSET_LIST FOLLOW_EOF_in_prog37	= { FOLLOW_EOF_in_prog37_bits, 1	};
/** Bitset defining follow set for error recovery in rule state: FOLLOW_assign_in_prog41  */
static	ANTLR3_BITWORD FOLLOW_assign_in_prog41_bits[]	= { ANTLR3_UINT64_LIT(0x0000000000000000) };
static  ANTLR3_BITSET_LIST FOLLOW_assign_in_prog41	= { FOLLOW_assign_in_prog41_bits, 1	};
/** Bitset defining follow set for error recovery in rule state: FOLLOW_EOF_in_prog43  */
static	ANTLR3_BITWORD FOLLOW_EOF_in_prog43_bits[]	= { ANTLR3_UINT64_LIT(0x0000000000000002) };
static  ANTLR3_BITSET_LIST FOLLOW_EOF_in_prog43	= { FOLLOW_EOF_in_prog43_bits, 1	};
/** Bitset defining follow set for error recovery in rule state: FOLLOW_list_in_assign53  */
static	ANTLR3_BITWORD FOLLOW_list_in_assign53_bits[]	= { ANTLR3_UINT64_LIT(0x0000000000000080) };
static  ANTLR3_BITSET_LIST FOLLOW_list_in_assign53	= { FOLLOW_list_in_assign53_bits, 1	};
/** Bitset defining follow set for error recovery in rule state: FOLLOW_7_in_assign55  */
static	ANTLR3_BITWORD FOLLOW_7_in_assign55_bits[]	= { ANTLR3_UINT64_LIT(0x0000000000000100) };
static  ANTLR3_BITSET_LIST FOLLOW_7_in_assign55	= { FOLLOW_7_in_assign55_bits, 1	};
/** Bitset defining follow set for error recovery in rule state: FOLLOW_list_in_assign57  */
static	ANTLR3_BITWORD FOLLOW_list_in_assign57_bits[]	= { ANTLR3_UINT64_LIT(0x0000000000000002) };
static  ANTLR3_BITSET_LIST FOLLOW_list_in_assign57	= { FOLLOW_list_in_assign57_bits, 1	};
/** Bitset defining follow set for error recovery in rule state: FOLLOW_8_in_list69  */
static	ANTLR3_BITWORD FOLLOW_8_in_list69_bits[]	= { ANTLR3_UINT64_LIT(0x0000000000000110) };
static  ANTLR3_BITSET_LIST FOLLOW_8_in_list69	= { FOLLOW_8_in_list69_bits, 1	};
/** Bitset defining follow set for error recovery in rule state: FOLLOW_elements_in_list71  */
static	ANTLR3_BITWORD FOLLOW_elements_in_list71_bits[]	= { ANTLR3_UINT64_LIT(0x0000000000000200) };
static  ANTLR3_BITSET_LIST FOLLOW_elements_in_list71	= { FOLLOW_elements_in_list71_bits, 1	};
/** Bitset defining follow set for error recovery in rule state: FOLLOW_9_in_list73  */
static	ANTLR3_BITWORD FOLLOW_9_in_list73_bits[]	= { ANTLR3_UINT64_LIT(0x0000000000000002) };
static  ANTLR3_BITSET_LIST FOLLOW_9_in_list73	= { FOLLOW_9_in_list73_bits, 1	};
/** Bitset defining follow set for error recovery in rule state: FOLLOW_element_in_elements89  */
static	ANTLR3_BITWORD FOLLOW_element_in_elements89_bits[]	= { ANTLR3_UINT64_LIT(0x0000000000000402) };
static  ANTLR3_BITSET_LIST FOLLOW_element_in_elements89	= { FOLLOW_element_in_elements89_bits, 1	};
/** Bitset defining follow set for error recovery in rule state: FOLLOW_10_in_elements92  */
static	ANTLR3_BITWORD FOLLOW_10_in_elements92_bits[]	= { ANTLR3_UINT64_LIT(0x0000000000000110) };
static  ANTLR3_BITSET_LIST FOLLOW_10_in_elements92	= { FOLLOW_10_in_elements92_bits, 1	};
/** Bitset defining follow set for error recovery in rule state: FOLLOW_element_in_elements94  */
static	ANTLR3_BITWORD FOLLOW_element_in_elements94_bits[]	= { ANTLR3_UINT64_LIT(0x0000000000000402) };
static  ANTLR3_BITSET_LIST FOLLOW_element_in_elements94	= { FOLLOW_element_in_elements94_bits, 1	};
/** Bitset defining follow set for error recovery in rule state: FOLLOW_NAME_in_element107  */
static	ANTLR3_BITWORD FOLLOW_NAME_in_element107_bits[]	= { ANTLR3_UINT64_LIT(0x0000000000000080) };
static  ANTLR3_BITSET_LIST FOLLOW_NAME_in_element107	= { FOLLOW_NAME_in_element107_bits, 1	};
/** Bitset defining follow set for error recovery in rule state: FOLLOW_7_in_element109  */
static	ANTLR3_BITWORD FOLLOW_7_in_element109_bits[]	= { ANTLR3_UINT64_LIT(0x0000000000000010) };
static  ANTLR3_BITSET_LIST FOLLOW_7_in_element109	= { FOLLOW_7_in_element109_bits, 1	};
/** Bitset defining follow set for error recovery in rule state: FOLLOW_NAME_in_element111  */
static	ANTLR3_BITWORD FOLLOW_NAME_in_element111_bits[]	= { ANTLR3_UINT64_LIT(0x0000000000000002) };
static  ANTLR3_BITSET_LIST FOLLOW_NAME_in_element111	= { FOLLOW_NAME_in_element111_bits, 1	};
/** Bitset defining follow set for error recovery in rule state: FOLLOW_NAME_in_element115  */
static	ANTLR3_BITWORD FOLLOW_NAME_in_element115_bits[]	= { ANTLR3_UINT64_LIT(0x0000000000000002) };
static  ANTLR3_BITSET_LIST FOLLOW_NAME_in_element115	= { FOLLOW_NAME_in_element115_bits, 1	};
/** Bitset defining follow set for error recovery in rule state: FOLLOW_list_in_element119  */
static	ANTLR3_BITWORD FOLLOW_list_in_element119_bits[]	= { ANTLR3_UINT64_LIT(0x0000000000000002) };
static  ANTLR3_BITSET_LIST FOLLOW_list_in_element119	= { FOLLOW_list_in_element119_bits, 1	};
/** Bitset defining follow set for error recovery in rule state: FOLLOW_list_in_synpred1_antlr_cpp35  */
static	ANTLR3_BITWORD FOLLOW_list_in_synpred1_antlr_cpp35_bits[]	= { ANTLR3_UINT64_LIT(0x0000000000000000) };
static  ANTLR3_BITSET_LIST FOLLOW_list_in_synpred1_antlr_cpp35	= { FOLLOW_list_in_synpred1_antlr_cpp35_bits, 1	};
/** Bitset defining follow set for error recovery in rule state: FOLLOW_EOF_in_synpred1_antlr_cpp37  */
static	ANTLR3_BITWORD FOLLOW_EOF_in_synpred1_antlr_cpp37_bits[]	= { ANTLR3_UINT64_LIT(0x0000000000000002) };
static  ANTLR3_BITSET_LIST FOLLOW_EOF_in_synpred1_antlr_cpp37	= { FOLLOW_EOF_in_synpred1_antlr_cpp37_bits, 1	};
     

 
 
/* ==============================================
 * Parsing rules
 */
/** 
 * $ANTLR start prog
 * antlr_cpp.g:8:1: prog : ( list EOF | assign EOF );
 */
static void
prog(pantlr_cppParser ctx)
{   
    /* Initialize rule variables
     */


    {
        {
            //  antlr_cpp.g:8:10: ( list EOF | assign EOF )
            
            ANTLR3_UINT32 alt1;

            alt1=2;


            {
                int LA1_0 = LA(1);
                if ( (LA1_0 == 8) ) 
                {

                    {
                        int LA1_1 = LA(2);
                        if ( (synpred1_antlr_cpp(ctx)) ) 
                        {
                            alt1=1;
                        }
                        else if ( (ANTLR3_TRUE) ) 
                        {
                            alt1=2;
                        }
                        else 
                        {
                            if (BACKTRACKING>0)
                            {
                                FAILEDFLAG = ANTLR3_TRUE; 
                                return ;
                            }
                        
                            CONSTRUCTEX();
                            EXCEPTION->type         = ANTLR3_NO_VIABLE_ALT_EXCEPTION;
                            EXCEPTION->message      = (void *)"";
                            EXCEPTION->decisionNum  = 1;
                            EXCEPTION->state        = 1;


                            goto ruleprogEx;
                        }
                    }
                }
                else 
                {
                    if (BACKTRACKING>0)
                    {
                        FAILEDFLAG = ANTLR3_TRUE; 
                        return ;
                    }
                
                    CONSTRUCTEX();
                    EXCEPTION->type         = ANTLR3_NO_VIABLE_ALT_EXCEPTION;
                    EXCEPTION->message      = (void *)"";
                    EXCEPTION->decisionNum  = 1;
                    EXCEPTION->state        = 0;


                    goto ruleprogEx;
                }
            }
            switch (alt1) 
            {
        	case 1:
        	    // antlr_cpp.g:8:12: list EOF
        	    {
        	        FOLLOWPUSH(FOLLOW_list_in_prog35);
        	        list(ctx);

        	        FOLLOWPOP();
        	        if  (HASEXCEPTION())
        	        {
        	            goto ruleprogEx;
        	        }
        	        if (HASFAILED())
        	        {
        	            return ;
        	        }
        	         MATCHT(EOF, &FOLLOW_EOF_in_prog37); 
        	        if  (HASEXCEPTION())
        	        {
        	            goto ruleprogEx;
        	        }
        	        if (HASFAILED())
        	        {
        	            return ;
        	        }

        	    }
        	    break;
        	case 2:
        	    // antlr_cpp.g:8:23: assign EOF
        	    {
        	        FOLLOWPUSH(FOLLOW_assign_in_prog41);
        	        assign(ctx);

        	        FOLLOWPOP();
        	        if  (HASEXCEPTION())
        	        {
        	            goto ruleprogEx;
        	        }
        	        if (HASFAILED())
        	        {
        	            return ;
        	        }
        	         MATCHT(EOF, &FOLLOW_EOF_in_prog43); 
        	        if  (HASEXCEPTION())
        	        {
        	            goto ruleprogEx;
        	        }
        	        if (HASFAILED())
        	        {
        	            return ;
        	        }

        	    }
        	    break;

            }
        }
    }
    

    // This is where rules clean up and exit
    //
    goto ruleprogEx; /* Prevent compiler warnings */
    ruleprogEx: ;

    if (HASEXCEPTION())
    {
        PREPORTERROR();
        PRECOVER();
    }

    return ;
}
/* $ANTLR end prog */

/** 
 * $ANTLR start assign
 * antlr_cpp.g:9:1: assign : list '=' list ;
 */
static void
assign(pantlr_cppParser ctx)
{   
    /* Initialize rule variables
     */


    {
        // antlr_cpp.g:9:10: ( list '=' list )
        // antlr_cpp.g:9:12: list '=' list
        {
            FOLLOWPUSH(FOLLOW_list_in_assign53);
            list(ctx);

            FOLLOWPOP();
            if  (HASEXCEPTION())
            {
                goto ruleassignEx;
            }
            if (HASFAILED())
            {
                return ;
            }
             MATCHT(7, &FOLLOW_7_in_assign55); 
            if  (HASEXCEPTION())
            {
                goto ruleassignEx;
            }
            if (HASFAILED())
            {
                return ;
            }
            FOLLOWPUSH(FOLLOW_list_in_assign57);
            list(ctx);

            FOLLOWPOP();
            if  (HASEXCEPTION())
            {
                goto ruleassignEx;
            }
            if (HASFAILED())
            {
                return ;
            }

        }

    }
    

    // This is where rules clean up and exit
    //
    goto ruleassignEx; /* Prevent compiler warnings */
    ruleassignEx: ;

    if (HASEXCEPTION())
    {
        PREPORTERROR();
        PRECOVER();
    }

    return ;
}
/* $ANTLR end assign */

/** 
 * $ANTLR start list
 * antlr_cpp.g:10:1: list : '[' elements ']' ;
 */
static void
list(pantlr_cppParser ctx)
{   
    /* Initialize rule variables
     */


    {
        // antlr_cpp.g:10:10: ( '[' elements ']' )
        // antlr_cpp.g:10:12: '[' elements ']'
        {
             MATCHT(8, &FOLLOW_8_in_list69); 
            if  (HASEXCEPTION())
            {
                goto rulelistEx;
            }
            if (HASFAILED())
            {
                return ;
            }
            FOLLOWPUSH(FOLLOW_elements_in_list71);
            elements(ctx);

            FOLLOWPOP();
            if  (HASEXCEPTION())
            {
                goto rulelistEx;
            }
            if (HASFAILED())
            {
                return ;
            }
             MATCHT(9, &FOLLOW_9_in_list73); 
            if  (HASEXCEPTION())
            {
                goto rulelistEx;
            }
            if (HASFAILED())
            {
                return ;
            }

        }

    }
    

    // This is where rules clean up and exit
    //
    goto rulelistEx; /* Prevent compiler warnings */
    rulelistEx: ;

    if (HASEXCEPTION())
    {
        PREPORTERROR();
        PRECOVER();
    }

    return ;
}
/* $ANTLR end list */

/** 
 * $ANTLR start elements
 * antlr_cpp.g:11:1: elements : element ( ',' element )* ;
 */
static void
elements(pantlr_cppParser ctx)
{   
    /* Initialize rule variables
     */


    {
        // antlr_cpp.g:11:10: ( element ( ',' element )* )
        // antlr_cpp.g:11:12: element ( ',' element )*
        {
            FOLLOWPUSH(FOLLOW_element_in_elements89);
            element(ctx);

            FOLLOWPOP();
            if  (HASEXCEPTION())
            {
                goto ruleelementsEx;
            }
            if (HASFAILED())
            {
                return ;
            }

            // antlr_cpp.g:11:20: ( ',' element )*

            for (;;)
            {
                int alt2=2;
                {
                   /* dfaLoopbackState(k,edges,eotPredictsAlt,description,stateNumber,semPredState)
                    */
                    int LA2_0 = LA(1);
                    if ( (LA2_0 == 10) ) 
                    {
                        alt2=1;
                    }

                }
                switch (alt2) 
                {
            	case 1:
            	    // antlr_cpp.g:11:21: ',' element
            	    {
            	         MATCHT(10, &FOLLOW_10_in_elements92); 
            	        if  (HASEXCEPTION())
            	        {
            	            goto ruleelementsEx;
            	        }
            	        if (HASFAILED())
            	        {
            	            return ;
            	        }
            	        FOLLOWPUSH(FOLLOW_element_in_elements94);
            	        element(ctx);

            	        FOLLOWPOP();
            	        if  (HASEXCEPTION())
            	        {
            	            goto ruleelementsEx;
            	        }
            	        if (HASFAILED())
            	        {
            	            return ;
            	        }

            	    }
            	    break;

            	default:
            	    goto loop2;	/* break out of the loop */
            	    break;
                }
            }
            loop2: ; /* Jump out to here if this rule does not match */


        }

    }
    

    // This is where rules clean up and exit
    //
    goto ruleelementsEx; /* Prevent compiler warnings */
    ruleelementsEx: ;

    if (HASEXCEPTION())
    {
        PREPORTERROR();
        PRECOVER();
    }

    return ;
}
/* $ANTLR end elements */

/** 
 * $ANTLR start element
 * antlr_cpp.g:12:1: element : ( NAME '=' NAME | NAME | list );
 */
static void
element(pantlr_cppParser ctx)
{   
    /* Initialize rule variables
     */


    {
        {
            //  antlr_cpp.g:12:10: ( NAME '=' NAME | NAME | list )
            
            ANTLR3_UINT32 alt3;

            alt3=3;


            {
                int LA3_0 = LA(1);
                if ( (LA3_0 == NAME) ) 
                {

                    {
                        int LA3_1 = LA(2);
                        if ( (LA3_1 == 7) ) 
                        {
                            alt3=1;
                        }
                        else if ( (LA3_1 == EOF || ((LA3_1 >= 9) && (LA3_1 <= 10))) ) 
                        {
                            alt3=2;
                        }
                        else 
                        {
                            if (BACKTRACKING>0)
                            {
                                FAILEDFLAG = ANTLR3_TRUE; 
                                return ;
                            }
                        
                            CONSTRUCTEX();
                            EXCEPTION->type         = ANTLR3_NO_VIABLE_ALT_EXCEPTION;
                            EXCEPTION->message      = (void *)"";
                            EXCEPTION->decisionNum  = 3;
                            EXCEPTION->state        = 1;


                            goto ruleelementEx;
                        }
                    }
                }
                else if ( (LA3_0 == 8) ) 
                {
                    alt3=3;
                }
                else 
                {
                    if (BACKTRACKING>0)
                    {
                        FAILEDFLAG = ANTLR3_TRUE; 
                        return ;
                    }
                
                    CONSTRUCTEX();
                    EXCEPTION->type         = ANTLR3_NO_VIABLE_ALT_EXCEPTION;
                    EXCEPTION->message      = (void *)"";
                    EXCEPTION->decisionNum  = 3;
                    EXCEPTION->state        = 0;


                    goto ruleelementEx;
                }
            }
            switch (alt3) 
            {
        	case 1:
        	    // antlr_cpp.g:12:12: NAME '=' NAME
        	    {
        	         MATCHT(NAME, &FOLLOW_NAME_in_element107); 
        	        if  (HASEXCEPTION())
        	        {
        	            goto ruleelementEx;
        	        }
        	        if (HASFAILED())
        	        {
        	            return ;
        	        }
        	         MATCHT(7, &FOLLOW_7_in_element109); 
        	        if  (HASEXCEPTION())
        	        {
        	            goto ruleelementEx;
        	        }
        	        if (HASFAILED())
        	        {
        	            return ;
        	        }
        	         MATCHT(NAME, &FOLLOW_NAME_in_element111); 
        	        if  (HASEXCEPTION())
        	        {
        	            goto ruleelementEx;
        	        }
        	        if (HASFAILED())
        	        {
        	            return ;
        	        }

        	    }
        	    break;
        	case 2:
        	    // antlr_cpp.g:12:28: NAME
        	    {
        	         MATCHT(NAME, &FOLLOW_NAME_in_element115); 
        	        if  (HASEXCEPTION())
        	        {
        	            goto ruleelementEx;
        	        }
        	        if (HASFAILED())
        	        {
        	            return ;
        	        }

        	    }
        	    break;
        	case 3:
        	    // antlr_cpp.g:12:35: list
        	    {
        	        FOLLOWPUSH(FOLLOW_list_in_element119);
        	        list(ctx);

        	        FOLLOWPOP();
        	        if  (HASEXCEPTION())
        	        {
        	            goto ruleelementEx;
        	        }
        	        if (HASFAILED())
        	        {
        	            return ;
        	        }

        	    }
        	    break;

            }
        }
    }
    

    // This is where rules clean up and exit
    //
    goto ruleelementEx; /* Prevent compiler warnings */
    ruleelementEx: ;

    if (HASEXCEPTION())
    {
        PREPORTERROR();
        PRECOVER();
    }

    return ;
}
/* $ANTLR end element */

// $ANTLR start synpred1_antlr_cpp
static void synpred1_antlr_cpp_fragment(pantlr_cppParser ctx ) 
{
    // antlr_cpp.g:8:12: ( list EOF )
    // antlr_cpp.g:8:12: list EOF
    {
        FOLLOWPUSH(FOLLOW_list_in_synpred1_antlr_cpp35);
        list(ctx);

        FOLLOWPOP();
        if  (HASEXCEPTION())
        {
            goto rulesynpred1_antlr_cppEx;
        }
        if (HASFAILED())
        {
            return ;
        }
         MATCHT(EOF, &FOLLOW_EOF_in_synpred1_antlr_cpp37); 
        if  (HASEXCEPTION())
        {
            goto rulesynpred1_antlr_cppEx;
        }
        if (HASFAILED())
        {
            return ;
        }

    }

// This is where rules clean up and exit
//
goto rulesynpred1_antlr_cppEx; /* Prevent compiler warnings */
rulesynpred1_antlr_cppEx: ;

}
// $ANTLR end synpred1_antlr_cpp
/* End of parsing rules
 * ==============================================
 */

/* ==============================================
 * Syntactic predicates
 */
static ANTLR3_BOOLEAN synpred1_antlr_cpp(pantlr_cppParser ctx) 
{
    ANTLR3_MARKER   start;
    ANTLR3_BOOLEAN  success;

    BACKTRACKING++;
    start	= MARK();
    synpred1_antlr_cpp_fragment(ctx);	    // can never throw exception
    success	= !(FAILEDFLAG);
    REWIND(start);
    BACKTRACKING--;
    FAILEDFLAG	= ANTLR3_FALSE;
    return success;
}

/* End of syntactic predicates
 * ==============================================
 */

 
 



/* End of code
 * =============================================================================
 */