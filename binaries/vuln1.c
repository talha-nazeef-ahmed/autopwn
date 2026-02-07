#include <stdio.h>

void vulnerable() {
	char buffer[64];
	printf("Enter Your Name: ");
	gets(buffer);
	printf("Hello %s\n", buffer);
}

int main(){
	vulnerable();
	printf("Program finished!\n");
	return 0;
}

