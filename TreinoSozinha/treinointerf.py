import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QLineEdit, QMessageBox

lista = []

class ListaTarefas(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lista de Tarefas")
        self.setGeometry(200, 200, 400, 300)

        # Layout principal
        layout = QVBoxLayout()

        # Campo de entrada
        self.entrada = QLineEdit()
        self.entrada.setPlaceholderText("Digite uma tarefa...")
        layout.addWidget(self.entrada)

        # Botões
        botoes = QHBoxLayout()
        btnAdd = QPushButton("Adicionar")
        btnRemove = QPushButton("Remover")
        btnListar = QPushButton("Listar")
        btnSair = QPushButton("Sair")

        botoes.addWidget(btnAdd)
        botoes.addWidget(btnRemove)
        botoes.addWidget(btnListar)
        botoes.addWidget(btnSair)
        layout.addLayout(botoes)

        # Lista visual
        self.listaBox = QListWidget()
        layout.addWidget(self.listaBox)

        # Conectar botões às funções
        btnAdd.clicked.connect(self.adicionaTarefa)
        btnRemove.clicked.connect(self.removerTarefa)
        btnListar.clicked.connect(self.listarTarefa)
        btnSair.clicked.connect(self.close)

        self.setLayout(layout)

    def adicionaTarefa(self):
        tarefa = self.entrada.text().capitalize()
        if tarefa:
            lista.append(tarefa)
            self.listarTarefa()
            self.entrada.clear()
        else:
            QMessageBox.warning(self, "Aviso", "Digite uma tarefa!")

    def listarTarefa(self):
        self.listaBox.clear()
        for tarefa in lista:
            self.listaBox.addItem(tarefa)

    def removerTarefa(self):
        selecionado = self.listaBox.currentRow()
        if selecionado >= 0:
            tarefa_removida = lista.pop(selecionado)
            self.listarTarefa()
            QMessageBox.information(self, "Removido", f"Tarefa removida: {tarefa_removida}")
        else:
            QMessageBox.warning(self, "Aviso", "Selecione uma tarefa para remover!")

# Executar aplicação
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = ListaTarefas()
    janela.show()
    sys.exit(app.exec())
