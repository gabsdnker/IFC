.section .data
n:		.word 10	#Quantidade de termos 
fibonacci:		.space 40 #Espaços para 10 inteiros (4 bytes cada)

.section .text

.global _start
_start:
	la a0, fibonacci #a0 aponta para o início do array
	li a1, 0 #a1 = f(0)
	li a2, 1 #a2 = f(1)
	li a3, 0 #a3 = i (contador)
	lw a4, n #a4 = n (total de termos)

	#Salvar o primeiro termo
	sw a1, 0(a0)
	addi a3, a3, 1
	
	#Salvar o segundo termo
	sw a2, 4(a0)
	addi a3, a3, 1
	
loop:
    bge a3, a4, end #Se i >= n, fim
    add a5, a1, a2	 #a5 = a1 + a2 (próximo termo)

    slli a6, a3, 2  #a6= i * 4 (deslocamento de bytes)
    add a7, a0, a6 #a7= endereço do próximo espaço
    sw a5, 0(a7) 	#salva f(i) = a5

    mv a1, a2 	# atualiza a1 f(n-2)
    mv a2, a5 	 # atualiza a2 f(n-1)
	
    addi a3, a3, 1  # i++
    j loop #volta pro início do loop

end:
    j end  #loop infinito para encerrar o programa
	
	