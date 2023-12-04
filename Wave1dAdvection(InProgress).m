%---------------------------------------------------------------
% 
%  Forward time central space difference (FTCS) scheme to solve the advection equation
%     u_t(x,t) + c u_x(x,t) = 0,        xl < x < xr, 0 < t < tf
%     u(x, 0) = f(x),                 xl < x < xr
%    periodic boundary
% 
% The analytic solution is:
%        u(x,t)= f(x-t)=e^(-50(x-t-0.5)^2)
%---------------------------------------------------------------
clear all;                  
close all;

xl=0; xr=1;           
N = 100;                    

tf = 2.4; 
dx = (xr-xl) / N; 
Mt = 2000;               
dt = tf/Mt;                
c1 = 50;               
c=1;
mu = c*dt/dx; 

% Evaluate the initial conditions
x = xl : dx : xr; 
figure(1)
f = exp(-c1*(x - 0.5).^2);        
plot(x,f,'b-');
ylim([-0.5,1.5])
xlabel('x')
ylabel('u')

u = zeros(N+1,Mt);  
u(:,1)= f;
udata=u(:,1);
tdata=0;

for m = 2:Mt                  
       for n=2:N
	        u(n,m) = u(n,m-1) - mu*(u(n,m-1)-u(n-1,m-1));
       end
    u(1,m) = u(N,m);  
    u(N+1,m) = u(2,m); 
    figure(1)
	plot(x,u(:,m),'b-');
    ylim([-0.5,1.5])
    xlabel('x')
    ylabel('u')
    t=m*dt;
    title(sprintf('t=%5.2f',t))
    hold off

end
tmax=Mt*dt;
figure(2)
waterfall(x,tdata,udata')
colormap(jet(128)); 
view(10, 60)
axis([xl xr 0 tmax -3 3]); 
xlabel('x')
ylabel('t')
zlabel('u')
grid off 
