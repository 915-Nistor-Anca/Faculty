bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf, scanf            ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll                ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import printf msvcrt.dll
import scanf msvcrt.dll     
                          
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; Read a number in base 10 from the keyboard and display the value of that number in base 16.
    n dd 0
    message db "n=", 0
    format db "%d", 0
    format2 db "numar baza 16: %x", 0
    

; our code starts here
segment code use32 class=code
    start:
        ; ...
        push dword message
        call [printf]
        add esp, 4 * 1
        
        
        
        push dword n
        push dword format
        call [scanf]
        mov eax, [n]
        add esp, 4 * 2
        
        push dword eax
        push dword format2
        call [printf]
        add esp, 4 * 2
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program