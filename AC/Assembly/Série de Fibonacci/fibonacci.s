.global _start
    .text

_start:
    li a0, 8          
    jal ra, fib       

    li a7, 93         
    ecall            

fib:
    addi sp, sp, -32
    sd ra, 24(sp)
    sd a0, 0(sp)

    beq a0, x0, IS_ZERO   
    li t0, 1
    beq a0, t0, IS_ONE    


    addi a0, a0, -1
    jal ra, fib
    sd a0, 8(sp)          


    ld a0, 0(sp)
    addi a0, a0, -2
    jal ra, fib

    ld t1, 8(sp)
    add a0, a0, t1

    j END_FIB

IS_ZERO:
    mv a0, x0
    j END_FIB

IS_ONE:
    li a0, 1

END_FIB:
    ld ra, 24(sp)
    addi sp, sp, 32
    ret
