import streamlit as st
from streamlit_option_menu import option_menu
import time
import streamlit.components.v1 as components
import pandas as pd
from streamlit_extras.badges import badge 
from streamlit_extras.mention import mention 


licitacoes = pd.read_csv("/Users/pedroafmelo/Documents/projetos/licitacoes/data/licitacoes.csv")
tradutor = pd.read_csv("../data/tcepb_tradutor_ug.csv", encoding = "latin", sep = ";", names = ["cod_mundv", "idmun_tce"], skiprows= 1)
mun = pd.read_csv("../data/mun.csv", encoding = "latin")
dados_tratados = pd.read_csv("/Users/pedroafmelo/Documents/projetos/licitacoes/data/df_tratado.csv", nrows = 20)
df_shows = pd.read_csv("/Users/pedroafmelo/Documents/projetos/licitacoes/data/df_shows.csv")

licitacoes["ano_homologacao_licitacao"] = licitacoes["ano_homologacao_licitacao"].astype(str)


st.set_page_config(page_title = "LICITAÇÕES",
                    page_icon = "📈", 
                    layout = "wide" )
st.title("Licitações")
st.markdown("""<h10 style = 'text-align : left; color: grey;'
            >Professor Dr. Aléssio Tony. <br> Técnicas de Pesquisa e Análise de Dados</h10>""", unsafe_allow_html= True)
st.markdown("""<hr style="height:2px;border:none;color:#006be8;background-color:#006be8;" /> """, unsafe_allow_html=True)
def main():
    menu()

def badges_one():
    badge("pypi", "pandas")
    badge("pypi", "streamlit")
    badge("pypi", "time")
def badges_two():
    badge("pypi", "matplotlib")
    badge("pypi", "seaborn")

def menu():
    selected = option_menu(
        menu_title= None,
        options = ["Apresentação", "Dashboard", "Dados"],
        icons = ["house", "bar-chart", "database"],
        default_index= 0,
        orientation= "horizontal"

    )
    if selected == "Apresentação":
        c1, c2, c3 = st.columns(3)
        st.write("#")
        c1.markdown("<h2 style='text-align: center; color: white;'>Grupo</h2>", unsafe_allow_html=True)
        #1.markdown("""<hr style="height:0.5px;border:none;color:#006be8;background-color:#006be8;" /> """, unsafe_allow_html=True)
        st.write("#")
        with c1.expander("Pedro Melo"):
            st.write("Matrícula: 20220062545")
            st.write("2º Período")
            st.image("/Users/pedroafmelo/Documents/ufpb/streamlit_ufpb/img/logo.png", width = 100)
            mention(
                label = "Github",
                url = "https://github.com/pedroafmelo"
            )

        with c1.expander("Pedro Henrique"):
            st.write("Matrícula: 20220092900")
            st.write("2º Período")
            st.image("/Users/pedroafmelo/Documents/ufpb/streamlit_ufpb/img/logo.png", width = 100)
            mention(
                label = "Github",
                url = "https://github.com/ricktherunner"
            )

        with c1.expander("Lucas Rabay"):
            st.write("Matrícula: 202200075334")
            st.write("2º Período")
            st.image("/Users/pedroafmelo/Documents/ufpb/streamlit_ufpb/img/logo.png", width = 100)
            mention(
                label = "Github",
                url = "https://github.com/lucasrabay"
            )

        st.write("#")

        with c2.container():
            st.markdown("<h2 style='text-align: center; color: white;'>Tema</h2>", unsafe_allow_html= True)
            #st.markdown("""<hr style="height:0.5px;border:none;color:#006be8;background-color:#006be8;" /> """, unsafe_allow_html=True)
            st.write("""
                     O tema escolhido foi o da análise de licitações realizadas para eventos esportivos, 
                     com o intuito de encontrar possíveis inconsistências nos referidos processos licitatórios.
                     Com este tema em mente, fizemos uma seleção dos dados que possuíam algumas palavras-chave
                     relacionadas a eventos musicais na coluna 'objeto_licitado' dos dados disponíveis."""
                     )

        with c3.container():
            coluna1, coluna2, coluna3 = c3.columns(3)
            st.markdown("<h2 style='text-align: center; color: white;'>Dados</h2>", unsafe_allow_html= True)
            #st.markdown("""<hr style="height:0.5px;border:none;color:#006be8;background-color:#006be8;" /> """, unsafe_allow_html=True)
            st.write("""
                 Os principais dados utilizados no presente trabalho foram os Dados Abertos do Sagres, do Tribunal de Contas do Estado da Paraíba."""
                 )
            coluna1.write(" ")
            coluna2.image("/Users/pedroafmelo/Documents/projetos/licitacoes/imagem/image.png", width = 100)
            coluna3.write(" ")
        st.markdown("<h5 style ='text-align: center; color: grey;' >João Pessoa, PB</h5>", unsafe_allow_html= True)
        st.markdown("<h5 style ='text-align: center; color: grey;' >10/11/2023</h5>", unsafe_allow_html= True)


        
    elif selected == "Dashboard":
        c1, c2 = st.columns(2)
        with st.spinner("Carregando dados..."):
            dashboard()

    elif selected == "Dados":
        st.markdown("<h2 style = 'text-align: center; color: white;'>Dados utilizados no trabalho</h2>", unsafe_allow_html= True)
        st.write("#")
        
        cont = st.container()

        c1, c2, c3 = st.columns([1, 2, 2])

    
        c1.markdown("<h4 style = 'text-align: left; color: grey;'>Tradutor de Municípios</h4>", unsafe_allow_html= True)
        c1.dataframe(tradutor)

        c2.markdown("<h4 style = 'text-align: center; color: grey;'>Municípios Paraibanos</h4>", unsafe_allow_html= True)
        c2.write("#")
        c2.dataframe(mun)

        c3.markdown("<h4 style = 'text-align: center; color: grey;'>Populações</h4>", unsafe_allow_html= True)
        c3.write("#")
        c3.write("""O botão abaixo irá le direcionar para o uma área do site do IBGE, 
                 no qual estão disponíveis os dados das populações de cada município do Brasil.""")

        co1, co2, co3 = c3.columns([2,2,1])
        co1.write(" ")
        co2.link_button("IBGE", "https://www.ibge.gov.br/estatisticas/sociais/populacao/9103-estimativas-de-populacao.html?edicao=17283&t=downloads")
        co3.write(" ")
        c3.write("#")
        c3.markdown("<h4 style = 'text-align: center; color: grey;'>Pacotes Utilizados</h4>", unsafe_allow_html= True)
        c3.write("#")
        col1, col2 = c3.columns(2)
        with col1:
            badges_one()
        with col2:
            badges_two()


        cont.markdown("<h4 style = 'text-align: center; color: grey;'>Licitações</h4>", unsafe_allow_html= True)
        cont.write("""Os dados receberam tratamento e apenas licitações com 
                  objetos relacionados a shows estão na base tratada.
                  É importante ressaltar que só há dados de população até 2021 nos dados encontrados, então,
                  nas análises que utilizamos população, só utilizamos os dados até 2021.""")
        cont.write("#")
        cont.dataframe(dados_tratados)
        
        

def dashboard():

    c1, c2, c3 = st.columns([2, 0.5, 2])
    
    df_shows = pd.read_csv("../data/df_shows.csv")

    agrupamento_geral_micro = pd.read_csv("/Users/pedroafmelo/Documents/projetos/licitacoes/data/agrupamento_micro_geral.csv")
    agrupamento_geral_cidade = pd.read_csv("/Users/pedroafmelo/Documents/projetos/licitacoes/data/agrupamento_cidade_geral.csv")
    agrupamento_geral_ano = pd.read_csv("/Users/pedroafmelo/Documents/projetos/licitacoes/data/agrupamento_ano_geral.csv")
    agrupamento_cidade = pd.read_csv("/Users/pedroafmelo/Documents/projetos/licitacoes/data/agrupamento_cidade_shows.csv")
    agrupamento_ano = pd.read_csv("/Users/pedroafmelo/Documents/projetos/licitacoes/data/agrupamento_ano_shows.csv")
    agrupamento_micro = pd.read_csv("/Users/pedroafmelo/Documents/projetos/licitacoes/data/agrupamento_micro_shows.csv")
    c1.write("#")
    c2.write("#")
    c3.write("#")

    # Tabela com cidades com maiores valores licitados (geral)
    if c1.toggle("Microrregiões"):
        c1.markdown("<h4 style = 'text-align: center; color: grey;'>As 10 microrregiões paraibanas com mais gastos em licitações (Geral)</h4>", unsafe_allow_html= True)
        co1, co2, co3 = c1.columns([0.5, 2, 0.5])
        co1.write("")
        co2.dataframe(agrupamento_geral_micro.style.applymap(lambda x: 'color: red' if any('João' in words for words in str(x).split()) else ''))
        co3.write("")
        with c1.expander("Observações"):
            st.write(f"""
                    O município de Pedra Branca, com menos de 15 mil habitantes, não deveria ter um valor 
                     tão elevado de gastos com licitações...""")
        c1.markdown("""<hr style="height:2px;border:none;color:#006be8;background-color:#006be8;" /> """, unsafe_allow_html=True)


    else:
        c1.markdown("<h4 style = 'text-align: center; color: grey;'>As 10 prefeituras paraibanas com mais gastos em licitações (Geral)</h4>", unsafe_allow_html= True)
        co1, co2, co3 = c1.columns([0.5, 2, 0.5])
        co1.write("")
        co2.dataframe(agrupamento_geral_cidade.style.applymap(lambda x: 'color: red' if any('João' in words for words in str(x).split()) else ''))
        co3.write("")
        with c1.expander("Observações"):
            st.write(f"""
                    O município de Pedra Branca, com menos de 15 mil habitantes, não deveria ter um valor 
                     tão elevado de gastos com licitações...""")
        c1.markdown("""<hr style="height:2px;border:none;color:#006be8;background-color:#006be8;" /> """, unsafe_allow_html=True)


    # Gráfico de somas dos valores licitados em anos diferentes:
    c1.markdown("<h4 style = 'text-align: center; color: grey;'>Total de valores licitados por ano (Geral)</h4>", unsafe_allow_html= True)
    c1.write("#")
    agrupamento_geral_ano["ano_homologacao_licitacao"] = agrupamento_geral_ano["ano_homologacao_licitacao"]
    agrupamento_geral_ano.columns = ["ANO", "GASTO COM LICITAÇÕES"]
    c1.line_chart(agrupamento_geral_ano, x = str("ANO"), y = "GASTO COM LICITAÇÕES", color = "#9B111E")


    
    # Tabela de soma de valor licitado por cidades
    if c3.toggle("Microrregiões Shows"):
        c3.markdown("<h4 style = 'text-align: center; color: grey;'>As 10 microrregiões paraibanas com mais gastos em licitações (Geral)</h4>", unsafe_allow_html= True)
        co1, co2, co3 = c3.columns([0.5, 2, 0.5])
        co1.write("")
        co2.dataframe(agrupamento_micro.style.applymap(lambda x: 'color: red' if any('João' in words for words in str(x).split()) else ''))
        co3.write("")
        with c3.expander("Observações"):
            st.write(f"""
                    O município de Pedra Branca, com menos de 15 mil habitantes, não deveria ter um valor 
                     tão elevado de gastos com licitações...""")
        c3.markdown("""<hr style="height:2px;border:none;color:#006be8;background-color:#006be8;" /> """, unsafe_allow_html=True)

    else:
        c3.markdown("<h4 style = 'text-align: center; color: grey;'>As 10 prefeituras paraibanas com mais gastos licitações (Shows)</h4>", unsafe_allow_html= True)
        co1, co2, co3 = c3.columns([0.5, 2, 0.5])
        co1.write("")
        co2.dataframe(agrupamento_cidade.style.applymap(lambda x: 'color: #006be8' if any('João' in words for words in str(x).split()) else ''))
        co1.write("")
        with c3.expander("Observações"):
            st.write(f"""
                    O município de Santa Luzia salta para o primeiro lugar nos gastos específicos com shows,
                     em virtude da época de Festa Junina, onde se contratam várias bandas com cachês elevados para participarem
                     de eventos no interior.""")
        c3.markdown("""<hr style="height:2px;border:none;color:#006be8;background-color:#006be8;" /> """, unsafe_allow_html=True)
  

    # Gráfico de somas dos valores licitados de shows em anos diferentes:
    c3.markdown("<h4 style = 'text-align: center; color: grey;'>Total de valores licitados por ano (Shows)</h4>", unsafe_allow_html= True)
    c3.write("#")
    agrupamento_ano.columns = ["ANO", "GASTO COM LICITAÇÕES"]
    c3.line_chart(agrupamento_ano, x = "ANO", y = "GASTO COM LICITAÇÕES", color = "#006be8")

    # Observações dos gráficos de linha (ano)
    cont = st.container()
    with cont.expander("Observações"):
        st.write(f"""
                Na análise dos valores gastos com licitações por ano, podemos ver que há
                 uma grande queda nos anos de 2020 e 2021, em virtude do período pandêmico,
                  seguido de uma grande subida em 2023, quando as pessoas sairam mais de casa após quarentena.
                 Enquanto isso, podemos ver que no total, os valores gastos seguiu crescendo nos anos pandêmicos,
                 possivelmente em virtude de licitações voltadas para a área da saúde.""")
    st.markdown("""<hr style="height:2px;border:none;color:#006be8;background-color:#006be8;" /> """, unsafe_allow_html=True)

    # MÉTRICAS ACERCA DE PROPONENTES
    c1, c2, c3 = st.columns([2, 0.5, 2])

    co1, co2, co3 = c1.columns([0.5, 2, 0.5])
    co1.write("")
    co2.metric("PROPONENTE DA MAIOR LICITAÇÃO", "GUSTTAVO LIMA")
    co3.write("")


    co1, co2, co3 = c3.columns([0.5, 2, 0.5])
    co1.write("")
    co2.metric("VALOR DA MAIOR LICITAÇÃO", "900.000,00")
    co3.write("")

    st.markdown("""<hr style="height:2px;border:none;color:#006be8;background-color:#006be8;" /> """, unsafe_allow_html=True)


    # Gráfico de barras com valor licitado dependendo do jurisdicionado
    
    df_pref = df_shows[["nome_tipo_jurisdicionado", "valor_licitado_licitacao"]]
    df_pref.columns = ["TIPO  JURISDICIONADO", "GASTO COM LICITAÇÕES DE SHOWS"]

    st.markdown("<h4 style = 'text-align: center; color: grey;'>Total de valores licitados tipo de Jurisdicionado</h4>", unsafe_allow_html= True)
    st.write("#")
    st.bar_chart(df_pref, x = "TIPO  JURISDICIONADO", y = "GASTO COM LICITAÇÕES DE SHOWS")

    cont = st.container()
    with cont.expander("Observações"):
        st.write(f"""
                Nas licitações de shows e eventos musicais, a prefeitura normalmente
                é o jurisdicionado encaregado pelo processo licitatório.""")
        
    st.markdown("""<hr style="height:2px;border:none;color:#006be8;background-color:#006be8;" /> """, unsafe_allow_html=True)

    dados_novos = pd.read_csv("/Users/pedroafmelo/Documents/projetos/licitacoes/data/novos_dados.csv")
    st.markdown("<h4 style = 'text-align: center; color: grey;'>Variação do valor gasto com licitações de shows por habitante ao longo dos anos</h4>", unsafe_allow_html= True)
    st.write("#")

    cidade =  st.selectbox(
    'Escolha uma entre as 10 cidades com maior de Gasto Por População em 2021 (Ou JP/CG):',
    ["João Pessoa", "Campina Grande", "Riacho dos Cavalos", "Monte Horebe", "Triunfo", "Nova Floresta", "Areial", "Pitimbu", "Nova Palmeira", "Juarez Távora", "Alagoinha", "Serra Grande"])
    st.write("#")
    st.line_chart(dados_novos.query(f"nome_mun == '{cidade}'"), x = str("ano"), y = "lic/pop", color = "#006be8")

    cont = st.container()
    with cont.expander("Observações"):
        st.write(f"""
                Uma observação importante e lógica é de que, em geral, 
                quanto maior a cidade, menor o seu lic/pop.""")


if __name__ == "__main__":
    main()