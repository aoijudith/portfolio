clc;
clear all;
close all


h=.125
t=0.0:h:1.0
y=zeros(size(t));
exact=zeros(size(t));
error=zeros(size(t));
y(1)=0.0;
exact(1)=0.0;
for n=1:8
    y(n+1)=y(n)+h*cos(y(n))
    exact(n+1)=asin((exp(2*n*h)-1)/(exp(2*n*h)+1))
    error(n+1)=abs(y(n)-exact(n));
end
plot(t,y,t,exact,'--');
title('approx vs exact')
xlabel('time')
ylabel('func')
legend('approximate','exact')
