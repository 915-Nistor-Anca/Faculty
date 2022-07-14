bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    A dw 0000010101010111b
    B db 10100110b
    C dd 0
; Given the word A and the byte B, compute the doubleword C:
;the bits 0-3 of C have the value 1
;the bits 4-7 of C are the same as the bits 0-3 of A
;the bits 8-13 of C have the value 0
;the bits 14-23 of C are the same as the bits 4-13 of A
;the bits 24-29 of C are the same as the bits 2-7 of B
;the bits 30-31 have the value 1


; 1110 1001 0001 0101 0100 0000 0111 1111
;  E    9    1    5    4    0    7    F

; our code starts here
segment code use32 class=code
    start:

     mov ebx, [C] ;the result will be in ebx
     or ebx, 00000000000000000000000000001111b                               ;the bits 0-3 of C have the value 1
     
     
     
     
     
     mov ax, [A]
     and ax, 0000000000001111b ;the bits 0-3 of A are now isolated in ax
     
     mov cl, 4
     rol ax, cl ;rotate 4 positions to the left
     cwd
     and eax, 00000000000000001111111111111111b ;in case the sign bit is 1 (works the same for: mov edx,0)
     or ebx, eax                                                             ;the bits 4-7 of C are the same as the bits 0-3 of A
     
     
     
     
     
     
     and ebx, 11111111111111111100000011111111b                              ;the bits 8-13 of C have the value 0
     
     
     
     mov ax, [A]
     and ax, 0011111111110000b ;the bits 4-13 of A are now isolated in ax
     
     cwd
     and eax, 00000000000000001111111111111111b
     mov cl, 10
     rol eax, cl
     or ebx, eax                                                             ;the bits 14-23 of C are the same as the bits 4-13 of A
    
    
    
    mov al, [B]
    and al, 11111100b ;the bits 2-7 of B are now isolated in al
    cbw
    and ax, 0000000011111111b
    cwd
    and eax, 00000000000000001111111111111111b
    mov cl,22
    rol eax, cl
    or ebx, eax                                                             ;the bits 24-29 of C are the same as the bits 2-7 of B
    
    
    
    
    or ebx, 11000000000000000000000000000000b                               ;the bits 30-31 have the value 1
    
    
    mov [C], ebx
    
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program