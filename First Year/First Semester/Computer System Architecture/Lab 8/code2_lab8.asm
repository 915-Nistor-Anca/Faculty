bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fopen, fclose, scanf, fprintf
import exit msvcrt.dll  
import fopen msvcrt.dll  
import fclose msvcrt.dll
import fprintf msvcrt.dll
import scanf msvcrt.dll

; our data is declared here (the variables needed by our program)

;A file name is given (defined in the data segment). Create a file with the given name, then read numbers from the keyboard and write only the numbers divisible by 7 to file, until the value '0' is read from the keyboard.

segment data use32 class=data
    file_name db "numbers_divisible_by_7.txt", 0
    access_mode db "w", 0
    descriptor dd -1
    read_number dd 0
    format db "%d", 0
    
; our code starts here
segment code use32 class=code
    start:
        push dword access_mode
        push dword file_name
        call [fopen]
        add esp, 4*2    ;create a file
        
        mov [descriptor], eax
    
        rpt:
            push dword read_number
            push dword format
            call [scanf]
            mov eax, [read_number]
            add esp, 4*2
            
            cmp eax, 0
            je final
            
            mov bx, 7
            div bx
            
            cmp dx, 0
            je instr1 ;if the number is divisible by 7, it is added to the file
            
            
            instr1:
                push dword [read_number]
                push dword [descriptor]
                call [fprintf]
                add esp, 4*2
                
                
        jmp rpt
        
        final:
            push dword [descriptor]
            call [fclose]  
            add esp, 4 ;close the file
            
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program