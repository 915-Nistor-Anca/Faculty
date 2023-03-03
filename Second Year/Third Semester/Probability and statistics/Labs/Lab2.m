%pdf('bino',k,n,p)
%binopdf(k,n,p), k = 0,n
%binopdf - exactly, binocdf - at most

%a
subplot(2,1,1)
k = 0:3;
p = 1/2; 
y = binopdf(k, 3, p);
plot(k,y)
title('a)')

%b
x = 0:0.1:3;
%plot(x, binocdf(x,3,1/2))

%plot(x,sin(x), x, cos(x))
%plot(x,sin(x))
% hold on
%plot(x,cos(x))
%hold off

subplot(2,1,2)
plot(k,binopdf(k,3,1/2))
hold on
plot(x,binocdf(x,3,1/2))
hold off
title('b)')

%c
c = binopdf(0,3,1/2);
c2 = 1 - binopdf(1,3,1/2);
fprintf('P(x=0) = %f, P(!=x) = %f\n\n', c, c2)

%d
x = 0:2;
d = binocdf(2,3,1/2);
d2 = binocdf(1.5,3,1/2);
fprintf('P(x<=2) = %f\n', d)
fprintf('\n')
fprintf('P(x<2) = %f\n', d2)

%e
x = 0:1;
e = binocdf(0.5,3,1/2);
e2 = binocdf(1,3,1/2);

fprintf('P(x>=1) = %f\n', 1 - e)
fprintf('\n')
fprintf('P(x>1) = %f\n', 1 -e2)