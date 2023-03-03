%Recall:
% pdf(k, n, p) = P(x = k)
% cdf(k, n, p) = P( x <= k)
% ex: bino = 3=> cdf(1, 3, p) = pdf(0, 3, p) + pdf (1, 3, c)
% P(x > k) = 1 - P(x <= k)
% P( a < x <= b) = cdf(b) - cdf(a)
% input('.......', 's')
% switch ____
% case 'normal'
% otherwise printf(....)
% normal - normcdf; student - tcdf; chi2 - chi2cdf; fischer - fcdf


distribution = input('normal / student / chi2 / fischer:', 's');
switch distribution
    case 'normal'
        mu = input('Enter mu:');
        sigma = input('Enter sigma:');

        %a)
        firstP = normcdf(0, mu, sigma);
        secondP = 1 - firstP;
        fprintf('P(x<=0) = %f, P(x>=0) = %f\n\n', firstP, secondP)

        %b)
        value = normcdf(1, mu, sigma) - normcdf(-1, mu, sigma);
        value2 = 1 - value;
        fprintf('P(-1<=x<=1) = %f, P(x<= -1 or x >= 1) = %f\n\n', value, value2)

        %c)
        a = input('Enter alpha:');
        if (a > 1 || a < 0) 
            fprintf('Alpha was not betweeen 0 and 1!');
        end
        v = norminv(a, mu, sigma);
        fprintf('P(x < xa) = %f\n\n',  v)

        %d)
        b = input('Enter beta:');
        if (b > 1 || b < 0) 
            fprintf('Beta was not betweeen 0 and 1!');
        end
        v2 = norminv(1 - b, mu, sigma);
        fprintf('P(x < xa) = %f\n\n',  v2)

    case 'student'
        n = input('Enter n:');

        %a)
        firstP = tcdf(0, n);
        secondP = 1 - firstP;
        fprintf('P(x<=0) = %f, P(x>=0) = %f\n\n', firstP, secondP)

        %b)
        value = tcdf(1, n) - tcdf(-1, n);
        value2 = 1 - value;
        fprintf('P(-1<=x<=1) = %f, P(x<= -1 or x >= 1) = %f\n\n', value, value2)

        %c)
        a = input('Enter alpha:');
        v = tinv(a, n);
        fprintf('P(x < xa) = %f\n\n',  v)

        %d)
        b = input('Enter beta:');
        v2 = 1 - tinv(b, n);
        fprintf('P(x < xa) = %f\n\n',  v2)


    case 'fischer'
        m = input('Enter m:');
        n = input('Enter n:');

        %a)
        firstP = fcdf(0, m, n);
        secondP = 1 - firstP;
        fprintf('P(x<=0) = %f, P(x>=0) = %f\n\n', firstP, secondP)

        %b)
        value = fcdf(1, m, n) - fcdf(-1, m, n);
        value2 = 1 - value;
        fprintf('P(-1<=x<=1) = %f, P(x<= -1 or x >= 1) = %f\n\n', value, value2)

        %c)
        a = input('Enter alpha:');
        v = finv(a, m, n);
        fprintf('P(x < xa) = %f\n\n',  v)

        %d)
        b = input('Enter beta:');
        v2 = 1 - finv(b, m, n);
        fprintf('P(x < xa) = %f\n\n',  v2)

end
