from agno.knowledge.knowledge import Knowledge
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.knowledge.embedder.openai import OpenAIEmbedder
from agno.db.sqlite import SqliteDb
from crawler import Crawler
from rich import print

knowledge = Knowledge(
    name='Base de Conhecimentos de Cinema',
    vector_db=LanceDb(
        uri="lancedb/knowledge1",
        table_name="wikipedia",
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    ),
    contents_db=SqliteDb("kbase.visie.sqlite"),
)


if __name__ == "__main__":
        knowledge.insert(
            name='O Agente Secreto',
            text_content='''
# O Agente Secreto

O Agente Secreto é um filme neo-noir brasileiro com coprodução francesa, neerlandesa e alemã de drama, suspense e thriller político de 2025, escrito e dirigido por Kleber Mendonça Filho. Produzido pela CinemaScópio (Brasil),[4][5] o filme teve sua estreia mundial no Festival de Cannes em 18 de maio de 2025,[6] onde competiu pela Palma de Ouro.[7] Na ocasião, venceu os prêmios de Interpretação Masculina para Wagner Moura[8] e Melhor Diretor para Kleber Mendonça Filho,[9] além do Prêmio FIPRESCI da competição oficial[10] e o Prix des Cinémas d’Art et Essai, concedido pela Associação Francesa de Cinemas de Arte (AFCAE).[11]

O filme é estrelado por Wagner Moura, Tânia Maria, Maria Fernanda Cândido, Gabriel Leone, Alice Carvalho, Udo Kier e Thomás Aquino. O longa-metragem estreou nos cinemas brasileiros em 6 de novembro de 2025, com distribuição da Vitrine Filmes.[12]

No Globo de Ouro de 2026, foi indicado em três categorias, Melhor Filme em Drama, Melhor Filme em Língua Não Inglesa e Melhor Ator em Drama, vencendo Melhor Filme em Língua Não Inglesa e Melhor Ator. Na 98.ª cerimônia do Oscar, foi nomeado a Melhor Filme, Melhor Filme Internacional, Melhor Ator e Melhor Elenco.[13][14]

Enredo
Em 1977, durante a ditadura militar brasileira, o ex-professor e viúvo Armando Solimões desembarca em Recife durante as férias de Carnaval, onde seu filho Fernando mora com os avós maternos após a morte da esposa de Armando, Fátima Nascimento. Ele é acolhido num albergue por Dona Sebastiana, uma ex-militante anarcocomunista, junto com outros dissidentes políticos, incluindo Claudia, Haroldo, e Thereza Vitória e António, um casal de refugiados da Guerra Civil Angolana. Enquanto isso, o delegado corrupto da Polícia Civil Euclides e os seus filhos Sérgio e Arlindo são chamados durante o feriado para investigar uma perna humana encontrada dentro de um tubarão capturado.

A rede de dissidentes de Armando o situa num instituto de identificação da Polícia Civil sob o pseudônimo "Marcelo", onde recebe boas-vindas e proteção de Euclides. Armando fica visivelmente irritado com a arrogância do delegado, que inclui importunar Hans—um alfaiate alemão que Euclides presume ser um fugitivo nazista, mas na verdade é um judeu sobrevivente do Holocausto. O novo emprego de Armando também lhe propõe a oportunidade de procurar arquivos sobre a sua falecida mãe, "Índia", de quem tem poucas lembranças. Em São Paulo, os assassinos de aluguel Bobbi e Augusto são contratados por Henrique Ghirotti, um executivo da Eletrobras e ex-ministro do governo militar, para matar Armando por uma disputa política e pessoal.

Sérgio e Arlindo desovam a perna engolida pelo tubarão no Rio Capibaribe. Os jornais locais noticiam que a perna ressuscitou e atacou casais gays num parque público, supostamente para acobertar a corrupção política e violência durante a semana de carnaval.

No Cinema São Luiz, onde seu sogro Seu Alexandre trabalha como projecionista, Armando encontra com Elza, líder de um movimento de resistência política no nordeste brasileiro, para gravar um testemunho sobre as atividades de Ghirotti, e relembra um jantar ao lado de Fátima em que, após receber comentários de mau gosto sobre sua classe socioeconômica e supostas simpatias comunistas, brigou com Ghirotti e seu filho. Elza informa Armando que há uma recompensa sobre a sua vida e o instrui a fugir do país com um passaporte falso. Augusto e Bobbi contratam um pistoleiro pobre, Vilmar, para encontrar Armando. Antecipando sua fuga, Armando dá adeus a Dona Sebastiana e os outros refugiados.

Na manhã seguinte, Bobbi descobre a localização de Armando ao seguir Seu Alexandre. Vilmar encontra Armando no instituto de identificação, mas não consegue matá-lo. Na perseguição, Vilmar mata dois policiais incluindo Arlindo e é baleado na perna, deixando um rastro de sangue. Bobbi segue o rastro até que é morto por Vilmar numa barbearia.

No presente, a estudante de história Flávia pesquisa a rede de resistência de Elza através de gravações de áudio pela mesma e acervos de jornais, até que descobre que Armando foi assassinado e enquadrado como um professor corrupto. Flávia viaja para Recife para entrevistar Fernando, agora um médico de meia-idade, após Flávia doar sangue no hospital onde trabalha. Discutindo o passado político, histórico familiar, e assassinato de Armando, Fernando diz que não tem lembranças do próprio pai, mas lembra de ter assistido Tubarão com o avô num cinema que se tornou o hospital onde ele trabalha.

Elenco
Wagner Moura como Armando / Marcelo / Fernando (presente)
Carlos Francisco como Seu Alexandre
Tânia Maria como Dona Sebastiana
Enzo Nunes como Fernando
Robério Diógenes como Euclides
Maria Fernanda Cândido como Elza
Gabriel Leone como Bobbi
Roney Villela como Augusto
Hermila Guedes como Claudia
Isabél Zuaa como Tereza Vitória
Licínio Januário como Antonio
Alice Carvalho como Fátima
Laura Lufési como Flavia[15]
Thomás Aquino como Arlindo
Igor de Araújo como Sergio
Udo Kier como Hans
João Vitor Silva como Haroldo
Kaiony Venâncio como Vilmar
Suzy Lopes como Carmem
Buda Lira como Anízio
Beto Quirino como Guarda Desidério
Produção
Desenvolvimento e Roteiro
O Agente Secreto nasceu do desejo de Kleber Mendonça Filho de realizar um "exercício histórico", ambientando a trama em 1977, durante o governo de Ernesto Geisel, um período da ditadura militar brasileira que o diretor considera menos explorado no cinema em comparação com os anos de chumbo mais intensos.[16] O roteiro foi escrito por Mendonça Filho ao longo de três anos,[17] num processo descrito por ele como difícil, com longos períodos de improdutividade até que a história "passa a se escrever sozinha".[16] O roteiro finalizado continha 167 páginas.[18]

A inspiração inicial para um elemento da trama veio de uma notícia de um jornal australiano sobre um tubarão encontrado com uma perna humana em seu ventre, que se transformou em uma homenagem a filmes de exploração dentro da narrativa.[16][19] Outra sequência, envolvendo uma bomba de gasolina, originou-se de um curta-metragem que o diretor nunca chegou a filmar.[16] Mendonça Filho afirmou que busca com seus filmes "suscitar ideias" em vez de "levar uma mensagem", e que desejava fazer um filme sobre os anos 70 com "detalhes do coração", explorando como indivíduos navegam e resistem a um sistema opressor.[16][20] O abrigo de "refugiados" no filme simboliza um "bunker de afeição".[16]

O processo de seleção do elenco incluiu a jovem atriz mineira Laura Lufési, que interpreta Flavia, após um processo de testes.[15] O filme marca a segunda colaboração de Mendonça Filho com Udo Kier, após Bacurau.

Financiamento
O Agente Secreto é uma coprodução internacional envolvendo Brasil, França, Holanda e Alemanha. As produtoras principais são a brasileira CinemaScópio Produções, a francesa MK2 Films (também creditada como MK Productions), a holandesa Lemming Film e a alemã One Two Films.[4][5] Arte France Cinéma (França), Black Rabbit Media, Itapoan e a distribuidora brasileira Vitrine Filmes também participam como coprodutoras.

O filme recebeu apoio financeiro de diversas instituições:

Brasil: Fundo Setorial do Audiovisual (FSA), gerido pela Ancine, através da Lei do Audiovisual.[21][22]
França: Centre national du cinéma et de l'image animée (CNC), através do programa "Aide aux cinémas du monde avant réalisation" (Ajuda aos cinemas do mundo antes da realização) e "Aide à l'édition en vidéo physique" (Ajuda para edição em vídeo físico).[23]
Holanda: Netherlands Film Fund, através do Film Production Incentive em 2024.[5] Leontine Petit da Lemming Film e Fred Burle são coprodutores associados à Holanda. Dora Amorim atuou como produtora executiva. Todos possuem ligações com programas de desenvolvimento audiovisual europeus como EAVE (European Audiovisual Entrepreneurs) e PUENTES.[5]
Alemanha: Recebeu € 150 000 do Medienboard Berlin-Brandenburg e € 60 000 do FFA (German Federal Film Fund).[4]
Filmagens
As filmagens de O Agente Secreto ocorreram ao longo de dez semanas, entre junho e agosto de 2024,[24] com locações nas cidades de Recife, Pernambuco, e São Paulo.[25]

Mendonça Filho buscou recriar suas memórias afetivas de Recife em 1977, focando em detalhes como decoração, objetos, carros, jornais e telegramas para construir uma "maquiagem bem-feita do passado" que ainda ressoasse com o presente.[26][27] A abordagem não visava uma reconstituição exata de incidentes da ditadura, mas sim criar uma "atmosfera tensa, densa e cheia de texturas" e um "clima sufocante" que dialogasse com questões contemporâneas.[26] Locais icônicos de Recife, como a Praça do Sebo e o Cinema São Luiz, são centrais na narrativa, refletindo o interesse contínuo do diretor por cinemas como espaços de memória e vivência comunal, tema já explorado em seu documentário Retratos Fantasmas.[28][17]

A direção de fotografia de Evgenia Alexandrova, a direção de arte de Thales Junqueira e o figurino de Rita Azevedo foram cruciais para estabelecer a estética "vintage" e a atmosfera do filme.[26][19] Críticos destacaram o uso de lentes anamórficas e dioptrias divididas por Mendonça Filho, elementos estilísticos que contribuem para a linguagem visual do filme.[17]

Pós-produção
A montagem do filme foi realizada por Matheus Farias e Eduardo Serrano, que trabalharam para dar forma à narrativa complexa e em camadas, com duração final de 158 minutos.[17] A trilha sonora original é de Mateus Alves e Tomaz Alves Souza, que já colaboraram com Mendonça Filho em trabalhos anteriores. Críticas mencionam o uso de clássicos brasileiros na trilha sonora, contribuindo para a imersão na época.[17]

Lançamento
O Agente Secreto teve sua estreia mundial em 18 de maio de 2025, como parte da Seleção Oficial do 78º Festival de Cannes, onde competiu pela Palma de Ouro.[29][20]

O filme estreou em 6 de novembro de 2025 nos cinemas brasileiros com distribuição da Vitrine Filmes,[30] sendo precedido por duas semanas de pré-estreias.[31] Na França, o lançamento está previsto para janeiro de 2026 pela Ad Vitam Distribution.[20] Nos Estados Unidos e Canadá, o filme terá distribuição da Neon.[32] No Reino Unido, Irlanda, Índia e no restante da América Latina (exceto Brasil), o longa possui distribuição da MUBI.[33] A distribuição na Alemanha será feita pela Port au Prince Pictures.[4] Em Portugal, o filme possui distribuição da Nitrato Filmes e estreou em 6 de novembro de 2025.[34][35]

Em dezembro de 2025, com seis semanas em cartaz nos cinemas, o filme alcançou a marca de 1 milhão de espectadores, tornando-se o primeiro filme brasileiro produzido fora do eixo Sul-Sudeste a alcançar este número de ingressos vendidos no país.[36]

Recepção
Crítica especializada
O Agente Secreto foi aclamado pela crítica especializada após sua estreia em Cannes. No agregador de críticas Rotten Tomatoes, o filme possui uma taxa de aprovação de 99% com base em 88 avaliações, com uma nota média de 8.9/10, recebendo um selo "Certificado Fresh". O consenso dos críticos do site diz: "um thriller político tematicamente rico e visualmente impressionante, O Agente Secreto mistura a estilização de grindhouse com um comentário social afiado para tecer uma história vividamente perigosa, mas sombriamente humana".[37] No Metacritic, que atribui uma pontuação normalizada de 0 a 100, o filme obteve uma média de 91, baseada em 25 críticas, indicando "aclamação universal". No mesmo site, o filme recebeu o selo "Must-See" ("Imperdível").[38][39][40]

Carlos Aguilar, do The Playlist, classificou o filme como: "Uma obra-prima imponente, imersa em história e com uma adoração palpável pelo cinema", elogiando a produção de Thales Junqueira e a forma como o filme explora a memória e a verdade.[19] Peter Bradshaw, do britânico The Guardian, deu ao filme 5 de 5 estrelas, descrevendo-o como um "brilhante drama brasileiro sobre um acadêmico em fuga nos anos 1970".[41] A crítica da BBC Culture, baseada em impressões da Sight and Sound, chamou o filme de um "thriller político estiloso e vibrante" que "compensa em excitação o que lhe falta em sutileza", destacando a atuação de Wagner Moura e a atmosfera criada por Mendonça Filho.[42]

Mariana Canhisares, do Omelete, considerou O Agente Secreto um "fantástico thriller" que utiliza o gênero de espionagem para discutir o apagamento de informações e identidades durante a ditadura, elogiando a direção de Kleber Mendonça Filho e as atuações do elenco, especialmente Wagner Moura.[28] A revista francesa Les Cahiers du Cinéma, através de resenhas publicadas por outros veículos que a citam, destacou o filme como um "thriller com toques fantásticos evocando a ditadura militar"[43] e um "belo e amplo afresco política", embora um crítico a tenha achado complicado em alguns momentos devido a desvios na trama.[44]

As críticas em geral elogiaram a direção de arte, o figurino, a fotografia e a trilha sonora por sua contribuição na criação da atmosfera e na recriação da época. Alguns críticos mencionaram a longa duração (158 minutos) como um ponto de atenção, mas geralmente justificável pela complexidade da trama e profundidade temática.[17]

O filme foi escolhido pela revista britânica The Economist para integrar sua lista de melhores filmes de 2025, ao lado de Ainda Estou Aqui.[45] Foi eleito pela The Hollywood Reporter o melhor filme de 2025.[46]

Repercussão política e cultural
A premiação do filme em Cannes gerou forte repercussão no Brasil. O presidente Luiz Inácio Lula da Silva parabenizou a equipe em suas redes sociais, afirmando que os "prêmios em Cannes mostram que cinema de nosso País não deve nada para ninguém".[47] O sucesso do filme também foi visto como um impulsionador do cinema brasileiro no cenário internacional e fortaleceu as especulações sobre uma possível indicação ao Oscar de Melhor Filme Internacional em 2026.[21][48]


Anúncio de sessões extras de O Agente Secreto no Cine Santa Teresa, dias após a premiação do Globo de Ouro 2026.
Submissão ao Oscar
Embora Mendonça Filho tenha sido preterido duas vezes pela comissão brasileira de inscrição para o Oscar de Melhor Longa-Metragem Internacional,[49] por duas produções aclamadas pela crítica: Aquarius em 2016[50] e Bacurau em 2019, esperava-se que O Agente Secreto fosse a escolha segura do país após sua exibição bem-sucedida no Festival de Cannes 2025 e a forte campanha contínua na temporada de premiações pela distribuidora Neon.[51][52]

Em agosto, o filme foi pré-selecionado juntamente com outros cinco longas-metragens, com a decisão final do país prevista para ser anunciada em 15 de setembro. Pouco depois, surgiram relatos sugerindo uma possível rejeição em favor de Manas, que foi apoiado por 70 empresas de alto perfil por seu suposto "assunto urgente no Brasil". O movimento criou um alvoroço público devido à percepção de abuso político e pessoal do processo de inscrição no Oscar, em vez do mérito e da lógica comercial.[53][54][55][56]

Após a indignação online, que incluiu um vídeo de quatro minutos de Fernanda Torres apoiando sua seleção, O Agente Secreto foi confirmado pela Academia Brasileira de Cinema como a submissão oficial do país em 15 de setembro.[57][58]

Em 22 de janeiro, o filme foi confirmado na lista final dos indicados ao prêmio de Melhor Longa-Metragem Internacional. O Agente Secreto também foi indicado para concorrer nas categorias de Melhor Filme, Melhor Elenco e Melhor ator com Wagner Moura.[59]

Prêmios e indicações
 Ver artigo principal: Lista de prêmios e indicações recebidos por O Agente Secreto
O Agente Secreto venceu duas das três categorias em que concorria, Melhor Filme em Língua Não Inglesa[60] e Melhor Ator em Drama, e conquistou dois feitos históricos: foi o primeiro filme brasileiro a vencer dois prêmios Globo de Ouro em uma única noite,[61] e Wagner Moura tornou-se o primeiro ator brasileiro a ganhar o troféu de Melhor Ator em Filme Dramático,[62][63] além de ter se tornando o primeiro filme brasileiro da história a ser indicado a Melhor Filme em Drama.[64][65]
            ''',
        )
