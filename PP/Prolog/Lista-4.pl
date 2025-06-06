%NOME: Gabrielli Danker  TURMA: BCC 2022.2  MATÉRIA: Paradigmas de Programação	DATA: 11/10/2022
%Lista 4.

%questão 1
%pai(X, Y)  familia Silva

pai(joao,maria).
pai(joao,pedro).
pai(joao, marcos).
pai(joao, joana).

pai(pedro, ricardo).
pai(pedro, bruno).

pai(bruno, victor).

%questão 2

% pai(X, ricardo)
% X= pedro

%questão 3

sexo(joao, maculino).
sexo(maria, feminino).
sexo(pedro, masculino).
sexo(marcos, masculino).
sexo(joana, feminino).
sexo(ricardo, masculino).
sexo(bruno, masculino).
sexo(victor, masculino).

irmao(X,Y) :- pai(Z,X), pai(Z,Y),
			  sexo(X,masculino),
			  not(X==Y).
irma(X,Y) :- pai(Z,X), pai(Z,Y),
			sexo(X,feminino),
			not(X==Y).

%questão 4

%irma(X,bruno)
%false

%questão 5

neto(X,Y) :- pai(Y,Z), pai(Z,X), sexo(X, masculino).
neta(X,Y) :- pai(Y,Z), pai(Z,X), sexo(X, feminino).

%questão 6

bisneto(X,Y) :- pai(Y,Z), pai(Z,W), pai(W,X), sexo(X, masculino).

%questão 7

aluno(ana).
aluno(gabriel).
aluno(monica).
aluno(henrique).

%questão 8

%nota(X,Y). X= nome Y= nota

nota(ana,10).
nota(gabriel,6).
nota(monica,8).
nota(henrique,5).

%questão 9

%passou(X) X= aluno, se X>= 7, aluno passou

passou(X) :- aluno(X), 
    		nota(X,Y),
    		Y>=7.

%questão 10

%além da Y>=7, frequencia tem que ser >= a 75

frequencia(ana, 60).
frequencia(gabriel, 98).
frequencia(monica, 75).
frequencia(henrique,100).

passou2(X) :- aluno(X),
    		nota(X,Y),
    		Y>=7,
    		frequencia(X,Z),
    		Z>=75.
