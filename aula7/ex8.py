from fila import Fila
requisicao = Fila ()
requisicao.enqueue('get /usuarios')
requisicao.enqueue('get /login')
requisicao.enqueue('post /aluno')
 
while not requisicao.vazia():
    req = requisicao.dequeue()
    print (req)