tree grammar eval;

options {
  language = Python;
  output = AST;
  tokenVocab = ExprAst;
  ASTLabelType = CommonTree;
}

rule: ;
