%{
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
%}


%option noyywrap
%option caseless

DIGIT [0-9]
NON_ZERO_DIGIT [1-9]
INT_CONSTANT [+-]?{NON_ZERO_DIGIT}{DIGIT}*|0
LETTER [a-zA-Z_]
SPECIAL_CHAR [ ?:*\^+=.!]
STRING_CONSTANT (\"({LETTER}|{DIGIT}|{SPECIAL_CHAR})*\")
IDENTIFIER {LETTER}({LETTER}|{DIGIT})*
BAD_IDENTIFIER ({DIGIT})+({LETTER})+({LETTER}|{DIGIT})*
%%

"$"   {printf("DOLLAR\n");}
"var" {printf("VAR\n");}
"array" {printf("ARRAY\n");}
"list" {printf("LIST\n");}
"read" {printf("READ\n");}
"show" {printf("SHOW\n");}
"if" {printf("IF\n");}
"else" {printf("ELSE\n");}
"for" {printf("FOR\n");}
"while" {printf("WHILE\n");}
"=>" {printf("STMT_SEPARATOR\n");}
"boolean" {printf("BOOLEAN\n");}
"char" {printf("CHAR\n");}
"integer" {printf("INTEGER\n");}
"real" {printf("REAL\n");}

{IDENTIFIER} {printf("IDENTIFIER: %s\n", yytext);}
{INT_CONSTANT} {printf("NUMBER: %s\n", yytext);}
{BAD_IDENTIFIER} {printf("Error at token %s at line %d\n", yytext, lines); exit(1);}
"["|"]"|";"|"("|")"|"{"|"}"|"," {printf("SEPARATOR: %s\n", yytext);}
"+"|"-"|"*"|"/"|"<"|"<="|"="|">="|"=="|"<>"|">"|"!="|"%"|"&&"|"||"|"+="|"-=" {printf("OPERATOR: %s\n", yytext);}
"\n" {printf("NEWLINE\n");}

. {printf("Error at token %s at line %d\n", yytext, lines); exit(1);}

%%

int main(int argc, char **argv) {
    FILE *file;

    if (argc > 1) {
        file = fopen(argv[1], "r");
        if (!file) {
            fprintf(stderr, "Could not open file %s\n", argv[1]);
            return 1;
        }
    } else {
        file = stdin;
    }

    yyin = file;
    yylex();
    fclose(file);
    return 0;
}