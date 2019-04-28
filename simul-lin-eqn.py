print( "A 3 X 3 matrix is denoted in this program as follows:- ");
print(" a1  a2  a3 ");
print(" b1  b2  b3 ");
print(" c1  c2  c3 "); 
a1 = int(input("Enter Value for a1:- "));
b1 = int(input("Enter Value for b1:- "));
c1 = int(input("Enter Value for c1:- "));
a2 = int(input("Enter Value for a2:- "));
b2 = int(input("Enter Value for b2:- "));
c2 = int(input("Enter Value for c2:- "));
a3 = int(input("Enter Value for a3:- "));
b3 = int(input("Enter Value for b3:- "));
c3 = int(input("Enter Value for c3:- "));
d1 = int(input("Enter Value for d1:- "));
d2 = int(input("Enter Value for d2:- "));
d3 = int(input("Enter Value for d3:- "));
t1 = float(a2/a1);
t2 = float(a3/a1);
gb1 = float(b1*t1-b2);
gb2 = float(b1*t2-b3);
t3 = float(gb2/gb1);
gc1 = float(c1*t1 - c2);
gc2 = float(c1*t2-c3);
gd1 = float(d1*t1 -d2);
gd2 = float(d1*t2-d3);
dct3 = float(gc1*t3-gc2);
if dct3 == 0:
	print("Zero division error");
else:
	ddt3 = float(gd1*t3-gd2);
	z = float(ddt3/dct3);
	y = float((gd1-gc1*z)/gb1);
	x = float((d1-c1*z-b1*y)/a1);
	print("The value of x is :- ",x);
	print("The value of y is :- ",y);
	print("The value of z is :- ",z);
	print("Written by Karthik Prabhu");
	
