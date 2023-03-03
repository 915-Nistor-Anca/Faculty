% mean - computes the mean of a sum 
% var - computes the variances
% var (x, 1) - sum of (xi - x)^2, i = 1, n
% var (x) - sum of (xi - x)^2, i = 1, n-1
% std (x)

% Confidence intervals
% a characteristic of a population X.
% with pdf f(x, theta), theta = target parameter
% a sample of size n X1, X2, .... Xn - independent and identically
% distributed variables
% theta bar = theta bar(X1 X2 ... Xn) - point estimate.
% Find theta bar low and theta bar upper such that:
% P(theta bar is included in (theta bar low, theta bar upper)) = 1 - alpha
% - interval estimate.
% 100(1 - alpha)% confidence interval
% 1 - alpha = confidence level
% alpha - significance level

%Pivot method: random variable W which depends on X1, ..., Xn and of theta
%such that P(W alpha/2 < W < W 1- alpha/2) = 1 - alpha
%P(theta bar low < theta < theha bar upper) = 1 - alpha

x = [7, 7, 4, 5, 9, 9, 4, 12, 8, 1, 8, 7, 3, 13, 2, 1, 17, 7, 12, 5, 6, 2, 1, 13, 14, 10, 2, 4, 9, 11, 3, 5, 12, 6, 10, 7];
n = length(x);
confidence_level = input('Enter 1 - alpha:');
alpha = 1 - confidence_level;
sigma = 5;
z1 = norminv(1 - alpha/2, 0, 1);
z2 = norminv(alpha/2, 0, 1);
average = mean(x);

 %a)
mu1 = average - (sigma/sqrt(n))*z1;
mu2 = average - (sigma/sqrt(n))*z2;
fprintf("a) The confidence interval for the mean(sigma known) is : (%.3f, %.3f).\n",mu1, mu2)

%b)
s = std(x);
t1 = tinv(1 - alpha/2, n-1);
t2 = tinv(alpha/2, n-1);
mu3 = average - (s/sqrt(n))*t1;
mu4 = average - (s/sqrt(n))*t2;
fprintf("b) The confidence interval for the mean(sigma unknown) is : (%.3f, %.3f).\n",mu3, mu4)


%c)
t3 = chi2inv(1 - alpha/2, n-1);
t4 = chi2inv(alpha/2, n-1);
s_sq = var(x);
mu5 = ((n-1)*s_sq)/t3;
mu6 = ((n-1)*s_sq)/t4;
fprintf("c) The confidence interval for variance is : (%.3f, %.3f).\n",mu5, mu6)

X1 = [22.4 21.7 24.5 23.4 21.6 23.3 22.4 21.6 24.8 20.0];
X2 = [17.7 14.8 19.6 19.6 12.1 14.8 15.4 12.6 14.0 12.2];
avgOfX1 = mean(X1);
avgOfX2 = mean(X2);
lengthOfX1 = length(X1);
lengthOfX2 = length(X2);
t1 = tinv(1-alpha/2, lengthOfX1 + lengthOfX2 - 2);
s1 = var(X1);
s2 = var(X2);
s = (((lengthOfX1 - 1)*s1) + ((lengthOfX2 - 1)*s2))/(lengthOfX1 + lengthOfX2 - 2);
mu1 = avgOfX1 - avgOfX2 - t1*sqrt(s)*sqrt((1/lengthOfX1) + (1/lengthOfX2));
mu2 = avgOfX1 - avgOfX2 + t1*sqrt(s)*sqrt((1/lengthOfX1) + (1/lengthOfX2));
fprintf("(%.3f, %.3f).\n",mu1, mu2)


t2 = tinv(1-alpha/2, n);
c = (s1/lengthOfX1) / ((s1/lengthOfX1 + s2/lengthOfX2));
n = 1/((c*c)/(lengthOfX1 - 1) + ((1-c)*(1-c))/(lengthOfX2-1));

mu1 = avgOfX1 - avgOfX2 - t2*sqrt((s1/lengthOfX1) + (s2/lengthOfX2));
mu2 = avgOfX1 - avgOfX2 + t2*sqrt((s1/lengthOfX1) + (s2/lengthOfX2));
fprintf("(%.3f, %.3f).\n",mu1, mu2)
