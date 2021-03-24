typedef struct {
	float real,imag;
} num_complexo;

void soma_complexo(num_complexo x, num_complexo y){
	num_complexo s;
	s.real = x.real + y.real;
	s.imag = x.imag + y.imag;
	printf("A soma eh: %f + (%f)i\n", s.real, s.imag);
}

void subtra_complexo(num_complexo x, num_complexo y){
	num_complexo s;
	s.real = x.real - y.real;
	s.imag = x.imag - y.imag;
	printf("A subtracao eh: %f + (%f)i\n", s.real, s.imag);
}

void multiplica_complexo(num_complexo x, num_complexo y){
	num_complexo m;
	m.real = x.real*y.real - x.imag*y.imag;
	m.imag = x.real*y.imag + x.imag*y.real;
	printf("O produto eh: %f + (%f)i\n", m.real, m.imag);
}

void divisao_complexo(num_complexo x, num_complexo y){
	num_complexo d;
	d.real = (x.real*y.real + x.imag*y.imag)/(y.imag*y.imag+y.real*y.real);
	d.imag = (x.imag*y.real - x.real*y.imag)/(y.imag*y.imag+y.real*y.real);
	printf("A divisao eh: %f + (%f)i\n", d.real, d.imag);
}

void polar_complexo(num_complexo x, num_complexo y){
	float ro, theta;
	ro = sqrt(x.real*x.real+x.imag*x.imag);
	theta = atan(x.real/x.imag)*180/3.141592; 
	printf("A forma polar do primeiro numero eh: %f*(cos(%f)+i*sen(%f))\n", ro, theta, theta);
	ro = sqrt(y.real*y.real+y.imag*y.imag);
	theta = atan(y.real/y.imag)*180/3.141592; 
	printf("A forma polar do segundo numero eh: %f*(cos(%f)+i*sen(%f))\n", ro, theta, theta);
}
