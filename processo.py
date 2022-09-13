class Processo:

    def __init__(self, pid: object, te: object) -> object:
        self.pid = pid  # Identificador de Processo
        self.tp = 0  # Tempo de Processamento
        self.cp = self.tp + 1  # Contador de Programa
        self.ep = 'PRONTO'  # Estado do Processo
        self.nes = 0  # Número de vezes que realizou uma opração de E/S
        self.n_cpu = 0  # Número de vezes que usou a CPU
        self.te = te  # Tempo de Execução para terminar a execução

    def executando(self):
        print(f'{self.ep} >>> EXECUTANDO')
        self.ep = 'EXECUTANDO'

    def bloqueado(self):
        print(f'{self.ep} >>> BLOQUEADO')
        self.ep = 'BLOQUEADO'

    def pronto(self):
        print(f'{self.ep} >>> PRONTO')
        self.ep = 'PRONTO'

    def finalizado(self):
        print(f'{self.ep} >>> FINALIZADO')
        self.ep = 'FINALIZADO'

    def ep(self):
        return self.ep

    def add__nes(self):
        self.nes += 1

    def reset__nes(self):
        self.nes = 0

    def nes(self):
        return self.nes

    def add__tp(self):
        self.tp += 1

    def pid(self):
        return self.pid

    def cp(self):
        return self.cp

    def set_cp(self):
        self.cp = self.tp + 1

    def add_ncpu(self):
        self.n_cpu += 1

    def tp(self):
        return self.tp

    def te(self):
        return self.te

    def print(self):
        print(f'PID: {self.pid}\nTP: {self.tp}\nCP: {self.cp}\nEP: {self.ep}\nNES: {self.nes}\nNCPU: {self.n_cpu}\nTE: {self.te}')