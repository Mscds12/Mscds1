clear all;
clc;

disp('Practical performed by Bhavesh Rathod');
disp('Kohonen Self-Organizing Feature Maps');
disp('The input patterns are:');

x = [0 0 1 1;
     1 0 0 0;
     0 1 1 0;
     0 0 0 1];
disp(x);
alpha = 0.5;

disp('Since we have 4 input patterns and 2 cluster units, the weight matrix is:');
w = [0.2 0.9;
     0.4 0.7;
     0.6 0.5;
     0.8 0.3];
disp(w);

disp('The learning rate of this epoch is:');
disp(alpha);
k = 1;
while k <= 4
    for j = 1:2
        temp = 0;
        for i = 1:4
            temp = temp + (x(k,i) - w(i,j))^2;
        end
        D(j) = temp;
    end
    if D(1) < D(2)
        J = 1;
    else
        J = 2;
    end
    disp('Winning unit is');
    disp(J)
    disp('weight updation');
    for m = 1:4
        w(m,J) = w(m,J) + alpha * (x(k,m) - w(m,J));
    end
    disp(w);
    k = k + 1;
    disp(k)
end


