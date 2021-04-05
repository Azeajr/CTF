#include "keys.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#define buffersize 1024

int main(int argc, char *argv[]){
    char buffer[buffersize];
	FILE *input;
	int commands[buffersize];
	if(argc==2){
		input=fopen(argv[1],"r");
	}

	if(input==NULL){
		printf("Unable to open file '%s'\n",argv[1]);
		exit(1);
	}

	int n=0;
	while(fgets(buffer,buffersize,input)){
		strtok(buffer,",");
		commands[n]=atoi(strtok(NULL,","));
		n++;
	}

	/*
	Start at n=6.
	*/
	const char *keys[11]={
		" 0",
		".,'?!\"1-()@/:",
		"abc2",
		"def3",
		"ghi4",
		"jkl5",
		"mno6",
		"pqrs7",
		"tuv8",
		"wxyz9",
		"@/:_;+&%*[]{}"
	};

	int i;
	int current;
	int next;
	int count=0;
	for(i=6;i<n;i++){
		current=i;
		next=i+1;


        printf("Count: %d\tStrLen: %ld\tComp: %d\n",count,strlen(keys[commands[current]]),count<strlen(keys[commands[current]]));
        
		if(commands[i]<11){
			if(commands[current]==commands[next] && count<strlen(keys[commands[current]])-1){
				count++;
			}else{
				//printf("%c",keys[commands[i]][count]);
				count=0;
			}

			//printf("Com: %d\tkey: %c\n",commands[i],keys[commands[i]][0]);
		}
	}
	printf("\n");






	if(fclose(input)!=0){
		perror("fclose");
		exit(EXIT_FAILURE);
	}

	return 0;
}
