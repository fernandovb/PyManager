# PyManager

Projeto de estudo para desenvolvimento de sistema ERP com uso de Firebird, SqlAlchemy, wxPython.

## Sobre o projeto

Sem grandes pretenções, este projeto visa o estudo da criação e uso de um sistema de gestão e controle, com uso de ferramentas OpenSource, buscando o conhecimento nas ferramentas de desenvolvimento e técnicas utilizadas para obtenção desses controles.

### Intenções do projeto

Sou formado em Ciências Contábeis e, por muitos anos, vejo a carência de ferramentas que possam, de uma forma mais completa, passar as informações necessárias ao negócio. Em geral as ferramentas são fragmentadas, sendo adquirido ferramentas separadas para controles financeiros, contábeis, estoques e fiscais, o que gera custos adicionais e dificulta a consolidação das informações as parte interessadas.
As ferramentas que oferecem soluções desta natureza, tem custos elevados, além de não integrarem uma solução realmente completa.
Reforço que sem grandes pretenções, a principal intenção deste projeto é o aprendizado desta fantástica ferramenta, o Python, além de aprofundar os estudos sobre programação.
Se, de alguma forma, este projeto puder ajudar, mesmo que de uma pequena maneira os usuários que o acessarem, já estarei além de minhas espectativas, já que sou uma criança neste universo gigantesco da programação.

### Módulos

Os módulos pretendidos neste projeto serão:

- SYS (Dados do Sistema): conterá os módulos de configuração e acesso do sistema, como cadastro de usuários, tela de login, controle de numerações e códigos etc.;
- SEB (System Environment Basics Data, ou Dados Básicos do Ambiente de Sistema): conterá os módulos de uso do sistema, possibilitando criação de ambientes que possibilitem o controle de forma independente para cada entidade. Podemos considerar o cadastro de empresas, unidades, atividades, ocupações, operações etc.;
- PRM (Gestão de Relacionamento de Pessoas): conterá os módulos de controle de relações de pessoas. Este módulo se baseia no conceito PRM (People Relationship Management, ou Gestão de Relacionamento de Pessoas), que visa incluir não somente os conceitos de CRM (Customer Relationship Management) e SRM (Supplier Relationship Management), mas uma nova gestão do relacionamento entre pessoas da entidade, visando prevenir conflitos de interesses, questões judiciais e trabalhistas, bem como integrar a cadeia de entregas;
- ACC (Accounting, ou Contabilidade): conterá o módulo de contabilidade, trazendo uma gestão baseada em fluxos contábeis, com utilização de lançamentos e relatórios contábeis, com utilização de informações complementares que irão possibilitar uma gestão do negócio com a visão contábil;
- FMI (Financial Management Information System): conterá o módulo financeiro, utilizando os recursos contábeis de registro, mas com informações complementares, além de recursos adicionais para facilitar a gestão financeira;
- CLC (Contract Life Cycle Management): conterá o módulo para gestão de contratos, que fornecerá informações sobre os contratos, como vigência, andamento do contrato, avisos de renovação, faturas ou parcelas geradas, análise pós finalização, recomendações. O módulo controlará tanto contratos de aquisição, como contratos de fornecimento;
- TAX (Management Taxes): conterá o módulo para gestão de tributos, que fornecerá informações sobre os impostos formas de tributação, legislação fiscal;
- MRP (Material Requirement Planning): conterá o módulo para controle de produtos, estoque e movimentações de materiais, bem como controles e registros de inventários.

Ainda haverá um móduto para a parte comercial, com controle de pedidos de compra e venda, mas que ainda não foi definido.

### Requisitos

Desenvolvido em Python 3.7 com uso dos módulos:

- wxPython;
- SqlAlchemy;

## Sobre o autor

Me chamo Fernando Vicente Batista. Sou formado em Ciências Contábeis desde 2011, tendo uma curta experiência com desenvolvimento com COBOL nos anos 90. Depois de muito tempo sem me envolver com programação, voltei, em 2005 a ter contato com a programação, mas desta vez com Delphi, onde tive os primeiros contatos com POO. Embora tenha gostado da linguagem e aprendido os fundamentos e conceitos, somente em 2018 voltei a pegar com mais vontade os estudos, mas agora com Python.

## Desenvolvimento

Devido a necessidade de estudo para obtenção de conhecimento com programação, principalmente em Python, o projeto está sendo desenvolvido apenas por mim.
Quem tiver sugestões sobre melhorias dos códigos, indicação de literaturas, poderá entrar em contato comigo através do e-mail fernandovicente.batista@hotmail.com.
