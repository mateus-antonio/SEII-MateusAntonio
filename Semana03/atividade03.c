#include <stdio.h>
#include <stdlib.h>

void hanoi(int n,char origem,char destino,char auxiliar){
	/*Se sobrar apenas o disco 1, mova fazer o movimento e retornar*/
	if(n==1){ 
		printf("\nMova o disco 1 da base %c para a base %c",origem ,destino);
		return;
	}
	/*Mover o n-1 disco de A para B, usando C de auxiliar*/
	hanoi(n-1,origem,auxiliar,destino);
	/* Mover os discos restantes de A para C*/
	printf("\nMova o disco %d da base %c para a base %c",n,origem,destino);
	/*Mover os n-1 discos de B para C usando A como auxiliar*/
	hanoi(n-1,auxiliar,destino,origem);
}

int main(int argc, char *argv[ ]){
	int n;
	n = atoi(argv[1]);
	
	printf("Para resolver a torre de Hanois faça :\n");
	hanoi(n,'A','C','B');
	printf("\n");

	return 0;
}