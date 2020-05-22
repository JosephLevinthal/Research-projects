/* 
Autor: Joseph Levinthal
E-mail: jvlo@icomp.ufam.edu.br
Projeto: PIBIC (2018 / 2019) - Geração de ajuda personalizada para estudantes de programação em um ambiente de correção automática de códigos.
Data: 25/09/2018.
------------------------------------------------------------------------------------------------------------------------------------------
Este arquivo foi criado para documentar algumas informações sobre meu trabalho com geração de dicas do Codebench, para a utilização futura, caso algum aluno de PIBIC trabalhe com um tema parecido e não queira/precise partir do 0, ou que precise de ajuda em algum aspecto qualquer do trabalho com o Codebench. Espero que seja útil =).
------------------------------------------------------------------------------------------------------------------------------------------
Este arquivo contém:
- Informações retiradas da coluna "executavel_erro" da tabela "submissao" do bando de dados do Codebench;
- Informações sobre quais e quantos erros foram submetidos pelos alunos de IPC durante o período estudado (2016/01 até 2018/01), ordenados pelo número de ocorrências;
- Requisições SQL para filtrar o número total de erros, ou filtrá-los separadamente.
------------------------------------------------------------------------------------------------------------------------------------------
Erros tabelados em CSV e descritos neste arquivo, ordenados pelo número de ocorrências:
0 - Numero total de erros - 129780;
1 - SyntaxError - 39361;
2 - NameError - 27334;
3 - ValueError - 12025;
4 - IndentationError - 12020;
5 - TypeError - 10611;
6 - EOFError - 7923;
7 - IndexError - 4153;
8 - UnicodeEncodeError - 3337;
9 - ZeroDivisionError - 2710;
10 - TabError - 2599;
11 - Warning - 1109;
12 - AttributeError - 881;
13 - DeprecationWarning - 813;
14 - ImportError - 387;
15 - RuntimeWarning - 269;
16 - OverflowError - 213;

Erros tabelados em CSV, porém DESCARTADOS deste arquivo por terem menos de 28 ocorrências das 129780 submissões (numero total de erros) das turmas de IPC:
- Exception
- UnboundLocalError
- UnicodeDecodeError
- PermissionError
- AssertionError
- KeyError
- FutureWarning
- MemoryError
------------------------------------------------------------------------------------------------------------------------------------------
Padrão de cada seção:
"NomeDoErro - NumeroTotalDeSubmissoes (erros encontrados)"
"requisições SQL para extrair os erros da coluna executavel_erro da tabela submissao do Codebench"
"CasosDoErroMaisEspecificos - NumeroTotalSubmissoes (erros encontrados)"
------------------------------------------------------------------------------------------------------------------------------------------
Notas:
* Edição do arquivo feita utilizando o editor VSCode, podendo ter uma formatação e visualização diferentes em outros editores de texto.
** Utilização de visualização do arquivo como "SQL", no próprio VSCode, para "Syntax highlight" das requisições SQL e dos comentários, sendo incentivado o uso para uma leitura mais "agradável" do arquivo.
------------------------------------------------------------------------------------------------------------------------------------------

/*Todos os erros em Python, mas somente das turmas de IPC - 129780*/

select submissao.*
from submissao inner join codigo_fonte on codigo_fonte.id = submissao.id_codigo_fonte inner join trabalho on codigo_fonte.id_trabalho = trabalho.id inner join turma on trabalho.id_turma = turma.id inner join disciplina on turma.id_disciplina = disciplina.id
WHERE (disciplina.codigo="IEC037" OR disciplina.codigo="IEC081") AND trabalho.id_linguagem = 3 AND length(executavel_erro)>0;

------------------------------------------------------------------------------------------------------------------------------------------

/*SyntaxError - 39361*/

select submissao.*
from submissao inner join codigo_fonte on codigo_fonte.id = submissao.id_codigo_fonte inner join trabalho on codigo_fonte.id_trabalho = trabalho.id inner join turma on trabalho.id_turma = turma.id inner join disciplina on turma.id_disciplina = disciplina.id
WHERE (disciplina.codigo="IEC037" OR disciplina.codigo="IEC081") AND trabalho.id_linguagem = 3 AND length(executavel_erro)>0 AND executavel_erro LIKE '%SyntaxError%'

select submissao.*
from submissao inner join codigo_fonte on codigo_fonte.id = submissao.id_codigo_fonte inner join trabalho on codigo_fonte.id_trabalho = trabalho.id inner join turma on trabalho.id_turma = turma.id inner join disciplina on turma.id_disciplina = disciplina.id
WHERE (disciplina.codigo="IEC037" OR disciplina.codigo="IEC081") AND trabalho.id_linguagem = 3 AND length(executavel_erro)>0 AND executavel_erro LIKE "%SyntaxError%" AND executavel_erro NOT LIKE '%SyntaxError: invalid syntax%' AND executavel_erro NOT LIKE '%SyntaxError: unexpected EOF while parsing%' AND executavel_erro NOT LIKE '%SyntaxError: EOL while scanning string literal%' AND executavel_erro NOT LIKE "%SyntaxError: Missing parentheses in call to 'print'%" AND executavel_erro NOT LIKE "%SyntaxError: keyword can't be an expression%" AND executavel_erro NOT LIKE "%SyntaxError: invalid token%" AND executavel_erro NOT LIKE "%SyntaxError: EOF while scanning triple-quoted string literal%" AND executavel_erro NOT LIKE '%SyntaxError: invalid character in identifier%' AND executavel_erro NOT LIKE "%SyntaxError: unexpected character after line continuation character%" AND executavel_erro NOT LIKE "%SyntaxError: can't assign to literal%" AND executavel_erro NOT LIKE "%SyntaxError: can't assign to function call%" AND executavel_erro NOT LIKE "%SyntaxError: positional argument follows keyword argument%" AND executavel_erro NOT LIKE "%SyntaxError: can't assign to operator%" AND executavel_erro NOT LIKE "%SyntaxError: can't use starred expression here%" AND executavel_erro NOT LIKE "%SyntaxError: starred assignment target must be in a list or tuple%" AND executavel_erro NOT LIKE "%SyntaxError: 'break' outside loop%" AND executavel_erro NOT LIKE "%SyntaxError: 'return' outside function%" AND executavel_erro NOT LIKE "%SyntaxError: can use starred expression only as assignment target%" AND executavel_erro NOT LIKE "%SyntaxError: non-keyword arg after keyword arg%"

select submissao.*
from submissao inner join codigo_fonte on codigo_fonte.id = submissao.id_codigo_fonte inner join trabalho on codigo_fonte.id_trabalho = trabalho.id inner join turma on trabalho.id_turma = turma.id inner join disciplina on turma.id_disciplina = disciplina.id
WHERE (disciplina.codigo="IEC037" OR disciplina.codigo="IEC081") AND trabalho.id_linguagem = 3 AND length(executavel_erro)>0 AND executavel_erro LIKE '%SyntaxError: invalid syntax%' AND executavel_erro LIKE '%print%'

/* (OK)
Caso 1 - SyntaxError: invalid syntax - 32342
Caso 2 - SyntaxError: unexpected EOF while parsing - 3580
Caso 3 - SyntaxError: EOL while scanning string literal - 1431
Caso 4 - SyntaxError: invalid character in identifier - 648
Caso 5 - SyntaxError: can't assign to operator - 499
Caso 6 - SyntaxError: Missing parentheses in call to 'print' - 220
Caso 7 - SyntaxError: can't assign to function call - 175
Caso 8 - SyntaxError: can't assign to literal - 120
Caso 9 - SyntaxError: keyword can't be an expression - 117
Caso 10 - SyntaxError: invalid token - 83
Caso 11 - SyntaxError: unexpected character after line continuation character - 60
Caso 12 - SyntaxError: EOF while scanning triple-quoted string literal - 26
Caso 13 - SyntaxError: can't use starred expression here - 19
Caso 14 - SyntaxError: positional argument follows keyword argument - 17 
Caso 15 - SyntaxError: 'return' outside function - 7
Caso 16 - SyntaxError: 'break' outside loop - 6
Caso 17 - SyntaxError: can use starred expression only as assignment target - 6
Caso 18 - SyntaxError: non-keyword arg after keyword arg - 3
Caso 19 - SyntaxError: starred assignment target must be in a list or tuple - 2
------------------------------------------------------------------------------------------------------------------------------------------

/*NameError - 27334*/

select submissao.*
from submissao inner join codigo_fonte on codigo_fonte.id = submissao.id_codigo_fonte inner join trabalho on codigo_fonte.id_trabalho = trabalho.id inner join turma on trabalho.id_turma = turma.id inner join disciplina on turma.id_disciplina = disciplina.id
WHERE (disciplina.codigo="IEC037" OR disciplina.codigo="IEC081") AND trabalho.id_linguagem = 3 AND length(executavel_erro)>0 AND executavel_erro LIKE '%NameError%'

select submissao.*
from submissao inner join codigo_fonte on codigo_fonte.id = submissao.id_codigo_fonte inner join trabalho on codigo_fonte.id_trabalho = trabalho.id inner join turma on trabalho.id_turma = turma.id inner join disciplina on turma.id_disciplina = disciplina.id
WHERE (disciplina.codigo="IEC037" OR disciplina.codigo="IEC081") AND trabalho.id_linguagem = 3 AND length(executavel_erro)>0 AND executavel_erro LIKE '%is not defined%'

/* (OK)
Caso 1 -  NameError: name 'NOMEDAVARIAVEL' is not defined - 27334
------------------------------------------------------------------------------------------------------------------------------------------

/*ValueError - 12025*/

select submissao.*
from submissao inner join codigo_fonte on codigo_fonte.id = submissao.id_codigo_fonte inner join trabalho on codigo_fonte.id_trabalho = trabalho.id inner join turma on trabalho.id_turma = turma.id inner join disciplina on turma.id_disciplina = disciplina.id
WHERE (disciplina.codigo="IEC037" OR disciplina.codigo="IEC081") AND trabalho.id_linguagem = 3 AND length(executavel_erro)>0 AND executavel_erro LIKE '%ValueError%'

select submissao.*
from submissao inner join codigo_fonte on codigo_fonte.id = submissao.id_codigo_fonte inner join trabalho on codigo_fonte.id_trabalho = trabalho.id inner join turma on trabalho.id_turma = turma.id inner join disciplina on turma.id_disciplina = disciplina.id
WHERE (disciplina.codigo="IEC037" OR disciplina.codigo="IEC081") AND trabalho.id_linguagem = 3 AND length(executavel_erro)>0 AND executavel_erro LIKE '%ValueError%' AND executavel_erro NOT LIKE '%ValueError: invalid literal for int() with base 10%' AND executavel_erro NOT LIKE '%ValueError: could not convert string to float%' AND executavel_erro NOT LIKE '%ValueError: math domain error%' AND executavel_erro NOT LIKE '%ValueError: int() base must be%' AND executavel_erro NOT LIKE '%ValueError: not enough values to unpack%' AND executavel_erro NOT LIKE '%ValueError: factorial() only accepts integral values%' AND executavel_erro NOT LIKE '%ValueError: factorial() not defined for negative values%' AND executavel_erro NOT LIKE '%ValueError: setting an array element with a sequence%' AND executavel_erro NOT LIKE '%ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()%'

/*
Caso 1 - ValueError: invalid literal for int() with base 10 - 9814
Caso 2 - ValueError: could not convert string to float - 1005
Caso 3 - ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()  - 523
Caso 4 - ValueError: math domain error - 224
Caso 5 - ValueError: setting an array element with a sequence - 71
Caso 6 - ValueError: factorial() only accepts integral values - 56
Caso 7 - ValueError: int() base must be >= 2 and <= 36 - 10
Caso 8 - ValueError: factorial() not defined for negative values - 13
Caso 9 - ValueError: not enough values to unpack - 1
Caso 10 - FALTAM 308
------------------------------------------------------------------------------------------------------------------------------------------

/*IndentationError - 12020*/

select submissao.*
from submissao inner join codigo_fonte on codigo_fonte.id = submissao.id_codigo_fonte inner join trabalho on codigo_fonte.id_trabalho = trabalho.id inner join turma on trabalho.id_turma = turma.id inner join disciplina on turma.id_disciplina = disciplina.id
WHERE (disciplina.codigo="IEC037" OR disciplina.codigo="IEC081") AND trabalho.id_linguagem = 3 AND length(executavel_erro)>0 AND executavel_erro LIKE "%IndentationError%"

select submissao.*
from submissao inner join codigo_fonte on codigo_fonte.id = submissao.id_codigo_fonte inner join trabalho on codigo_fonte.id_trabalho = trabalho.id inner join turma on trabalho.id_turma = turma.id inner join disciplina on turma.id_disciplina = disciplina.id
WHERE (disciplina.codigo="IEC037" OR disciplina.codigo="IEC081") AND trabalho.id_linguagem = 3 AND length(executavel_erro)>0 AND executavel_erro LIKE "%IndentationError%" AND executavel_erro NOT LIKE '%IndentationError: unexpected indent%' AND executavel_erro NOT LIKE "%IndentationError: Missing parentheses in call to 'print'%" AND executavel_erro NOT LIKE "%IndentationError: expected an indented block%" AND executavel_erro NOT LIKE "%IndentationError: unindent does not match any outer indentation level%"

/* (OK)
Caso 1 - IndentationError: expected an indented block - 4254 
Caso 2 - IndentationError: unindent does not match any outer indentation level - 4080
Caso 3 - IndentationError: unexpected indent - 3676
Caso 4 - IndentationError: Missing parentheses in call to 'print' - 10
------------------------------------------------------------------------------------------------------------------------------------------

/*TypeError - 10611*/

select submissao.*
from submissao inner join codigo_fonte on codigo_fonte.id = submissao.id_codigo_fonte inner join trabalho on codigo_fonte.id_trabalho = trabalho.id inner join turma on trabalho.id_turma = turma.id inner join disciplina on turma.id_disciplina = disciplina.id
WHERE (disciplina.codigo="IEC037" OR disciplina.codigo="IEC081") AND trabalho.id_linguagem = 3 AND length(executavel_erro)>0 AND executavel_erro LIKE '%TypeError%'

select submissao.*
from submissao inner join codigo_fonte on codigo_fonte.id = submissao.id_codigo_fonte inner join trabalho on codigo_fonte.id_trabalho = trabalho.id inner join turma on trabalho.id_turma = turma.id inner join disciplina on turma.id_disciplina = disciplina.id
WHERE (disciplina.codigo="IEC037" OR disciplina.codigo="IEC081") AND trabalho.id_linguagem = 3 AND length(executavel_erro)>0 AND executavel_erro LIKE "%TypeError%" AND executavel_erro NOT LIKE "%TypeError: unsupported operand type(s)%" AND executavel_erro NOT LIKE "%object is not callable%" AND executavel_erro NOT LIKE "%takes%" AND executavel_erro NOT LIKE "%can't multiply sequence%" AND executavel_erro NOT LIKE "%cannot be interpreted as%" AND executavel_erro NOT LIKE "%invalid keyword argument%" AND executavel_erro NOT LIKE "%can't convert%" AND executavel_erro NOT LIKE "%doesn't define __round__ method%" AND executavel_erro NOT LIKE "%input expected%" AND executavel_erro NOT LIKE "%argument must be%" AND executavel_erro NOT LIKE '%TypeError: can only concatenate%' AND executavel_erro NOT LIKE '%object is not iterable%' AND executavel_erro NOT LIKE '%is required%' AND executavel_erro NOT LIKE '%TypeError: not all arguments converted during string formatting%' AND executavel_erro NOT LIKE '%TypeError: bad operand type for%' AND executavel_erro NOT LIKE '%TypeError: print() argument after%' AND executavel_erro NOT LIKE '%TypeError: unorderable types:%' AND executavel_erro NOT LIKE "%TypeError: Required argument%" AND executavel_erro NOT LIKE "%must be a string, bytes or code object%" AND executavel_erro NOT LIKE "%TypeError: round() argument after ** must be a mapping, not float%" AND executavel_erro NOT LIKE "%required positional argument%" AND executavel_erro NOT LIKE "%object is not subscriptable%" AND executavel_erro NOT LIKE "%TypeError: cannot perform reduce with flexible type%" AND executavel_erro NOT LIKE "%TypeError: iteration over a 0-d array%" AND executavel_erro NOT LIKE "%object argument after%" AND executavel_erro NOT LIKE "%does not support item assignment%" AND executavel_erro NOT LIKE "%TypeError: slice indices must be%" AND executavel_erro NOT LIKE "%TypeError: Argument given by name%"

/*
Caso 1 - TypeError: unsupported operand type(s) - 2085
Caso 2 - doesn't define __round__ method - 1446
Caso 3 - object is not callable - 1444
Caso 4 - can't multiply sequence - 709
Caso 5 - object is not subscriptable - 668
Caso 6 - takes - 633
Caso 7 - object is not iterable - 447
Caso 8 -  TypeError: unorderable types: - 409
Caso 9 - Can't convert - 390
Caso 10 - cannot be interpreted as - 312
Caso 11 - argument must be - 224
Caso 12 - TypeError: not all arguments converted during string formatting - 197
Caso 13 - TypeError: "NOME DA VARIAVEL" is an invalid keyword argument for this function - 172
Caso 14 - does not support item assignment - 105
Caso 15 - TypeError AND "is required" - 98
Caso 16 - must be a string, bytes or code object - 86
Caso 17 - TypeError: Required argument - 69
Caso 18 - TypeError: bad operand type for - 45
Caso 19 - TypeError: iteration over a 0-d array - 44
Caso 20 - input expected - 30
Caso 21 - required positional argument - 29
Caso 22 - TypeError: can only concatenate - 28
Caso 23 - TypeError: cannot perform reduce with flexible type - 21
Caso 24 - TypeError: Argument given by name - 15
Caso 25 - TypeError: print() argument after - 8
Caso 26 - object argument after - 4
Caso 27 - TypeError: round() argument after ** must be a mapping, not float - 3
Caso 28 - TypeError: slice indices must be - 2
Caso 29 -  FALTAM 888

------------------------------------------------------------------------------------------------------------------------------------------

/*EOFError - 7923*/

select submissao.*
from submissao inner join codigo_fonte on codigo_fonte.id = submissao.id_codigo_fonte inner join trabalho on codigo_fonte.id_trabalho = trabalho.id inner join turma on trabalho.id_turma = turma.id inner join disciplina on turma.id_disciplina = disciplina.id
WHERE (disciplina.codigo="IEC037" OR disciplina.codigo="IEC081") AND trabalho.id_linguagem = 3 AND length(executavel_erro)>0 AND executavel_erro LIKE '%EOFError%'

select submissao.*
from submissao inner join codigo_fonte on codigo_fonte.id = submissao.id_codigo_fonte inner join trabalho on codigo_fonte.id_trabalho = trabalho.id inner join turma on trabalho.id_turma = turma.id inner join disciplina on turma.id_disciplina = disciplina.id
WHERE (disciplina.codigo="IEC037" OR disciplina.codigo="IEC081") AND trabalho.id_linguagem = 3 AND length(executavel_erro)>0 AND executavel_erro LIKE '%EOFError: EOF when reading a line%'

/* (OK)
Caso 1 - EOFError: EOF when reading a line - 7923 

------------------------------------------------------------------------------------------------------------------------------------------

/*IndexError - 4153*/

select submissao.*
from submissao inner join codigo_fonte on codigo_fonte.id = submissao.id_codigo_fonte inner join trabalho on codigo_fonte.id_trabalho = trabalho.id inner join turma on trabalho.id_turma = turma.id inner join disciplina on turma.id_disciplina = disciplina.id
WHERE (disciplina.codigo="IEC037" OR disciplina.codigo="IEC081") AND trabalho.id_linguagem = 3 AND length(executavel_erro)>0 AND executavel_erro LIKE '%IndexError%'

select submissao.*
from submissao inner join codigo_fonte on codigo_fonte.id = submissao.id_codigo_fonte inner join trabalho on codigo_fonte.id_trabalho = trabalho.id inner join turma on trabalho.id_turma = turma.id inner join disciplina on turma.id_disciplina = disciplina.id
WHERE (disciplina.codigo="IEC037" OR disciplina.codigo="IEC081") AND trabalho.id_linguagem = 3 AND length(executavel_erro)>0 AND executavel_erro LIKE '%IndexError%' AND executavel_erro NOT LIKE '%out of bounds for axis%' AND executavel_erro NOT LIKE '%IndexError: list index out of range%' AND executavel_erro NOT LIKE '%IndexError: tuple index out of range%' AND executavel_erro NOT LIKE '%IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices%' AND executavel_erro NOT LIKE '%IndexError: list assignment index out of range%' AND executavel_erro NOT LIKE '%IndexError: too many indices for array%' AND executavel_erro NOT LIKE '%IndexError: string index out of range%' AND executavel_erro NOT LIKE '%IndexError: invalid index to scalar variable.%' AND executavel_erro NOT LIKE '%IndexError: arrays used as indices must be of integer (or boolean) type%'

/* (OK)
Caso 1 - is out of bounds for axis - 2903
Caso 2 - IndexError: too many indices for array - 553
Caso 3 - IndexError: string index out of range - 215
Caso 4 - IndexError: tuple index out of range - 209
Caso 5 - IndexError: list index out of range - 105
Caso 6 - IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices - 74
Caso 7 - IndexError: invalid index to scalar variable. - 58
Caso 8 - IndexError: arrays used as indices must be of integer (or boolean) type - 18
Caso 9 - IndexError: list assignment index out of range - 13
Caso 10 - IndexError: failed to coerce slice entry of type numpy.ndarray to integer - 4
Caso 11 - IndexError: range object index out of range - 1

------------------------------------------------------------------------------------------------------------------------------------------

/*UnicodeEncodeError - 3337*/

select submissao.*
from submissao inner join codigo_fonte on codigo_fonte.id = submissao.id_codigo_fonte inner join trabalho on codigo_fonte.id_trabalho = trabalho.id inner join turma on trabalho.id_turma = turma.id inner join disciplina on turma.id_disciplina = disciplina.id
WHERE (disciplina.codigo="IEC037" OR disciplina.codigo="IEC081") AND trabalho.id_linguagem = 3 AND length(executavel_erro)>0 AND executavel_erro LIKE '%UnicodeEncodeError%'

------------------------------------------------------------------------------------------------------------------------------------------

/*ZeroDivisionError - 2710*/

select submissao.*
from submissao inner join codigo_fonte on codigo_fonte.id = submissao.id_codigo_fonte inner join trabalho on codigo_fonte.id_trabalho = trabalho.id inner join turma on trabalho.id_turma = turma.id inner join disciplina on turma.id_disciplina = disciplina.id
WHERE (disciplina.codigo="IEC037" OR disciplina.codigo="IEC081") AND trabalho.id_linguagem = 3 AND length(executavel_erro)>0 AND executavel_erro LIKE '%ZeroDivisionError%'

select submissao.*
from submissao inner join codigo_fonte on codigo_fonte.id = submissao.id_codigo_fonte inner join trabalho on codigo_fonte.id_trabalho = trabalho.id inner join turma on trabalho.id_turma = turma.id inner join disciplina on turma.id_disciplina = disciplina.id
WHERE (disciplina.codigo="IEC037" OR disciplina.codigo="IEC081") AND trabalho.id_linguagem = 3 AND length(executavel_erro)>0 AND executavel_erro LIKE '%ZeroDivisionError%' AND executavel_erro NOT LIKE '%float division by zero%' AND executavel_erro NOT LIKE '%division by zero%' AND executavel_erro NOT LIKE '%integer division or modulo by zero%'

/* (OK)
Caso 1 - ZeroDivisionError: float division by zero - 2349
Caso 2 - ZeroDivisionError: division by zero - 244
Caso 3 - ZeroDivisionError: float modulo - 66
Caso 4 - ZeroDivisionError: integer division or modulo by zero - 51
------------------------------------------------------------------------------------------------------------------------------------------

/*TabError - 2599*/

select submissao.*
from submissao inner join codigo_fonte on codigo_fonte.id = submissao.id_codigo_fonte inner join trabalho on codigo_fonte.id_trabalho = trabalho.id inner join turma on trabalho.id_turma = turma.id inner join disciplina on turma.id_disciplina = disciplina.id
WHERE (disciplina.codigo="IEC037" OR disciplina.codigo="IEC081") AND trabalho.id_linguagem = 3 AND length(executavel_erro)>0 AND executavel_erro LIKE '%TabError%'

select submissao.*
from submissao inner join codigo_fonte on codigo_fonte.id = submissao.id_codigo_fonte inner join trabalho on codigo_fonte.id_trabalho = trabalho.id inner join turma on trabalho.id_turma = turma.id inner join disciplina on turma.id_disciplina = disciplina.id
WHERE (disciplina.codigo="IEC037" OR disciplina.codigo="IEC081") AND trabalho.id_linguagem = 3 AND length(executavel_erro)>0 AND executavel_erro LIKE '%TabError%' AND executavel_erro LIKE '%TabError: inconsistent use of tabs and spaces in indentation%'

/*  (OK)
Caso 1 - TabError: inconsistent use of tabs and spaces in indentation - 2598
Caso 2 - TabError: Missing parentheses in call to 'print' - 1
------------------------------------------------------------------------------------------------------------------------------------------

/*Warning - 1109*/

select submissao.*
from submissao inner join codigo_fonte on codigo_fonte.id = submissao.id_codigo_fonte inner join trabalho on codigo_fonte.id_trabalho = trabalho.id inner join turma on trabalho.id_turma = turma.id inner join disciplina on turma.id_disciplina = disciplina.id
WHERE (disciplina.codigo="IEC037" OR disciplina.codigo="IEC081") AND trabalho.id_linguagem = 3 AND length(executavel_erro)>0 AND executavel_erro LIKE '%Warning%'

------------------------------------------------------------------------------------------------------------------------------------------

/*AttributeError - 881*/

select submissao.*
from submissao inner join codigo_fonte on codigo_fonte.id = submissao.id_codigo_fonte inner join trabalho on codigo_fonte.id_trabalho = trabalho.id inner join turma on trabalho.id_turma = turma.id inner join disciplina on turma.id_disciplina = disciplina.id
WHERE (disciplina.codigo="IEC037" OR disciplina.codigo="IEC081") AND trabalho.id_linguagem = 3 AND length(executavel_erro)>0 AND executavel_erro LIKE '%AttributeError%'

------------------------------------------------------------------------------------------------------------------------------------------

/*DeprecationWarning - 813*/

select submissao.*
from submissao inner join codigo_fonte on codigo_fonte.id = submissao.id_codigo_fonte inner join trabalho on codigo_fonte.id_trabalho = trabalho.id inner join turma on trabalho.id_turma = turma.id inner join disciplina on turma.id_disciplina = disciplina.id
WHERE (disciplina.codigo="IEC037" OR disciplina.codigo="IEC081") AND trabalho.id_linguagem = 3 AND length(executavel_erro)>0 AND executavel_erro LIKE '%DeprecationWarning%'

------------------------------------------------------------------------------------------------------------------------------------------

/*ImportError - 387*/

select submissao.*
from submissao inner join codigo_fonte on codigo_fonte.id = submissao.id_codigo_fonte inner join trabalho on codigo_fonte.id_trabalho = trabalho.id inner join turma on trabalho.id_turma = turma.id inner join disciplina on turma.id_disciplina = disciplina.id
WHERE (disciplina.codigo="IEC037" OR disciplina.codigo="IEC081") AND trabalho.id_linguagem = 3 AND length(executavel_erro)>0 AND executavel_erro LIKE '%ImportError%'

------------------------------------------------------------------------------------------------------------------------------------------

/*RuntimeWarning - 269*/

select submissao.*
from submissao inner join codigo_fonte on codigo_fonte.id = submissao.id_codigo_fonte inner join trabalho on codigo_fonte.id_trabalho = trabalho.id inner join turma on trabalho.id_turma = turma.id inner join disciplina on turma.id_disciplina = disciplina.id
WHERE (disciplina.codigo="IEC037" OR disciplina.codigo="IEC081") AND trabalho.id_linguagem = 3 AND length(executavel_erro)>0 AND executavel_erro LIKE '%RuntimeWarning%'

------------------------------------------------------------------------------------------------------------------------------------------

/*OverflowError - 213*/

select submissao.*
from submissao inner join codigo_fonte on codigo_fonte.id = submissao.id_codigo_fonte inner join trabalho on codigo_fonte.id_trabalho = trabalho.id inner join turma on trabalho.id_turma = turma.id inner join disciplina on turma.id_disciplina = disciplina.id
WHERE (disciplina.codigo="IEC037" OR disciplina.codigo="IEC081") AND trabalho.id_linguagem = 3 AND length(executavel_erro)>0 AND executavel_erro LIKE '%OverflowError%'

------------------------------------------------------------------------------------------------------------------------------------------




