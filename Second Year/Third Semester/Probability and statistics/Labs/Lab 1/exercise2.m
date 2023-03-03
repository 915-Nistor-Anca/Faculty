x = 0:0.1:3;

f1 = x.^5/10;
f2 = x.*sin(x);
f3 = cos(x);

plot(x, f1, '-r', x, f2, '.-g', x, f3)
title('The combined plots!')
legend('First.', 'Second.', 'Third.')