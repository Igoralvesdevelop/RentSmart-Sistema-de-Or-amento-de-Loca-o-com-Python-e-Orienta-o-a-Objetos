import csv
from models import Imovel


class OrcamentoLocacao:
    """Responsável por formatar o resumo comercial e gerar a projeção anual em CSV."""

    def __init__(self, imovel: Imovel):
        self.imovel = imovel

    def exibir_resumo(self) -> None:
        detalhes = self.imovel.obter_detalhamento()
        aluguel_mensal = self.imovel.calcular_aluguel_mensal()
        parcela_contrato = self.imovel.calcular_parcela_contrato()

        print("\n" + "=" * 55)
        print("           ORÇAMENTO DE LOCAÇÃO - R.M IMÓVEIS")
        print("=" * 55)
        print(f"Categoria:              {detalhes['Tipo de Imóvel']}")
        print(f"Aluguel Base:           R$ {detalhes['Aluguel Base']:.2f}")

        if "Quartos" in detalhes:
            print(f"Configuração Quartos:   {detalhes['Quartos']}")
        if "Garagem" in detalhes:
            print(f"Vaga de Garagem:        {detalhes['Garagem']}")
        if "Estacionamento" in detalhes:
            print(f"Estacionamento:         {detalhes['Estacionamento']}")
        if "Possui Crianças" in detalhes:
            print(f"Possui Crianças:        {detalhes['Possui Crianças']}")
            print(f"Desconto Aplicado:      {detalhes['Valor do Desconto']}")

        print("-" * 55)
        print(f"VALOR DO ALUGUEL MENSAL: R$ {aluguel_mensal:.2f}")
        print("-" * 55)
        print("CONDIÇÕES DA TAXA CONTRATUAL (Custo Separado):")
        print(f"Taxa Total de Contrato:  R$ {self.imovel.taxa_contrato:.2f}")
        print(f"Parcelamento Escolhido:  {self.imovel.parcelas_contrato}x de R$ {parcela_contrato:.2f}")
        print("=" * 55 + "\n")

    def gerar_csv_projecao_anual(self, nome_arquivo: str = "projecao_12_meses.csv") -> str:
        aluguel_mensal = self.imovel.calcular_aluguel_mensal()
        parcela_contrato = self.imovel.calcular_parcela_contrato()
        total_parcelas = self.imovel.parcelas_contrato

        with open(nome_arquivo, mode="w", newline="", encoding="utf-8-sig") as arquivo_csv:
            escritor = csv.writer(arquivo_csv, delimiter=";")
            escritor.writerow([
                "Mês",
                "Aluguel Mensal (R$)",
                "Parcela Taxa Contratual (R$)",
                "Total Previsto no Mês (R$)"
            ])

            for mes in range(1, 13):
                valor_parcela_mes = parcela_contrato if mes <= total_parcelas else 0.00
                total_mes = aluguel_mensal + valor_parcela_mes

                escritor.writerow([
                    f"Mês {mes:02d}",
                    f"{aluguel_mensal:.2f}".replace(".", ","),
                    f"{valor_parcela_mes:.2f}".replace(".", ","),
                    f"{total_mes:.2f}".replace(".", ",")
                ])

        return nome_arquivo