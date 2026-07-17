# Sobre o projeto

Este projeto consiste na construção de um pipeline completo de análise de dados utilizando a base pública de e-commerce da Olist. O objetivo foi desenvolver uma solução de ponta a ponta, contemplando as etapas de extração, tratamento, validação, modelagem e análise dos dados, culminando na criação de um dashboard interativo para apoio à tomada de decisão.

Durante o desenvolvimento foram utilizadas tecnologias amplamente empregadas em projetos de dados, incluindo Python, SQL, BigQuery, Looker Studio e Git/GitHub. O projeto foi estruturado seguindo boas práticas de organização, documentação e versionamento, simulando um cenário próximo ao encontrado em ambientes corporativos.

# Objetivos

O desenvolvimento deste projeto teve como principais objetivos:

* Construir um pipeline completo de análise de dados utilizando um conjunto de dados reais de e-commerce.
* Aplicar técnicas de limpeza, transformação e validação dos dados para garantir sua qualidade.
* Desenvolver consultas SQL voltadas para indicadores de negócio e análises exploratórias.
* Utilizar o BigQuery como plataforma de armazenamento e consulta dos dados.
* Criar um dashboard interativo no Looker Studio para visualização dos principais indicadores.
* Aplicar boas práticas de organização de projetos, documentação e versionamento com Git e GitHub.


# Arquitetura da solução

O projeto foi desenvolvido seguindo um fluxo de processamento de dados de ponta a ponta, desde a preparação dos dados até a disponibilização de indicadores para análise.

**Fluxo da solução:**

Dados Olist
→ Python (ETL e Validação)
→ BigQuery (Armazenamento e Consultas SQL)
→ Looker Studio (Dashboard e Visualização)

Esse fluxo representa uma arquitetura simples, porém amplamente utilizada em projetos de Analytics e Business Intelligence, permitindo a integração entre processamento, armazenamento, análise e visualização dos dados.


# Tecnologias utilizadas

As principais tecnologias e ferramentas utilizadas neste projeto foram:

* **Python** — Extração, tratamento, validação e preparação dos dados.
* **Pandas** — Manipulação e transformação dos conjuntos de dados.
* **SQL** — Consultas analíticas e geração de indicadores.
* **Google BigQuery** — Armazenamento e processamento analítico dos dados.
* **Looker Studio** — Desenvolvimento do dashboard interativo.
* **Git** — Controle de versão.
* **GitHub** — Hospedagem e versionamento do projeto.
* **Visual Studio Code** — Ambiente de desenvolvimento.


# Estrutura do repositório

O projeto está organizado de forma modular para facilitar a manutenção, a navegação e a compreensão do fluxo de trabalho.

```text
├── data/
│   ├── processed/
│   └── analytics/
├── scripts/
├── sql/
├── dashboard/
├── images/
├── README.md
```

**Descrição das pastas:**

* **data/** — Dados processados e arquivos utilizados nas análises.
* **scripts/** — Scripts Python responsáveis pelo pipeline ETL e validações.
* **sql/** — Consultas SQL utilizadas para geração dos indicadores.
* **dashboard/** — Recursos relacionados ao dashboard desenvolvido no Looker Studio.
* **images/** — Imagens utilizadas na documentação, como capturas de tela e diagramas.


# Principais resultados

Ao final do projeto, foram entregues os seguintes resultados:

* Pipeline ETL desenvolvido em Python para processamento e validação dos dados.
* Base analítica consolidada e disponibilizada no Google BigQuery.
* Consultas SQL para análise de indicadores de negócio, incluindo receita, ticket médio, categorias mais vendidas e desempenho por estado.
* Dashboard interativo no Looker Studio para acompanhamento dos principais indicadores de e-commerce.
* Repositório organizado com documentação, versionamento em Git e estrutura modular, facilitando a manutenção e a reprodução do projeto.

# Acesse o projeto

Os principais resultados deste projeto podem ser explorados por meio dos links abaixo:

* **Dashboard interativo (Looker Studio):** https://datastudio.google.com/s/lpReVwyVaoQ
* **Repositório no GitHub:** https://github.com/JulioPeniche/Marketing_Analytics_00


