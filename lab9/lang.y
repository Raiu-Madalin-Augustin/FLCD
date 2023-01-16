%{
#include <stdio.h>
#include <stdlib.h>

int yyerror(char *s);

#define YYDEBUG 1
%}

%token VAR
%token BOOLEAN
%token CHAR
%token INTEGER
%token REAL
%token IDENTIFIER
%token ARRAY
%token LIST
%token NR
%token READ
%token SHOW
%token IF
%token ELSE
%token WHILE
%token FOR
%token FORSTMT
%token CONDITION
%token RELATION
%token LESS
%token LESSEQ
%token EQ
%token NEQ
%token BIGGEREQ
%token EQQ
%token BIGGER
%token EXPRESSION
%token TERM
%token FACTOR
%token CMPSTMT

%start Program

%%
Program : $ DeclList CmpdStmt $    { printf("Program -> $ DeclList CmpdStmt $\n"); }
        ;
DeclList : Declaration    { printf("DeclList -> Declaration\n"); }
         | Declaration ';' DeclList    { printf("DeclList -> Declaration ; DeclList\n"); }
         ;
Declaration : VAR IDENTIFIER ':' Type    { printf("Declaration -> VAR IDENTIFIER : Type\n"); }
            ;
Type : Type1    { printf("Type -> Type1\n"); }
     | ArrayDecl    { printf("Type -> ArrayDecl\n"); }
     | ListDecl    { printf("Type -> ListDecl\n"); }
     ;
Type1 : BOOLEAN    { printf("Type1 -> BOOLEAN\n"); }
      | CHAR    { printf("Type1 -> CHAR\n"); }
      | INTEGER    { printf("Type1 -> INTEGER\n"); }
      | REAL    { printf("Type1 -> REAL\n"); }
      ;

AssignmentStatement : IDENTIFIER EQ Expression     { printf("AssignmentStatement -> IDENTIFIER = Expression\n"); }
                    | IDENTIFIER EQ ArrayStatement     { printf("AssignmentStatement -> IDENTIFIER = ArrayStatement\n"); }
                    ;
Expression : Expression PLUS Term     { printf("Expression -> Expression + Term\n"); }
           | Expression MINUS Term     { printf("Expression -> Expression - Term\n"); }
           | Term     { printf("Expression -> Term\n"); }
           ;
Term : Term TIMES Factor     { printf("Term -> Term * Factor\n"); }
     | Term DIV Factor     { printf("Term -> Term / Factor\n"); }
     | Factor     { printf("Term -> Factor\n"); }
     ;
Factor : OPEN Expression CLOSE     { printf("Factor -> ( Expression )\n"); }
       | IDENTIFIER     { printf("Factor -> IDENTIFIER\n"); }
       | INTCONSTANT     { printf("Factor -> INTCONSTANT\n"); }
       | MINUS IDENTIFIER     { printf("Factor -> - IDENTIFIER\n"); }
       | SQRT OPEN Expression CLOSE     { printf("Factor -> sqrt ( Expression )\n"); }
       ;
ArrayDecl : VAR IDENTIFIER ':' ARRAY '[' NR ']' ':' Type1    { printf("ArrayDecl -> VAR IDENTIFIER : ARRAY [ NR ] : Type1\n"); }
          ;
ListDecl : VAR IDENTIFIER ':' LIST '[' NR ']' ':' Type1    { printf("ListDecl -> VAR IDENTIFIER : LIST [ NR ] : Type1\n"); }
         ;
IOStmt : READ IDENTIFIER    { printf("IOStmt -> READ IDENTIFIER\n"); }
       | SHOW IDENTIFIER    { printf("IOStmt -> SHOW IDENTIFIER\n"); }
       ;
IfStmt : IF CONDITION '=>' CmpdStmt ELSE '=>' CmpdStmt    { printf("IfStmt -> IF CONDITION => CmpdStmt ELSE => CmpdStmt\n"); }
       ;
WhileStmt : WHILE CONDITION '=>' CmpdStmt    { printf("WhileStmt -> WHILE CONDITION => CmpdStmt\n"); }
         ;
ForStmt : FOR FORSTMT ';' IDENTIFIER RELATION IDENTIFIER ';' IDENTIFIER EXPRESSION '=>' CmpdStmt    { printf("ForStmt -> FOR FORSTMT ; IDENTIFIER RELATION IDENTIFIER ;
 IDENTIFIER EXPRESSION => CmpdStmt\n"); }

Condition : Expression Relation Expression     { printf("Condition -> Expression Relation Expression\n"); }
          ;
Relation : LESS     { printf("Relation -> <\n"); }
         | LESSEQ     { printf("Relation -> <=\n"); }
         | EQQ     { printf("Relation -> ==\n"); }
         | NEQ     { printf("Relation -> <>\n"); }
         | BIGGEREQ     { printf("Relation -> >=\n"); }
         | BIGGER     { printf("Relation -> >\n"); }
         ;

%%
int yyerror(char *s) {
    printf("Error: %s", s);
}

extern FILE *yyin;

int main(int argc, char** argv) {
    if (argc > 1) 
        yyin = fopen(argv[1], "r");
    if (!yyparse()) 
        fprintf(stderr, "\tOK\n");
}