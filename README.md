
🧾 Automação de Leitura de Pedidos com Visão de IA
Este projeto automatiza a leitura de pedidos escritos à mão a partir de imagens, utilizando um modelo de visão de inteligência artificial. As imagens são analisadas, os produtos e suas quantidades são identificados e organizados automaticamente em um arquivo CSV, pronto para ser utilizado em qualquer fluxo posterior.

🚀 Objetivo

O objetivo é eliminar o trabalho manual de interpretar pedidos em papel e digitar item por item em um sistema.

Em vez de olhar cada pedido, ler os produtos, contar quantidades e digitar tudo em um computador, você apenas coloca as imagens em uma pasta, executa o script e recebe um arquivo estruturado com:

o código de cada produto;

a quantidade associada;

a informação de qual imagem aquele item veio.

Isso reduz erros, acelera o processo e padroniza a forma como os dados são capturados.

🧠 Tecnologias utilizadas

O projeto é construído em cima de:

Python 3 – linguagem principal da automação;

API de IA com visão – para interpretar o conteúdo das imagens (códigos e quantidades);

Leitura de variáveis de ambiente – para manter a chave de API de forma segura em um arquivo de configuração;

Manipulação de arquivos CSV – para gerar um arquivo final com todos os itens detectados;

Bibliotecas nativas do Python – para percorrer pastas, trabalhar com caminhos de arquivos, codificação de imagens e escrita de dados.

⚙️ Como funciona

De forma geral, o fluxo deste projeto é:

Carregamento da configuração
O script lê as configurações necessárias (como a chave de API) a partir de um arquivo de ambiente, garantindo que dados sensíveis não fiquem expostos diretamente no código.

Leitura das imagens em uma pasta específica
Todas as imagens de pedidos são colocadas em uma pasta definida previamente. O script percorre essa pasta e identifica automaticamente os arquivos de imagem compatíveis (por exemplo, formatos comuns de foto).

Envio das imagens para o modelo de visão
Cada imagem é convertida para um formato adequado e enviada para um modelo de IA capaz de entender conteúdo visual.
Junto com a imagem é enviado um texto explicando o contexto: que se trata de um pedido, com códigos de produtos escritos à mão e quantidades associadas a esses códigos.

📂 Estrutura esperada dos arquivos

Uma pasta destinada às imagens dos pedidos, onde você coloca as fotos ou digitalizações dos documentos.

Um arquivo CSV de saída, gerado automaticamente ao final da execução, reunindo todos os itens encontrados em todas as imagens.

Cada linha do CSV corresponde a um item identificado em uma das imagens de entrada, incluindo a quantidade e a indicação de qual arquivo de imagem originou aquele registro
Interpretação dos pedidos pela IA
A inteligência artificial analisa a imagem e retorna o resultado em um formato tabular simples, com linhas representando itens do pedido, contendo:

um identificador do produto (código);

a quantidade solicitada.

O projeto orienta o modelo a responder de forma estruturada, para facilitar a conversão direta desses dados para CSV.

Tratamento e limpeza dos dados retornados
O texto retornado pela IA é processado:

cada linha é separada em código e quantidade;

são feitas pequenas correções e limpezas (remoção de espaços indesejados, padronização de letras, validação de quantidade numérica, etc.);

o nome do arquivo de origem é associado a cada item, permitindo rastrear de qual imagem veio cada linha.

Geração do arquivo CSV final
Após processar todas as imagens, o script reúne todos os itens em uma única lista e grava em um arquivo CSV.
Esse arquivo contém colunas genéricas como:

código do produto,

quantidade,

imagem de origem.

Assim, qualquer outro sistema ou script pode ler esses dados e dar continuidade ao processo, por exemplo: preenchendo um sistema desktop, gerando etiquetas, alimentando um ERP, etc.

🧰 Requisitos

Para rodar este projeto, é necessário:

Ter Python 3 instalado.

Criar e configurar um arquivo de ambiente contendo a chave de acesso à API de IA.

Instalar as dependências responsáveis por:

integrar com o serviço de IA;

carregar variáveis de ambiente;

manipular arquivos CSV;

percorrer diretórios e manipular arquivos e imagens.

▶️ Como usar na prática

Coloque as imagens dos pedidos na pasta indicada pela documentação do projeto.

Garanta que a chave da API esteja corretamente configurada no arquivo de ambiente.

Execute o script principal do projeto com o Python.

Ao final, abra o arquivo CSV gerado e confira os códigos e quantidades extraídos automaticamente.


📝 Toda a lógica foi pensada para ser um “primeiro estágio” da automação: transformar imagens de pedidos em dados estruturados, que podem ser consumidos por qualquer outro sistema ou processo que você queira implementar depois.
