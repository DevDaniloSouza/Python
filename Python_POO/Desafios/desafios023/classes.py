class Carrinho:
    def __init__(self) -> None:
        self.produtos = []
        self.total = 0

    def __iadd__(self, other):
        self.produtos.append(other)
        self.total += other.valor
        return self

    def __add__(self, other):
        self.produtos.append(other)
        self.total += other.valor
        return self

    def __str__(self) -> str:
        msg = "-" * 25
        for item in self.produtos:
            msg += f"\n{item.produto} (R$ {item.valor:,.2f})"
        msg += "\n"
        msg += "-" * 25
        msg += f"\nTotal: R$ {self.total:,.2f}"
        return msg

        
class Produto:
    def __init__(self, produto, preco) -> None:
        self.produto = produto
        self.valor = preco

    def __str__(self) -> str:
        return f"`{self.produto} (R$ {self.valor:,.2f})"

