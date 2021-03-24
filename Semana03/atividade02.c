#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[ ]){
   char origem_file[40], destino_file[40];
   FILE *origem, *destino;
   int n, m;
   unsigned char *buff;
   buff = malloc(1024);

   strcpy(origem_file, argv[1]);
   strcpy(destino_file, argv[2]);

   origem = fopen(origem_file, "rb");
   if (origem == NULL){
      printf("Erro ao abrir o arquivo!\n");
      exit(EXIT_FAILURE);
   }

   destino = fopen(destino_file, "wb");
   if (destino == NULL){
      fclose(origem);
      printf("Erro ao duplicar o arquivo!\n");
      exit(EXIT_FAILURE);
   }

   do{
      n = fread(buff, 1, sizeof buff, origem);
      if(n){
         m = fwrite(buff, 1, n, destino);
      }
      else{
         m = 0;
      }   
   }while((n > 0) && (n == m));

   printf("Arquivo duplicado!\n");

   fclose(origem);
   fclose(destino);
   free(buff);

   return 0;
}