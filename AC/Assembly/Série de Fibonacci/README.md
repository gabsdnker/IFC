# Trabalho de Implementação

✅ Objetivo:

Calcular a série de Fibonacci até o n-ésimo termo, onde n é definido diretamente no código.

📌 Premissas:

O primeiro termo é 0, o segundo é 1, como em:
0, 1, 1, 2, 3, 5, 8, 13, ...

O resultado será armazenado em memória.

O código será compatível com simuladores como Spike ou QEMU, ou com montagem/linkagem usando riscv64-unknown-elf-gcc no Windows.

- Simulador: Cpulator

- Formula Fibonacci
    - F(n) = F(n-1) + F(n-2)

Para programar, primeiro inicializamos os registradores, depois fazemos a função.

- Windows 
    - Instalar o MSYS2: https://www.msys2.org/ 
    - Abra o terminal MSYS2 MSYS
    - Instale os pacotes:
        ``pacman -Syu``
        ``pacman -S riscv64-elf-gcc riscv64-elf-binutils make``
        Obs.: Isso instala ``riscv64-elf-as``, ``ld``, ``gcc``, etc. 

Desenvolvido por Gabriel Rodrigues, Gabrielli Danker e Mateus Dall'gna