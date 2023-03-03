
P = input('Enter the probability:');
if (P < 0.05 || P > 0.95) 
    fprintf('P should be between 0.05 and 0.95!')
end

for n = 0:2:100
    a = n*P;
    b = sqrt(n*P*(1 - P));
    plot(0:n, binopdf(0:n, n, P), 0:n, normpdf(0:n, a, b));

    pause(0.5)
end

