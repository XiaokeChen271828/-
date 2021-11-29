N=500;
M=500;
lamda=1050;
k=2*pi/lamda;

x=linspace(-1,1,N);
y=linspace(-1,1,M);

[X,Y]=meshgrid(x,y);
[theta,r]=cart2pol(X,Y);
figure;

E=get_fai(r);
I=fix(E)+1-E;
I1=I/max(max(I))
h1=pcolor(theta,r,I1);

mat=I1
imshow(I1);

function f=get_fai(r1)
f=(100000/1050)*sqrt(1.45^2-0.7^2.*(r1).^2);
end
