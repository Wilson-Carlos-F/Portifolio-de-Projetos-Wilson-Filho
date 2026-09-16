Coca_zero = 6.00
Passa_Tempo = 5.00
Papel_Higienico = 2.76

print("Olá meu cliente lindo, maravilhoso, e fantástico! Seja bem vindo ao Mix Alexandre, o melhor mercado da cidade! Aqui você encontra os melhores produtos com os melhores preços! \n")
print("Então, vamos começar a nossa compra! \n")

Quantidade_Coca_zero = int(input("Quantas Coca zero você deseja comprar?: "))
Quantidade_Passa_Tempo = int(input("Quantos Passa Tempo você deseja comprar?: "))
Quantidade_Papel_Higienico = int(input("Quantos Pacotes de Papel Higienico você deseja comprar?:"))

def calculo_da_compra(Quantidade_Coca_zero, Quantidade_Passa_Tempo, Quantidade_Papel_Higienico):
    total = (Coca_zero * Quantidade_Coca_zero) + (Passa_Tempo * Quantidade_Passa_Tempo) + (Papel_Higienico * Quantidade_Papel_Higienico)
    return total

Forma_de_Pagamento = input("Qual a forma de pagamento? (Dinheiro, Crédito, Débito ou Pix): ")

print("Sua compra ficou assim \n")
print(f"\nCoca zero: {Quantidade_Coca_zero} x R${Coca_zero:.2f} = R${Coca_zero * Quantidade_Coca_zero:.2f}")
print(f"Passa Tempo: {Quantidade_Passa_Tempo} x R${Passa_Tempo:.2f} = R${Passa_Tempo * Quantidade_Passa_Tempo:.2f}")
print(f"Papel Higienico: {Quantidade_Papel_Higienico} x R${Papel_Higienico:.2f} = R${Papel_Higienico * Quantidade_Papel_Higienico:.2f}")
total_da_compra = calculo_da_compra(Quantidade_Coca_zero, Quantidade_Passa_Tempo, Quantidade_Papel_Higienico)
print(f"Total da compra: R${total_da_compra:.2f} \n")
print(f"Forma de pagamento: {Forma_de_Pagamento} \n")
print("Compra aprovada! Muito obrigado por comprar no Mix Alexandre, volte sempre! \n")