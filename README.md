# TSP_a280

## Problema
O problema escolhido foi o a280 da TSPLib, o qual consistiria em pontos que devem ser minerados de forma eficiente (a menor rota).  
Há 280 pontos no arquivo do problema, com suas respectivas coordenadas (x;y), e o método usado para calcular a distância é a euclidiana.  

> [!CAUTION] 
> É necessário arredondar os valores obtidos pela raiz quadrada

## Abordagem
A abordagem escolhida foi a heurísitca de, dado um nó inicial, escolher o nó com a menor distância até ele.  
Além disso, para evitar que demorasse muito, caso o número de elementos analisados aumentassem, decidi verificar apenas algumas vezes e sempre escolhendo um nó inicial aleatório.  

## Dependências
Esse código enm python usa apenas as bibliotecas nativas, assim não é necessário isntalar nenhuma dependência.  
Só é necessário baixar os seguintes arquivos desse repositório:
- [tsp.py](./tsp.py)
- [a280.tsp](./a280.tsp)
- [a280.opt.tour](./a280.opt.tour)

## Resultados obtidos
Após alguns testes observei que os melhores resultados obtidos ficaram em torno de 12% a cima do melhor valor.

## Discussão
Esse código possui algumas limitações, uma vez que pode encontrar um caminho que seja ótimo local, mas não o melhor caminho, dado que o algoritmo utilizado é guloso, sempre tenta minimizar a distância.  
Dessa forma, um dos pontos a se melhorar é a heurísitca utilizada, para permitir escolher um caminho maior para conseguir pegar caminhos mais curtos no futuro.
