;Read a string of unsigned numbers in base 10 from keyboard. Determine the maximum value of the string and write it in the file max.txt (it will be created) in 16  base.
;Read a string of unsigned numbers in base 10 from keyboard. Determine the minimum value of the string and write it in the file min.txt (it will be created) in 16 base.

bits 32

; indicate to the assembler that the function _sumNumbers should be available to other compile units
global _min

; the linker may use the public data segment for external datta
segment data public data use32

; the code written in assembly language resides in a public segment, that may be shared with external code
segment code public code use32

; int sumNumbers(int, int)
; cdecl call convention
_min:
    ; create a stack frame
    push ebp
    mov ebp, esp
    
    ; retreive the function's arguments from the stack
    ; [ebp+4] contains the return value 
    ; [ebp] contains the ebp value for the caller
    mov eax, [ebp + 8]        ; eax <- a
    
    mov ebx, [ebp + 12]        ; ebx <- b
    
    cmp eax, ebx ; ”compares” the values stored in the two registers (fictional subtraction eax-ebx)
    jl done
    mov eax,ebx    ;Depending on the conditional jump instruction used (here JLE), the comparison criteria is established.
    ;In this case: If the EAX content in the signed interpretation is less than or equal to the content in EBX then JUMP to the Done label. 
    ;Otherwise continue with the following instruction (the flag being tested here is ZF).
    done:
    ;instructions after the label 'done'

    ; restore the stack frame
    mov esp, ebp
    pop ebp

    ret
    ; cdecl call convention - the caller will remove the parameters from the stack
