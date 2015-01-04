grammar descent;

options
{
  language = Python;
}


prog          : stat+      ;
              

stat            :   list  ;
list            :   '[' elements ']'  ;
elements        :   element ( ',' element )* ;
element         :   NAME | list ;
NAME            :   ('a'..'z' | 'A'..'Z')+  ;