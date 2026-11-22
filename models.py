class Imovel:
    """Classe base que representa um imóvel genérico da R.M Imóveis."""

    def __init__(self, tipo: str, valor_base: float, parcelas_contrato: int = 1):
        if not 1 <= parcelas_contrato <= 5:
            raise ValueError("A taxa contratual pode ser parcelada em no máximo 5 vezes.")
        self.tipo = tipo
        self.valor_base = valor_base
        self.taxa_contrato = 2000.00
        self.parcelas_contrato = parcelas_contrato

    def calcular_parcela_contrato(self) -> float:
        return self.taxa_contrato / self.parcelas_contrato

    def calcular_aluguel_mensal(self) -> float:
        return self.valor_base

    def obter_detalhamento(self) -> dict:
        """Retorna um dicionário com os componentes do valor para exibição transparente."""
        return {
            "Tipo de Imóvel": self.tipo,
            "Aluguel Base": self.valor_base,
            "Aluguel Mensal Final": self.calcular_aluguel_mensal(),
            "Taxa Contratual Total": self.taxa_contrato,
            "Parcelas do Contrato": f"{self.parcelas_contrato}x de R$ {self.calcular_parcela_contrato():.2f}"
        }


class Apartamento(Imovel):
    def __init__(self, quartos: int, tem_garagem: bool, tem_criancas: bool, parcelas_contrato: int):
        super().__init__(tipo="Apartamento", valor_base=700.00, parcelas_contrato=parcelas_contrato)
        self.quartos = quartos
        self.tem_garagem = tem_garagem
        self.tem_criancas = tem_criancas

    def calcular_aluguel_mensal(self) -> float:
        subtotal = self.valor_base
        if self.quartos == 2:
            subtotal += 200.00
        if self.tem_garagem:
            subtotal += 300.00

        # Desconto de 5% aplicado após os adicionais para clientes sem crianças
        if not self.tem_criancas:
            subtotal *= 0.95

        return round(subtotal, 2)

    def obter_detalhamento(self) -> dict:
        detalhes = super().obter_detalhamento()
        adicional_quartos = 200.00 if self.quartos == 2 else 0.00
        adicional_garagem = 300.00 if self.tem_garagem else 0.00
        subtotal = self.valor_base + adicional_quartos + adicional_garagem
        desconto = round(subtotal * 0.05, 2) if not self.tem_criancas else 0.00

        detalhes.update({
            "Quartos": f"{self.quartos} quarto(s) (+ R$ {adicional_quartos:.2f})",
            "Garagem": f"{'Sim' if self.tem_garagem else 'Não'} (+ R$ {adicional_garagem:.2f})",
            "Possui Crianças": "Sim" if self.tem_criancas else "Não (Desconto 5% aplicado)",
            "Valor do Desconto": f"- R$ {desconto:.2f}"
        })
        return detalhes


class Casa(Imovel):
    def __init__(self, quartos: int, tem_garagem: bool, parcelas_contrato: int):
        super().__init__(tipo="Casa", valor_base=900.00, parcelas_contrato=parcelas_contrato)
        self.quartos = quartos
        self.tem_garagem = tem_garagem

    def calcular_aluguel_mensal(self) -> float:
        total = self.valor_base
        if self.quartos == 2:
            total += 250.00
        if self.tem_garagem:
            total += 300.00
        return round(total, 2)

    def obter_detalhamento(self) -> dict:
        detalhes = super().obter_detalhamento()
        adicional_quartos = 250.00 if self.quartos == 2 else 0.00
        adicional_garagem = 300.00 if self.tem_garagem else 0.00

        detalhes.update({
            "Quartos": f"{self.quartos} quarto(s) (+ R$ {adicional_quartos:.2f})",
            "Garagem": f"{'Sim' if self.tem_garagem else 'Não'} (+ R$ {adicional_garagem:.2f})"
        })
        return detalhes


class Estudio(Imovel):
    def __init__(self, pacote_duas_vagas: bool, vagas_extras: int, parcelas_contrato: int):
        super().__init__(tipo="Estúdio", valor_base=1200.00, parcelas_contrato=parcelas_contrato)
        self.pacote_duas_vagas = pacote_duas_vagas
        self.vagas_extras = vagas_extras if pacote_duas_vagas else 0

    def calcular_aluguel_mensal(self) -> float:
        total = self.valor_base
        if self.pacote_duas_vagas:
            total += 250.00
            total += self.vagas_extras * 60.00
        return round(total, 2)

    def obter_detalhamento(self) -> dict:
        detalhes = super().obter_detalhamento()
        custo_estacionamento = (250.00 + self.vagas_extras * 60.00) if self.pacote_duas_vagas else 0.00
        total_vagas = (2 + self.vagas_extras) if self.pacote_duas_vagas else 0

        detalhes.update({
            "Estacionamento": f"{total_vagas} vaga(s) (+ R$ {custo_estacionamento:.2f})"
        })
        return detalhes