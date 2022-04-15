%include "io64.inc"

section .text

global CHAIN

CHAIN:

    mov eax, 10

    PRINT_DEC 1, eax
    

    xor rax, rax

    ret