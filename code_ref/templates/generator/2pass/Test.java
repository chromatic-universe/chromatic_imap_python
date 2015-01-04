/***
 * Excerpted from "The Definitive ANTLR Reference",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material, 
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose. 
 * Visit http://www.pragmaticprogrammer.com/titles/tpantlr for more book information.
***/
import org.antlr.runtime.*;
import org.antlr.runtime.tree.*;
import org.antlr.stringtemplate.*;
import java.io.*;

public class Test {
    public static void main(String[] args) throws Exception {
        // load the group file ByteCode.stg, put in templates var
        FileReader groupFileR = new FileReader("ByteCode.stg");
        StringTemplateGroup templates =
            new StringTemplateGroup(groupFileR);
        groupFileR.close();

        // PARSE INPUT AND BUILD AST
        ANTLRInputStream input = new ANTLRInputStream(System.in);
        ExprLexer lexer = new ExprLexer(input);     // create lexer
        // create a buffer of tokens pulled from the lexer
        CommonTokenStream tokens = new CommonTokenStream(lexer);
        ExprParser parser = new ExprParser(tokens); // create parser
        ExprParser.prog_return r = parser.prog();   // parse rule prog

        // WALK TREE
        // get the tree from the return structure for rule prog
        CommonTree t = (CommonTree)r.getTree();
        // create a stream of tree nodes from AST built by parser
        CommonTreeNodeStream nodes = new CommonTreeNodeStream(t);
        // tell it where it can find the token objects
        nodes.setTokenStream(tokens);
        Gen walker = new Gen(nodes); // create the tree Walker
        walker.setTemplateLib(templates); // where to find templates
        // invoke rule prog, passing in information from parser
        Gen.prog_return r2 = walker.prog(parser.numOps, parser.locals);

        // EMIT BYTE CODES
        // get template from return values struct
	StringTemplate output = (StringTemplate)r2.getTemplate(); 
        System.out.println(output.toString()); // render full template
    }
}
