bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    a db 10
    d dw 5
; our code starts here
; 4. 300 - [5*(d-2*a) - 1]
; a, b - byte
; d - word
segment code use32 class=code
    start:
        ; ...
        mov al, 2
        mov ah, [a]
        mul ah ; ax = 2*a
        
        mov bx, [d]
        sub bx, ax ; bx = d - 2*a
        
        mov ax, 5
        mul bx ; dx:ax = 5*(d-2*a)
        
        push dx
        push ax
        pop ebx ; ebx = 5*(d-2*a)
        
        dec ebx ; ebx = 5*(d-2*a) - 1
        mov ecx, 300
        sub ecx, ebx ; ecx = 300 - [5*(d-2*a) - 1]
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
