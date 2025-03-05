# Gerador de Relatórios com Factory Method

## Descrição

Este projeto tem como principal objetivo implementar o padrão de projeto **Factory Method** em Python para a geração de relatórios em diferentes formatos: **TXT, CSV e JSON**. A abordagem permite criar novos formatos de relatório sem modificar o código principal, garantindo maior flexibilidade e aderência ao princípio **Open/Closed** (OCP) do SOLID.

## Tecnologias Utilizadas

- Python 3.x
- Bibliotecas padrão: `abc`, `json`, `csv`

## Estrutura do Projeto

```
/
├──requiriments.txt       # Documento com os requisitos para rodar o projeto
├── report_generators.py  # Implementação dos geradores de relatório
├── report_factories.py   # Implementação das fábricas (Factory Method)
├── main.py               # Execução do projeto
└── README.md             # Documentação do projeto
```

## Como Executar

1. **Certifique-se de ter o Python instalado.**
2. **Baixe ou clone este repositório:**
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```
3. **Execute o script principal:**
   ```bash
   python run.py
   ```

## Implementação do Factory Method

O projeto segue a estrutura do Factory Method, com:

- **Uma interface abstrata \*\*\*\*****`ReportGenerator`**, que define o método `generate_report()`.
- **Três classes concretas** (`TxtReportGenerator`, `CsvReportGenerator` e `JsonReportGenerator`) que implementam esse método para diferentes formatos.
- **Fábricas especializadas** (`FabricTxtReportGenerator`, `FabricCsvReportGenerator`, `FabricJsonReportGenerator`) que encapsulam a criação das instâncias de relatório.

## Exemplo de Uso

O código principal instancia as fábricas e gera os relatórios:

```python
# Criando um gerador de relatório TXT
fabric = FabricTxtReportGenerator()
generator = fabric.get_report()
generator.generate_report(lista_clientes, "relatorio.txt")
```

Isso garante que o código principal **não precise saber os detalhes da implementação de cada tipo de relatório**.

## Possíveis Melhorias

- Adicionar suporte a PDF (`reportlab`)
- Armazenar os relatórios em um banco de dados (`sqlite3`)
- Criar uma interface de linha de comando interativa

## Autor

Desenvolvido por **Bernardo Vieira**.

