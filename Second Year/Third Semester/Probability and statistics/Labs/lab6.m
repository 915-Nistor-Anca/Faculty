% H0 = null hypothesis
% H1 = alternative hypothesis
% H0 : theta = theta_zero
% H1: theha < theta_zero or theta > theta_zero or theta != theta_zero
%    (left-tailed test)   (right-tailed test)     (two- tailed test)
% alpha in (0,1) ~~~> significance level
% TS ~~~> statistics test
% TS0 = TS( theta = theta_zero) ~~~> observed value
% RR ~~~> rejection region
% P -value ~~~> (if alpha < P, reject H0)

% How do we reject or not H0?
% -> hypothesis testing: if TS0 in RR, reject H0;
%                        otherwise, don't reject H0.
%
% -> significance testing: if alpha >= P, reject H0. Otherwise, don't reject H0.

% H0: mu = 9
% H1: mu < 9 <-- left-tailed test

x = [7, 7, 4, 5, 9, 9, 4, 12, 8, 1, 8, 7, 3, 13, 2, 1, 17, 7, 12, 5, 6, 2, 1, 13, 14, 10, 2, 4, 9, 11, 3, 5, 12, 6, 10, 7];
n = length(x);

mu = input('Enter mu:');
sigma = 5;
alpha = input('Enter alpha:');
[H, P, CI, ZVAL] = ztest(x, mu, sigma, alpha, 'left');
RR = [-inf, norminv(alpha)]; 
fprintf('The confidence interval for mu is (%4.4f, %4.4f)\n', CI)
fprintf('The rejection region is (%4.4f, %4.4f)\n', RR)
fprintf('The value of the test statistic z is %4.4f\n', P)
if H == 1
    fprintf('\nThe null hypothesis is rejected.\n')
    fprintf('The data suggests that the standard IS NOT met.\n')
   
else
    fprintf('\nThe null hypothesis is not rejected.\n')
    fprintf('The data suggests that the standard IS met.\n')
end




mu = input('Enter mu:');
[H, P, CI, ZVAL] = ttest(x, mu, alpha, 'right');
RR = [tinv(1-alpha,n-1), Inf];
fprintf('\nThe confidence interval for mu is (%4.4f,%4.4f)\n',CI)
fprintf('The rejection region is (%4.4f,%4.4f)\n', RR)
fprintf('The value of the test statistic t is %4.4f\n', ZVAL.tstat)
fprintf('The P-Value of the test is %4.4f\n', P)
if H == 1
    fprintf('The null hypothesis is rejected.\n')
    fprintf('The data suggests that the average exceeds 5.5.\n')
    
else
    fprintf('The null hypothesis is not rejected.\n')
    fprintf('The data suggests that the average does not exceeds 5.5.\n')
end