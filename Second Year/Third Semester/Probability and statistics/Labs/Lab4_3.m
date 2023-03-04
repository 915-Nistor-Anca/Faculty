p = input('Probability of success = ');
N = input('Number of simulations = ');
n= input('Number of successes =');

for i=1:N
    U = rand;
    success = U<p;
    X(i) = 0;
    while(success == 0)
        X(i) = X(i) + 1;
        U = rand;
        success = U<p;
    end
end

U_X = unique(X);
n_X = hist(X, length(U_X));
relative_freq = n_X/N;
[U_X; relative_freq]

plot(U_X, relative_freq, 'x', 0:30, nbinpdf(0:30, n, p), 'o');
legend('simulation', 'nbinpdf');