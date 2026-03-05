# TSP_a280

> [!NOTE]
> O único uso de IA foi na parte da classe na função `__repr__`, pois não sabia como utilizar a função `__str__` quando o objeto estava dentro de uma lista.  
> O resto do código foi criado por mim.

## Problema
O problema escolhido foi o a280 da TSPLib, o qual consiste em pontos que devem ser minerados de forma eficiente, escolhendo a menor rota.  
Há 280 pontos no arquivo do problema, com suas respectivas coordenadas (x;y) e o método usado para calcular a distância: euclidiana.  

> [!CAUTION] 
> É necessário arredondar os valores obtidos pela raiz quadrada ao calcular as distâncias

## Abordagem
A abordagem escolhida foi a heurísitca de, dado um nó inicial, escolher o nó com a menor distância até ele.  
Além disso, para evitar que demorasse muito, caso o número de elementos aumentasse, decidi verificar apenas algumas vezes e sempre escolhendo um nó inicial aleatório.  
No final do código, será mostrado o caminho encontrado, a sua distância percorrida e comparando-o com o melhor caminho, calculando o erro percentual.

## Dependências e como rodar
Esse código enm python usa apenas as bibliotecas nativas, assim não é necessário instalar nenhuma dependência.  
Só é necessário baixar os seguintes arquivos desse repositório:
- [tsp.py](./tsp.py)
- [a280.tsp](./a280.tsp)
- [a280.opt.tour](./a280.opt.tour)

Após o download, basta colocá-los em um mesmo diretório e executar o arquivo python ([tsp.py](./tsp.py))

## Resultados obtidos
Após alguns testes, observei que os melhores resultados obtidos ficavam em torno de 12% a cima do valor esperado (obtido através do [gabarito](./a280.opt.tour).

## Discussão
Esse código possui algumas limitações, pois pode encontrar um caminho que seja ótimo localmente, mas não o melhor caminho, dado que o algoritmo utilizado é guloso, sempre tenta minimizar a distância.  
Dessa forma, um dos pontos a se melhorar é a heurísitca utilizada, para permitir escolher um caminho maior para conseguir pegar caminhos mais curtos no futuro.
