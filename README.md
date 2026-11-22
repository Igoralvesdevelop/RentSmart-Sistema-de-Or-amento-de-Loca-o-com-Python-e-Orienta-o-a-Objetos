# RentSmart — Sistema de Orçamento de Locação (R.M Imóveis)

Aplicação desenvolvida em Python utilizando Programação Orientada a Objetos (POO) para automatizar o cálculo de orçamentos de locação residencial (Apartamentos, Casas e Estúdios) e gerar projeções financeiras anuais em CSV.

## Estrutura do Projeto

- `models.py`: Contém a hierarquia de classes (`Imovel`, `Apartamento`, `Casa`, `Estudio`) com encapsulamento das regras de negócio, adicionais, descontos e parcelamento da taxa contratual.
- `orcamento.py`: Classe `OrcamentoLocacao` responsável por formatar a exibição do orçamento e exportar a planilha `projecao_12_meses.csv`.
- `main.py`: Ponto de entrada da aplicação com menu interativo em linha de comando e validação de entradas.


## Requisitos

- Python 3.10 ou superior (utiliza apenas bibliotecas padrão: `csv` e `unittest`).

## Como Executar

1. Clone o repositório:
   ```bash
   git clone <URL_DO_SEU_REPOSITORIO>
   cd rentsmart-rm-imoveis
