def calcular(num1, num2, operacao):
    operacoes = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "Erro: Divisão por zero!"
    }
    
    if operacao not in operacoes:
        return "Operação inválida!"
        
    resultado = operacoes[operacao](num1, num2)
    return f"{resultado:.2f}" if isinstance(resultado, float) else resultado

def main():
    while True:
        print("\nCalculadora Simples")
        print("Digite 'sair' para encerrar")
        
        entrada1 = input("\nDigite o primeiro número: ")
        if entrada1.lower() == 'sair':
            break
            
        try:
            num1 = float(entrada1)
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação (+, -, *, /): ")
            
            resultado = calcular(num1, num2, operacao)
            print(f"\nResultado: {resultado}")
            
        except ValueError:
            print("Erro: Digite apenas números válidos!")
        except Exception as e:
            print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
