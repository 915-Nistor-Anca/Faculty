bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf, printf, fprintf, fclose, fopen              ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll
import fprintf msvcrt.dll
import fclose msvcrt.dll
import fopen msvcrt.dll   ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

                          
extern prime_number
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    format db " %d", 0
    format2 db "%d", 0
    m dd 0 
    len equ 100
    
    msj db "How many numbers: ",0
    msj2 db "Enter the number:", 0
    msj3 db "The prime numbers are: %s", 0
    
    text dd 0, 0
    text2 dd 0, 0
    n dd 0
    

; our code starts here
segment code use32 class=code
    start:
        push dword msj
        call [printf]
        add esp, 4*1  
    
        push dword m
        push dword format 
        call [scanf]
        add esp, 4*2
      
        
        mov ecx,[m]
        mov esi, 0
        
        jecxz sf
        .read:
            push ecx
            
            push dword msj2
            call [printf]
            add esp, 4*1  
        
            push dword text
            push dword format2
            call [scanf]
            add esp, 4*2
            
            mov eax, [text]
            push eax
            call prime_number
            cmp eax, 1
            je .save_number
            jl .fin
            
            .save_number:
                mov ebx, [text]
                mov dword [text2 + n], ebx
                add byte [n], 4
            .fin:
            pop ecx
        loop .read
        
        
    
        sf:
            push dword text2
            push dword msj3 
            call [printf]
            add esp, 4*2
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
