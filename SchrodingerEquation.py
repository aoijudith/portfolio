
clear all;                  % clear all variables in memory
close all;

L=3.;
T=200.;

Nx = 200;
dx = L/(Nx-1);
Nt=5000;
dt=T/(Nt-1);
k=2.0*pi;
mass=9.11*10^(-31);
hb=1.0546*10^(-34);
a=1.0*dt/(dx)^2;


%Initial conditions: u(x,0)=exp(-1i*k*x) [wave function at t=0]
x = 0 : dx : L;
f = exp(-1i*k*x);
u = zeros(Nx,Nt);  
u(:,1)=f(:);
u(:,Nt)=f(:);

%Using explicit scheme to solve for Schrodinger's time dependent equation
for m = 1:Nt
    t = m*dt;         
    for n = 2:Nx-1
        u(n,m+1)=1i*a*(hb*(u(n+1,m)-2*u(n,m)+u(n-1,m))/mass)/2+u(n,m);
    end
end

%Plotting the animation of Schrodinger's Equation
for m=1: round(Nt/100): Nt
    figure(1)
	plot(x,real(u(:,m)),'b-');
    ylim([-0.5,1.5])
    xlabel('x')
    ylabel('u')
    t=m*dt;
    title(sprintf('t=%5.2f',t))
        hold off
    drawnow
end
