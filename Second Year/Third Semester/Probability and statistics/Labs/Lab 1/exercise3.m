x = 0:0.1:3;

f1 = x.^5/10;
f2 = x.*sin(x);
f3 = cos(x);

subplot(3,1,1)
plot(x, f1, '-y')
title('First plot')
legend('A nice yellow line.')

subplot(3,1,2)
plot(x, f2, '-.m')
title('Second plot')
legend('Dots are fun.')

subplot(3,1,3)
plot(x, f3, ':r')
title('Third subplot')
legend('Going down.')
