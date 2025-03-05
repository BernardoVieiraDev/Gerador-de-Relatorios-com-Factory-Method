from report_factories import *

# Dados de exemplo de clientes
# Esses dados serão usados para gerar os relatórios.
lista_clientes = [
        {'Nome': 'João', 'Endereço': 'Rua A'},
        {'Nome': 'Maria', 'Endereço': 'Rua B'},
        {'Nome': 'Carlos', 'Endereço': 'Rua C'},
]

if __name__ == '__main__':
    
        # Exemplo de uso do padrão Factory Method para gerar um relatório TXT
        # A fábrica cria o gerador apropriado, que em seguida gera o relatório.
        generate_report(FactoryTxtReportGenerator(), lista_clientes, "relatorio_cliente.txt")


        # Exemplo de uso do padrão Factory Method para gerar um relatório CSV
        generate_report(FactoryCsvReportGenerator(), lista_clientes, "relatorio_cliente.csv")

        # Exemplo de uso do padrão Factory Method para gerar um relatório JSON
        generate_report(FactoryJsonReportGenerator(), lista_clientes, "relatorio_cliente.json")