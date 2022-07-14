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
    a db 2
    c db 6
    b dd 6
    x dq 100
    
    
; our code starts here
; x - (a*a + b) / (a + c/a) -> unsigned representation
; a, c - byte; b- doubleword; x- quadword

segment code use32 class=code
    start:
        ; ...
        mov al, [a]
        mul byte [a] ; ax = a*a 
        mov dx, 0 ; dx:ax = a*a
        
        push dx
        push ax 
        pop eax ;eax = a*a
        
        add eax, [b] ; eax = a*a + b
        mov ebx, eax ; ebx = a*a + b 
        
        mov al, [c]
        mov ah, 0 ; ax = c 
        div byte [a] ; al = c/a 
        
        add al, [a] ; al = a + c/a
        mov ah, 0 ; ax = a + c/a 
        
        mov cx, ax ; cx = a + c/a 
        mov eax, ebx ; eax = a*a + b 
        div cx ; ax = (a*a + b) / (a + c/a)
        neg ax ; ax = -(a*a + b) / (a + c/a)
        
        mov dx, 0
        mov edx, 0 ; edx:eax = -(a*a + b) / (a + c/a)
        
        add eax, dword [x]
        add edx, dword [x + 4] ; edx:eax = x - (a*a + b) / (a + c/a)
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
