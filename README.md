<h1 align="center">📊 Análise de Desempenho de Lojas - Challenge Alura Store</h1> <p align="center"> Este projeto foi desenvolvido durante meus estudos no <strong>Programa ONE - Oracle Next Education</strong>, após concluir os cursos:<br> <ul> <li>Python para Data Science: primeiros passos;</li> <li>Python para Data Science: Trabalhando com funções, estruturas de dados e exceções.</li> </ul> </p>
<h2>💡 Objetivo</h2> 
<p>O objetivo deste projeto foi ajudar o <strong>Senhor João</strong> a decidir qual das suas quatro lojas vender, com base nos dados de desempenho de cada uma. Foram avaliados: faturamento total, produtos mais e menos vendidos, satisfação dos clientes e custo médio de frete.</p>
<p> Obs: Já que a proposta do Challenge não deixa explicito, foi considerado que o frete é cobrado do cliente, não sendo deduzido do faturamento das lojas.</p>

<h2>🛠️ Ferramentas utilizadas</h2> <ul> <li>Python</li> <li>Pandas</li> <li>Matplotlib</li> <li>Jupyter Notebook / VS Code </li> </ul>

<h1>📈 Análises Realizadas</h1> 
<h2>💵 Faturamento Total por Loja</h2> 
<p align="center"><em><img src="https://github.com/heloisa-azevedo/Challenge-Alura-Store/blob/main/img/Faturamento_total_por_loja.jpg" alt="Teste"></em></p> <p> <strong>Análise:</strong> <br> A Loja 1 apresentou o maior faturamento (R$ 1.534.509,12). Já a Loja 4 ficou em último lugar, com o valor de R$ 1.384.497,58 — indicando menor retorno financeiro. </p>

<h2>📊 Participação das Categorias nas Vendas</h2> 
<p align="center"><em><img src="https://github.com/heloisa-azevedo/Challenge-Alura-Store/blob/main/img/Participacao_vendas_por_categoria.jpg" alt="Teste"></em></p> <p> <strong>Análise:</strong> <br> As quatro lojas mostraram que os produtos da categoria <strong>móveis</strong> são os mais vendidos, enquanto <strong>instrumentos musicais</strong> e <strong>utilidades domésticas</strong> aparecem como as categorias menos populares. A Loja 4, apesar de boa variedade, não converteu tanto em vendas. </p>

<h2>⭐ Média das Avaliações dos Clientes</h2> 
<p> <strong>Análise:</strong> <br> A Loja 3 se destacou com a avaliação mais alta (4.05), enquanto a Loja 4 ficou abaixo das demais, com uma média de 3.99. </p>

<h2>🚚 Frete Médio por Loja</h2> 
<p> <strong>Análise:</strong> <br> A Loja 4 tem o frete médio mais baixo (R$ 31,28). Mesmo assim, isso não se refletiu em melhor faturamento nem em melhores avaliações. </p>

<h2>🔥 Dispersão: Avaliação x Frete</h2> 
<p align="center"><em><img src="https://github.com/heloisa-azevedo/Challenge-Alura-Store/blob/main/img/Comparacao_avaliacao_frete.jpg" alt="Teste"></em></p> <p> <strong>Análise:</strong> <br> O gráfico mostrou que frete mais barato não garante melhores avaliações, tendo em vista que a quantidade de avaliações altas (5.0) acontecem de forma semelhante em todas as regiões, indenpendende se o frete é mais barato ou mais caro  </p>

<h2>🏆 Conclusão</h2> 
<p>Resumo final dos dados:</p> 
<table> <tr> <th>Loja</th> <th>Faturamento Total</th> <th>Produto + Vendido</th> <th>Produto - Vendido</th> <th>Avaliação Média</th> <th>Frete Médio</th> </tr> <tr> <td>Loja 1</td> <td>R$ 1.534.509,12</td> <td>Móveis (465)</td> <td>Utilidades Domésticas (171)</td> <td>3.98</td> <td>R$ 34,69</td> </tr> <tr> <td>Loja 2</td> <td>R$ 1.488.459,06</td> <td>Móveis (442)</td> <td>Utilidades Domésticas (181)</td> <td>4.04</td> <td>R$ 33,62</td> </tr> <tr> <td>Loja 3</td> <td>R$ 1.464.025,03</td> <td>Móveis (499)</td> <td>Instrumentos Musicais (177)</td> <td>4.05</td> <td>R$ 33,07</td> </tr> <tr> <td>Loja 4</td> <td>R$ 1.384.497,58</td> <td>Móveis (480)</td> <td>Instrumentos Musicais (170)</td> <td>3.99</td> <td>R$ 31,28</td> </tr> </table> <p><strong>Decisão:</strong><br> A partir dessa análise, a recomendação é que o Senhor João venda a <strong>Loja 4</strong>, pois ela teve o pior desempenho geral: menor faturamento, avaliações medianas e, mesmo com frete mais barato, não conseguiu se destacar nas vendas. </p>
