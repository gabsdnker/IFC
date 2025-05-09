# 📚 Assistente de Estudos com Agenda Inteligente

Este projeto é um sistema de gerenciamento de tarefas e projetos voltado para estudantes, que oferece uma interface gráfica simples e sugestões inteligentes baseadas em horários. A aplicação foi desenvolvida em Java e utiliza ***6 Padrões de Projeto*** como parte da arquitetura.

## 🚀 Funcionalidades

- Cadastro e visualização de tarefas
- Organização de tarefas dentro de projetos
- Sugestões inteligentes baseadas na hora do dia
- Interface gráfica simples com `Swing`
- Aplicação de padrões de projeto consagrados


---

## 🧠 Padrões de Projeto Utilizados

| Padrão             | Local de Aplicação |
|--------------------|---------------------|
| **Singleton**      | `GerenciadorDeTarefas.java` para garantir instância única do gerenciador |
| **Factory Method** | `FabricaTarefa.java` e `FabricaProjeto.java` para criação padronizada de objetos |
| **Strategy**       | `SugeridorInteligente.java` usa estratégias diferentes para sugerir tarefas |
| **Observer**       | `InterfaceGrafica.java` observa o `GerenciadorDeTarefas` e atualiza a interface |
| **Command**        | `ComandoAdicionarTarefa.java` encapsula ações de adicionar tarefa |
| **MVC (Model-View-Controller)** | Separação entre `Modelo`, `Controle` e `InterfaceGrafica (View)` |

---

## 🗂️ Estrutura de Pacotes

src/
├── InterfaceGrafica.java
├── Controle/
│   ├── ControladorDeTarefas.java
│   └── GerenciadorDeTarefas.java
├── Modelo/
│   ├── Tarefa.java
│   └── Projeto.java
├── Servico/
│   ├── SugeridorInteligente.java
│   ├── EstrategiaSugestao.java
│   ├── EstrategiaHorario.java
│   └── EstrategiaAleatoria.java
├── Fabrica/
│   ├── FabricaTarefa.java
│   └── FabricaProjeto.java
├── Observer/
│   └── ObservadorTarefa.java
│   └── ObservadorTarefaImpl.java
└── Command/
    ├── Comando.java
    └── ComandoAdicionarTarefa.java

---

## 🎓 Tecnologias Utilizadas

- Java 11+
- Swing (GUI)
- Padrões de Projeto (GoF)

---

## 🧪 Como Executar

1. Clone o repositório
2. Compile todos os arquivos Java
3. Execute `InterfaceGrafica.java`

javac *.java

java InterfaceGrafica

## 🧾 Licença
Este projeto é apenas para fins acadêmicos. Todos os direitos reservados ao autor.

## 👨‍💻 Autor
Desenvolvido por Gabrielli Danker — Aluna do Instituto Federal Catarinense, Campus Blumenau.

<img src="https://github.com/gabsdnker/IFC/blob/main/PAP/Projeto%20Final/images/Inicio.PNG" alt="Imagem do Projeto" width="400" height="800">
