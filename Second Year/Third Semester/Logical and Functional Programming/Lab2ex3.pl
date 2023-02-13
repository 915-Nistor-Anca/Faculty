remove_element([], _, []).
remove_element([H|T], E, R) :- H =:= E,
    remove_element(T, E, R).
remove_element([H|T], E, [H|R]) :- H =\= E,
    remove_element(T, E, R).

frequency([], _, 0).
frequency([H|T], E, R) :- H =:= E,
    frequency(T, E, R1),
    R is R1 + 1.
frequency([H|T], E, R) :- H =\= E,
    frequency(T, E, R).

remove_repetitive([], []).
remove_repetitive([H|T], [H|R]) :-
    frequency([H|T], H, RC),
    RC =:= 1,
    remove_repetitive(T, R).
remove_repetitive([H|T], R) :-
    frequency([H|T], H, RC),
    RC =\= 1,
    remove_element([H|T], H, RO),
    remove_repetitive(RO, R).


maxim_number(A, B, A) :- A >= B.
maxim_number(A, B, B) :- A < B.

maxim_list([H], H).
maxim_list([H|T], R) :- 
    maxim_list(T, RM),
    maxim_number(H, RM, R).

remove_maxim(L, R) :-
    maxim_list(L, RM),
    remove_element(L, RM, R).