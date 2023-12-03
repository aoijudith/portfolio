clear all
close all
t0=0.0;       
tmax=2.0;
N=40;
y0=1.0;          % initial value
dt=(tmax-t0)/N   % size of dt
t(1)=t0;
y(1)=y0;   % Initial value of approximation
ye(1)=y0;  % Initial value of exact function
error(1)=0.0;  % Error of approximation

for n=1:N
t(n+1)=t(n)+dt;
y(n+1)=y(n)+dt*y(n);            % Euler's method approximation
ye(n+1)=y0*exp(t(n+1));         % Exact function
error(n+1)=abs(y(n+1)-ye(n+1)); % Error of approximation
end

figure(1)
plot(t,y)
hold on
plot(t,ye)
xlabel('t')
ylabel('y')
title('dy/dt=y')
ylim([-10,10])
xlim([0,tmax])
legend('numerical solution','exact solution')

figure(2)
plot(t,error)
xlabel('t')
ylabel('error')
title('Absolute error of a numerical solution of dy/dt=y')
ylim([0,1])
xlim([0,tmax])
