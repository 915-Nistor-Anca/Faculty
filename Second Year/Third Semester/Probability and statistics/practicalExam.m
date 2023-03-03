x = [4.6 0.7 4.2 1.9 4.8 6.1 4.7 5.5 5.4];
y = [2.5 1.3 2.0 1.8 2.7 3.2 3.0 3.5 3. 4];


n1 = length(x);
n2 = length(y);
mx = mean(x);
my = mean(y);
sx = var(x);
sy = var(y);

fprintf('a) \n');

%null hyphotesis: variances are equal;
%alternative hypothesis: variances differ;

alpha = 0.05;

f1 = finv(alpha/2, n1-1, n2-1);
f2 = finv(1-alpha/2, n1-1, n2-1);

[H, P, CI, ZVAL] = vartest2(x, y, 'alpha', alpha);

if H==0
    fprintf('The null hypothesis is not rejected.\n')
    fprintf('The variances seem to be equal.\n')
    fprintf('The rejection region for F is (%6.4f, %6.4f) U (%6.4f, %6.4f)\n', -inf, f1, f2, inf)
    fprintf('The value of the test statistic F is %6.4f\n', ZVAL.fstat)
    fprintf('The P-value for the variances test is %6.4f\n', P)

    n = n1 + n2 - 2;
    t2 = tinv(1 - alpha, n);
    [H2, P2, CI2, ZVAL2] = ttest2(pr, rg, "alpha", alpha, "tail", "right");
    if H2==1
        fprintf('The null hypothesis is rejected.\n') 
    else
        fprintf('The null hypothesis is not rejected.\n')
    end
    fprintf('the rejection region for T is (%6.4f,%6.4f)\n', t2, inf)
    fprintf('the value of the test statistic T is %6.4f\n', ZVAL2.tstat)
    fprintf('the P-value of the test for diff. of means is %e\n', P2)
else
    fprintf('The null hypothesis is rejected.\n')
    fprintf('The variances seem to be different.\n')
    fprintf('The rejection region for F is (%6.4f,%6.4f)U(%6.4f,%6.4f)\n', -inf, f1, f2, inf)
    fprintf('The value of the test statistic F is %6.4f\n', ZVAL.fstat)
    fprintf('The P-value for the variances test is %6.4f\n', P)
end

fprintf('b)\n');
fprintf('SIGNIFICANCE LEVEL %f:\n',alpha)

mu = input('Enter mu:');
[H, P, CI, ZVAL] = ttest(x, mu, alpha, 'right');
RR = [tinv(1-alpha,n-1), Inf];
fprintf('\nThe confidence interval for mu is (%4.4f,%4.4f)\n',CI)