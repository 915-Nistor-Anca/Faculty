n = input('Enter n:');
p = input('Enter p:');

if (n < 30 || p > 0.05)
    fprintf('Error')
end

l = n*p;
plot(0:n, binopdf(0:n, n, p), 0:n, poisspdf(0:n,l));