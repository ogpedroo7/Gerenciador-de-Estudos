nome = input("Digite o nome da matéria: ")
nivel = input("Digite o nível da matéria (iniciante, intermediário, avançado): ")
horas_estudadas = int(input("Digite o número de horas estudadas: "))
progresso = int(input("Digite o progresso da matéria (em %): "))




if progresso < 0 or progresso > 100:
    print("Erro: O progresso deve estar entre 0 e 100%.")

else:
    print("Progresso registrado com sucesso!")    

    if progresso >= 100:
        print("Parabéns! Você concluiu a matéria!")

    elif progresso >= 90:
        print("Você está prestes a concluir a matéria, continue assim cara!")    

    elif progresso >= 75:
        print("Você está quase completando a matéria! Continue se esforçando!")    

    elif progresso >= 50:
        print("Você chegou na metade do caminho! Continue assim!")    

    elif progresso >= 30:
        print("Você está indo muito bem! Belo progresso!")

    elif progresso >= 15:
        print("Você já está no caminho certo!")

    elif progresso >= 1:
        print("Você começou a estudar!")

    else:
        print("Você ainda não começou a estudar!")


def mostrar_matéria(nome, nivel, horas_estudadas, progresso):
        print(f"Matéria: {nome}")
        print(f"Nível: {nivel}")
        print(f"Horas estudadas: {horas_estudadas}")
        print(f"Progresso: {progresso}%")



def verificar_progresso(progresso):
            if progresso < 0 or progresso > 100:
                print("Erro: O progresso deve estar entre 0 e 100%.")
            else:
                print("Progresso registrado com sucesso!")    

                if progresso >= 100:
                    print("Parabéns! Você concluiu a matéria!")

                elif progresso >= 90:
                    print("Você está prestes a concluir a matéria, continue assim cara!")    

                elif progresso >= 75:
                    print("Você está quase completando a matéria! Continue se esforçando!")    

                elif progresso >= 50:
                    print("Você chegou na metade do caminho! Continue assim!")    

                elif progresso >= 30:
                    print("Você está indo muito bem! Belo progresso!")

                elif progresso >= 15:
                    print("Você já está no caminho certo!")

                elif progresso >= 1:
                    print("Você começou a estudar!")

                else:
                    print("Você ainda não começou a estudar!")


def mostrar_mensagem():
    print("Sistema de Gerenciamento de Estudos")


mostrar_mensagem()

mostrar_matéria(nome, nivel, horas_estudadas, progresso)

verificar_progresso(progresso)

