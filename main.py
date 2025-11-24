from movies_base import MOVIES
from typing import Optional

class Node:
    def __init__(self, key, year):
        self.key = key
        self.year = year
        self.left = None
        self.right = None
        self.height = 1
        self.index = None  # índice estrutural (heap-like): raiz=1, left=2*i, right=2*i+1


class AVLTree:

    # --------------------------------
    # Atribuição de índices estruturais
    # --------------------------------
    def assign_indices(self, root: Optional[Node]):
        def _assign(node, idx):
            if not node:
                return
            node.index = idx
            _assign(node.left, idx * 2)
            _assign(node.right, idx * 2 + 1)
        _assign(root, 1)

    # --------------------------------
    # Helpers de logging (estética)
    # --------------------------------
    def _format_node_mention(self, node: Optional[Node]):
        if not node:
            return "None"
        if node.index is None:
            return f"[#?] {node.key}"
        return f"[#{node.index}] {node.key}"

    def _log_path(self, direction):
        if direction == "L":
            print("   ↓ esquerda")
        else:
            print("   ↓ direita")

    def _log_rotation(self, tipo, node):
        # node pode ser Node ou string
        if isinstance(node, Node):
            node_repr = self._format_node_mention(node)
        else:
            node_repr = str(node)
        print(f'\nÁrvore reequilibrada: Rotação à {tipo} em "{node_repr}"')

    # --------------------------------
    # Funções AVL clássicas
    # --------------------------------
    def get_height(self, node: Optional[Node]):
        if not node:
            return 0
        return node.height

    def get_balance(self, node: Optional[Node]):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y: Node):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def left_rotate(self, x: Node):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    # =====================================================
    # INSERT com log estilo "Árvore Viva" e suporte de índices
    # =====================================================
    def insert(self, root: Optional[Node], key, year, *, _log=False):
        """
        Se _log=True: exibe o percurso (com índices atuais), setas de direção,
        marca [INSERIU AQUI], e logs de rotações (com menção de nós).
        Atribui índices antes do início (para que o log mostre os índices atuais)
        e reatribui após a inserção para refletir a nova estrutura.
        """

        if _log:
            self.assign_indices(root)

        if _log:
            print(f'\nInserindo: "{key}" ({year})\n')

        def _insert(node, key, year):
            if not node:
                print("[INSERIU AQUI]")
                return Node(key, year)

            # exibir menção do nó atual durante o percurso
            print(self._format_node_mention(node))

            if key < node.key:
                self._log_path("L")
                node.left = _insert(node.left, key, year)
            elif key > node.key:
                self._log_path("R")
                node.right = _insert(node.right, key, year)
            else:
                return node

            node.height = 1 + max(self.get_height(node.left),
                                  self.get_height(node.right))

            balance = self.get_balance(node)

            # LL
            if balance > 1 and key < node.left.key:
                # log usando nó atual (com índice possivelmente pré-inserção)
                self._log_rotation("Direita", node)
                return self.right_rotate(node)

            # RR
            if balance < -1 and key > node.right.key:
                self._log_rotation("Esquerda", node)
                return self.left_rotate(node)

            # LR
            if balance > 1 and key > node.left.key:
                # mostrar rotações compostas; exibir o filho afetado também
                self._log_rotation("Esquerda", node.left)
                node.left = self.left_rotate(node.left)
                self._log_rotation("Direita", node)
                return self.right_rotate(node)

            # RL
            if balance < -1 and key < node.right.key:
                self._log_rotation("Direita", node.right)
                node.right = self.right_rotate(node.right)
                self._log_rotation("Esquerda", node)
                return self.left_rotate(node)

            return node

        new_root = _insert(root, key, year)

        # após a inserção, reatribua índices para refletir a nova estrutura
        if _log:
            self.assign_indices(new_root)
            # localizar o nó inserido para mostrar sua menção final
            inserted_node = self.search(new_root, key)
            if inserted_node:
                print(f'\nInserido em {self._format_node_mention(inserted_node)}')

        return new_root

    # =====================================================
    # BUSCA (permanece recursiva); show_node usa índices
    # =====================================================
    def search(self, root: Optional[Node], key):
        if root is None:
            return None
        if key == root.key:
            return root
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def show_node(self, node: Node):
        print("\n===== FILME ENCONTRADO =====")
        print(f"Título: {self._format_node_mention(node)}")
        print(f"Ano: {node.year}")
        print(f"Altura: {node.height}")
        left_repr = self._format_node_mention(node.left) if node.left else "None"
        right_repr = self._format_node_mention(node.right) if node.right else "None"
        print(f"Left : {left_repr}")
        print(f"Right: {right_repr}")
        print("============================")

    # =====================================================
    def inorder(self, root: Optional[Node], results):
        if root:
            self.inorder(root.left, results)
            results.append((root.key, root.year, root.index))
            self.inorder(root.right, results)

    def count_nodes(self, root: Optional[Node]):
        if not root:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)


# =========================================================
# MENU / UI
# =========================================================

def mostrar_menu():
    print("\n===== MENU =====")
    print("1 - Buscar filme")
    print("2 - Inserir novo filme")
    print("3 - Listar filmes em ordem alfabética")
    print("4 - Mostrar estatísticas da árvore")
    print("0 - Sair")
    return input("Escolha uma opção: ")


# =========================================================
# MAIN
# =========================================================

def main():
    tree = AVLTree()
    root = None

    # Carregar filmes iniciais (sem log). Depois atribuímos índices.
    for movie in MOVIES:
        root = tree.insert(root, movie["title"], movie["year"])
    tree.assign_indices(root)

    print("Árvore AVL carregada com 100 filmes!")

    while True:
        opcao = mostrar_menu()

        # ================== BUSCAR ==================
        if opcao == "1":
            query = input("Digite o título do filme: ").strip()
            result = tree.search(root, query)
            if result:
                # garantir índices atualizados antes de exibir (por segurança)
                tree.assign_indices(root)
                tree.show_node(result)
            else:
                print("\nFilme não encontrado.")

        # ================== INSERIR ==================
        elif opcao == "2":
            titulo = input("Título do novo filme: ").strip()
            try:
                ano = int(input("Ano de lançamento: "))
            except ValueError:
                print("Ano inválido. Tente novamente.")
                continue

            # insert com log e reatribuição de índices interna
            root = tree.insert(root, titulo, ano, _log=True)
            print("\nFilme inserido com sucesso!")

        # ================== LISTAR ==================
        elif opcao == "3":
            # garantir índices atualizados
            tree.assign_indices(root)
            lista = []
            tree.inorder(root, lista)
            print("\n=== FILMES EM ORDEM ALFABÉTICA ===")
            for i, (t, a, idx) in enumerate(lista, start=1):
                idx_repr = f"[#{idx}]" if idx is not None else "[#?]"
                print(f"{i} — {idx_repr} {t} ({a})")
            print("=================================")

        # ================== ESTATÍSTICAS ==================
        elif opcao == "4":
            # garantir índices atualizados
            tree.assign_indices(root)
            num_nos = tree.count_nodes(root)
            altura = tree.get_height(root)
            balanceamento = tree.get_balance(root)

            print("\n=== ESTATÍSTICAS DA ÁRVORE ===")
            print(f"Número de nós: {num_nos}")
            print(f"Altura da árvore: {altura}")
            print(f"Fator de balanceamento da raiz: {balanceamento}")
            print("================================")

        elif opcao == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
