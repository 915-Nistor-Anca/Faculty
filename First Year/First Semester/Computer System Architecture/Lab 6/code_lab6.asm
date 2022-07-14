bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    s dd 12345678h, 1256ABCDh, 12AB4344h
    l equ ($ - s)/4
    ok db 0
    pos db 0
    low_words times l dw 0
    ;A string of doublewords is given. Order in decreasing order the string of the low words (least significant) from these doublewords. The high words (most significant) remain unchanged.

; our code starts here
segment code use32 class=code
    start:
        mov ecx, l
        mov esi, 2
        jecxz stop
        
        rep1:
            mov ax, [s + esi-2]
            mov [low_words + esi], ax
            add esi, 4
        loop rep1
        ; low words are saved in another string
        
        stop:
        ;sorting these low words (bubble sort):
        
        mov byte[ok], 0
        jmp do
        do:
            mov byte[ok], 1
            mov ecx, l-1
            mov esi, 0
            jecxz condition
            
            _for:
                mov ax, [low_words + esi + 2]
                mov bx, [low_words + esi + 6]
                cmp ax, bx
                add esi, 4
                jg et1 ; jumps at et1 if ax > bx
                et1:
                    mov byte[ok], 0 
                    mov [low_words + esi - 2], bx
                    mov [low_words + esi + 2], ax ;we swap the values
            loop _for

        condition:
        cmp byte [ok], 0
        je do
        ; the low words are sorted
        
        
        mov ecx, l
        jecxz done
        mov esi, 2
        rep2:
            mov ax, [low_words + esi-2]
            mov [s + esi], ax
            add esi, 4
        loop rep2 ; we modify the low words of the initial string using the second string
        done:
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program