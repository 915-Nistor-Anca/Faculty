clear all;
clc;
p = input('Probability of success = ');
N = input('Number of simulations = ');
n = input('Number of trials = ');
for j=1:N
    X(j) = 0;
    for i=1:n
      U = rand;
      X(j) = X(j) + (U<p);
    end
    
end  
U_X = unique(X);
n_X = hist(X, length(U_X));
relative_freq = n_X/N;
[U_X; relative_freq]

plot(U_X, relative_freq, 'x', 0:n, binopdf(0:n, n, p), 'o');
legend('simulation', 'binopdf');

for i=1:n
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

plot(U_X, relative_freq, 'x', 0:30, geopdf(0:30, p), 'o');
legend('simulation', 'binopdf');
