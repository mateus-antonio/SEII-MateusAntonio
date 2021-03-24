#include <stdio.h>
#include <math.h>
#include "biblioteca.h"

int main() {
	num_complexo A,B;
	printf("Digite a parte real e imaginaria do primeiro numero: ");
	scanf("%f %f", &A.real, &A.imag);
	
	printf("Digite a parte real e imaginaria do segundo numero: ");
	scanf("%f %f", &B.real, &B.imag);
	
	soma_complexo(A,B);
	subtra_complexo(A,B);
	multiplica_complexo(A,B);
	divisao_complexo(A,B);
	polar_complexo(A,B);
	
	return(0);
}