close all
clear all
clc

prompt = "What is the prey's growth rate? ";
alpha = input(prompt);

prompt = "What is the prey's death rate? ";
beta = input(prompt);

prompt = "What is the predator's growth rate? ";
delta = input(prompt);

prompt = "What is the predator's death rate? ";
gamma = input(prompt);

prompt = "What is the initial population of prey? ";
prey = input(prompt);

prompt = "What is the initial population of predators? ";
predator = input(prompt);

params = [alpha; beta; delta; gamma];

y0 = [prey; predator];

tspan = [0 50];

[t,y] = ode45(@(t,y)myODE(t,y,params),tspan,y0);

subplot(2,1,1);
plot(t,y(:,1));
xlabel('Time');
ylabel('Prey');

subplot(2,1,2);
plot(t,y(:,2));
xlabel('Time');
ylabel('Predator');


function dy = myODE(t,y,params)

    alpha = params(1);
    beta = params(2);
    delta = params(3);
    gamma = params(4);


    X = y(1);
    Y = y(2);

    dy = zeros(2,1);

    dy(1) = alpha * X - beta * X * Y;
    dy(2) = delta * X * Y - gamma * Y;

end
