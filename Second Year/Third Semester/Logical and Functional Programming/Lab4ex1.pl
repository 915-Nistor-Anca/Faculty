% insert(l1...ln, e) =
% 	[e], n = 0
% 	e + l1...ln, n >= 1
% 	l1 + insert(l2...ln, e), otherwise

% insert(L:list, E:number, R:list)
% insert(i, i, o)

insert([], E, [E]).
insert([H|T], E, [E,H|T]).
insert([H|T], E, [H|R]) :- 
         insert(T, E, R).

% permutation(l1...ln) =
% 	[], n = 0
% 	insert(permutation(l2...ln), l1), otherwise

% permutation(L:list, R:list)
% permutation(i, o)

permutation([], []).
permutation([H|T], R) :-
    permutation(T, RP),
    insert(RP, H, R).

% combinations(l1...ln, k) =
% 	[], k = 0
% 	l1 + combinations(l2...ln, k - 1), k > 0
% 	combinations(l2...ln, k), k > 0

% combinations(L:list, K:number, R:list)
% combinations(i, o)

combinations(_, 0, []).
combinations([H|T], K, [H|R]) :-
    K > 0,
    NK is K - 1,
    combinations(T, NK, R).
combinations([_|T], K, R) :-
    K > 0,
    combinations(T, K, R).

% allsolutions(L:list, N:number, R:list)
% allsolutions(i, i, o)

allsolutions(L, N, R) :-
    findall(RPartial, combinations(L, N, RPartial), R).