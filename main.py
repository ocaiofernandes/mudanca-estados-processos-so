from random import random
from processo import Processo


def chance():  # Gera um número aleatório entre 0 e 1
    return random()


# Processos em execução
processos = [Processo(0, 10000),
             Processo(1, 5000),
             Processo(2, 7000),
             Processo(3, 3000),
             Processo(4, 3000),
             Processo(5, 8000),
             Processo(6, 2000),
             Processo(7, 5000),
             Processo(8, 4000),
             Processo(9, 10000)]
quantum = 1000
finalizados = 0

while finalizados < 10:
    if finalizados == 10:
        break

    for processo in processos:
        if processo.ep == 'PRONTO':
            processo.executando()
            processo.add_ncpu()
            realizou_es = False

            for i in range(1, quantum + 1):
                if processo.tp == processo.te:
                    finalizados += 1
                    processo.finalizado()
                    processo.print()
                    processos.remove(processo)
                    break

                processo.add__tp()
                processo.set_cp()

                print(f'PID: {processo.pid}')
                print(f'CP: {processo.cp}')

                if chance() <= 0.05:
                    realizou_es = True
                    processo.add__nes()
                    processo.bloqueado()
                    break

            if not realizou_es:
                processo.pronto()
                processo.print()

        else:
            if chance() <= 0.3:
                processo.pronto()