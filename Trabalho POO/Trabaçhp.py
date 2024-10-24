class Produto:
    def __init__(self, id_produto, nome_produto, valor_unitario, tamanho, quantidade_estoque):
        self.id_produto = id_produto
        self.nome_produto = nome_produto
        self.valor_unitario = valor_unitario
        self.tamanho = tamanho #PP, P, M, G, GG, XG, X1, X2, X3, X4
        self.quantidade_estoque = quantidade_estoque


class Pedido(Produto):
    def __init__(self, nome_produto, valor_unitario, tamanho, quantidade_estoque, id_pedido, itens):
       # super().__init__(id_produto, nome_produto, valor_unitario, tamanho, quantidade_estoque)
        self.id_pedido = id_pedido #nota fiscal
        self.itens = itens #quantidade vendida
        self.valor_pedido = valor_pedido


class Cliente(Pedido):
    def __init__(self, id_cliente, nome_cliente, cpf, telefone, email, endereço):
       # super().__init__(nome, preco, tamanho, quantidade_estoque, id_pedido, itens)
       self.id_cliente = id_cliente
       self.nome_cliente = nome_cliente
       self.cpf = cpf
       self.telefone = telefone
       self.email = email
       self.endereço = endereço


       
    


    

    