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
    a db 5
    b dw 5
    c dd 10
    d dq 15
    aux resq 1
    
; our code starts here
; (c+d-a) - (d-c) - b -> signed representation
; a - byte, b - word, c - doubleword, d - quadword
segment code use32 class=code
    start:
        ; ...
        mov eax, dword [c]
        cdq ; edx:eax = c
        
        mov ebx, dword [d]
        mov ecx, dword [d+4] ; ecx:ebx = d 
        
        add ebx, eax
        adc ecx, edx ; ecx:ebx = c + d
        
        mov ah, 0
        mov al, [a]
        cbw ; ax = a
        cwde ; eax = a
        cdq ; edx:eax = a
        
        sub ebx, eax
        sbb ecx, edx ; ecx:ebx = c + d - a
        
        mov dword [aux], ebx 
        mov dword [aux + 4], ecx ; aux = c + d - a
        
        mov ebx, dword [d]
        mov ecx, dword [d + 4] ;ecx:ebx = d
        
        mov eax, [c]
        cdq ; edx:eax = c
        
        sub ebx, eax
        sbb ecx, edx ; ecx:ebx = d - c
        
        mov eax, dword [aux]
        mov edx, dword [aux + 4] ; edx:eax = c + d - a
        
        sub eax, ebx 
        sbb edx, ecx ; edx:eax = (c+d-a) - (d-c)
        
        mov ebx, eax
        mov ecx, edx ; ecx:ebx = (c+d-a) - (d-c)
        
        mov ax, [b]
        cwde ; eax = b
        cdq ; edx:eax = b
        
        sub ebx, eax
        sbb ecx, edx ; ecx:ebx = (c+d-a) - (d-c) - b
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
