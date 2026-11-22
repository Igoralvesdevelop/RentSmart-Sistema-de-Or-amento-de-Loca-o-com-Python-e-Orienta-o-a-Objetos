from models import Apartamento, Casa, Estudio, Imovel
from orcamento import OrcamentoLocacao


def ler_opcao_inteira(mensagem: str, opcoes_validas: list[int]) -> int:
    while True:
        try:
            valor = int(input(mensagem))
            if valor in opcoes_validas:
                return valor
            print(f"Opção inválida. Escolha entre {opcoes_validas}.")
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")


def ler_inteiro_nao_negativo(mensagem: str) -> int:
    while True:
        try:
            valor = int(input(mensagem))
            if valor >= 0:
                return valor
            print("O valor não pode ser negativo.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido.")


def ler_sim_nao(mensagem: str) -> bool:
    while True:
        resposta = input(mensagem).strip().upper()
        if resposta in ("S", "SIM"):
            return True
        if resposta in ("N", "NAO", "NÃO"):
            return False
        print("Resposta inválida. Digite 'S' para Sim ou 'N' para Não.")


def criar_imovel_interativo() -> Imovel:
    print("\n--- RENTSMART | NOVO ORÇAMENTO DE LOCAÇÃO ---")
    print("Selecione a categoria do imóvel:")
    print("1 - Apartamento (Base: R$ 700,00)")
    print("2 - Casa        (Base: R$ 900,00)")
    print("3 - Estúdio     (Base: R$ 1.200,00)")

    categoria = ler_opcao_inteira("Opção (1/2/3): ", [1, 2, 3])
    parcelas = ler_opcao_inteira("Em quantas parcelas deseja pagar a taxa contratual de R$ 2.000,00? (1 a 5): ", [1, 2, 3, 4, 5])

    if categoria == 1:
        quartos = ler_opcao_inteira("Quantidade de quartos (1 ou 2): ", [1, 2])
        garagem = ler_sim_nao("Deseja incluir 1 vaga de garagem (+ R$ 300,00)? [S/N]: ")
        criancas = ler_sim_nao("Algum morador possui crianças? [S/N]: ")
        return Apartamento(quartos=quartos, tem_garagem=garagem, tem_criancas=criancas, parcelas_contrato=parcelas)

    elif categoria == 2:
        quartos = ler_opcao_inteira("Quantidade de quartos (1 ou 2): ", [1, 2])
        garagem = ler_sim_nao("Deseja incluir 1 vaga de garagem (+ R$ 300,00)? [S/N]: ")
        return Casa(quartos=quartos, tem_garagem=garagem, parcelas_contrato=parcelas)

    else:
        pacote_vagas = ler_sim_nao("Deseja contratar o pacote inicial de 2 vagas de estacionamento (+ R$ 250,00)? [S/N]: ")
        vagas_extras = 0
        if pacote_vagas:
            vagas_extras = ler_inteiro_nao_negativo("Quantas vagas adicionais além das 2 iniciais deseja incluir (+ R$ 60,00 cada)? ")
        return Estudio(pacote_duas_vagas=pacote_vagas, vagas_extras=vagas_extras, parcelas_contrato=parcelas)


def main():
    while True:
        imovel_selecionado = criar_imovel_interativo()
        orcamento = OrcamentoLocacao(imovel_selecionado)

        orcamento.exibir_resumo()
        arquivo_gerado = orcamento.gerar_csv_projecao_anual()
        print(f"[OK] Projeção financeira de 12 meses exportada para: '{arquivo_gerado}'")

        if not ler_sim_nao("\nDeseja realizar um novo orçamento? [S/N]: "):
            print("Encerrando o sistema RentSmart. Até logo!")
            break


if __name__ == "__main__":
    main()