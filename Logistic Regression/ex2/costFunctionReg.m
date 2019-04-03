function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta


H = sigmoid(X * theta) ;

n = length(theta) ;


Reg_exp = (theta(2:n))' * theta(2:n) 
Reg_exp = (lambda.*Reg_exp) ./(2.*m)

J1 = (-y)' * log(H) ;
J2 = (1 .- y)' * log(1 .- H) ;
J =  (J1 - J2) ./ m ;
J = J + Reg_exp ;
% Gradient

A = (H - y)' * X ;
Reg_grad = (lambda .* theta)./m
grad = A' ./ m  + Reg_grad;
grad(1,1) -= Reg_grad(1,1) ;


% =============================================================

end
