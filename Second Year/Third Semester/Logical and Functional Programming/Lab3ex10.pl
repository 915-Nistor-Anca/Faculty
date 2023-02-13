prime(N, _):- N == 1, !, false.
prime(N, _):- N > 1, N =< 3.
prime(N, D):- N mod D =\= 0,
    D >= N / 2, !.
prime(N, D):- N mod D =\= 0,
    D2 is D + 1,
    prime(N, D2).


primeTwice([], []).
primeTwice([H|T], [H,H|R]):- prime(H,2), !,
    primeTwice(T, R).
primeTwice([H|T], [H|R]):- 
    primeTwice(T, R).

modify([], []).
modify([E], [E]).
modify([H|T], [HR|R]) :- is_list(H), !,
    primeTwice(H, HR),
    modify(T, R).
modify([H|T], [H|R]) :-
    modify(T, R).