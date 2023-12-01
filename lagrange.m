m1=1;
m2=2;
% solution vector with start values
S=[0; % x
   0; % y
   1; % phi
   10; % Vx
   0; % Vy
   5]; % omega
R=3;
R1=R*m2/(m1+m2); % distance to masses center from m1
% forces:
F1x=0;
F1y=0; % force at m1
F2x=0;
F2y=0; % force at m2
dt=0.01;
tm=5;
t=0:dt:tm;
x=S(1);
y=S(2);
hp=plot([x x+R*cos(S(3))],[y y+R*sin(S(3))],'bo-');
hold on;
lm=30;
xlim([-lm lm]);
ylim([-lm lm]);
axis equal;
lc=1;
for tt=t(2:end)
    x=S(1);
    y=S(2);
    phi=S(3);
    Vx=S(4);
    Vy=S(5);
    om=S(6);
    % M*a=b; => a=inv(M)*b => a=M\b;
    M=[m1+m2                  0                 -m2*R*sin(phi);
       0                      m1+m2             m2*R*cos(phi);
       -m2*R*sin(phi)         m2*R*cos(phi)     m2*R^2];
    b=[F1x+F2x+m2*om^2*R*cos(phi);
       F1y+F2y+m2*om^2*R*sin(phi); 
       -F2x*R*sin(phi)+F2y*R*cos(phi)];
    
    a=M\b;
    % a=[ dVx/dt
    %     dVy/dt
    %     dom/dt
    ae=[S(4:6); a];
    S=S+dt*ae;
    set(hp,'XData',[x x+R*cos(S(3))],'YData',[y y+R*sin(S(3))]);
    plot(x+R1*cos(S(3)),y+R1*sin(S(3)),'r.');
    xlim([-lm lm]);
    ylim([-lm lm]);
    if mod(lc,5)==0
        drawnow;
        pause(0.002);
    end
    lc=lc+1;
end
    
    

