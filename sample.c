#include <stdio.h>
#include <string.h>

void win() {
    printf("Congratulations! You found the vulnerability.\n");
}

void vulnerable_function() {
    char buffer[64];
    
    printf("Enter your input: ");
    // Vulnerable - no bounds checking
    if (fgets(buffer, 128, stdin) == NULL) {
        printf("Error reading input\n");
        return;
    }
    
    printf("You entered: %s\n", buffer);
}

int main() {
    printf("Welcome to the sample vulnerable program\n");
    vulnerable_function();
    return 0;
} 