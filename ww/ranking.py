import pandas as pd
import streamlit as st
from finalapp import*
gk=GK[GK['minutes']>700]
df=DF[DF['minutes']>700]
fw=FW[FW['minutes']>700]
mf=MF[MF['minutes']>700]
gk['rank']=0.04*gk['clean_sheets_pct']+(1/3)*(gk['saves']/gk['games_starts_gk'])-(1/2)*(gk['goals_conceded']/gk['games_starts_gk'])
mf['rank']=5*(mf['goals_scored']/mf['games_starts'])+3*(mf['assists']/mf['games_starts'])
df['rank']=4*(df['clean_sheets']/df['games_starts'])+6*(df['goals_scored']/df['games_starts'])+3*(df['assists']/df['games_starts'])-(1/2)*(df['goals_conceded']/df['games_starts'])
fw['rank']=4*(fw['goals_scored']/fw['games_starts'])+3*(fw['assists']/fw['games_starts'])
def app():
    col1, col2= st.beta_columns(2)
    with col1:
        st.write('Best Goalkeepers')
        st.dataframe(gk[['web_name','rank']].sort_values('rank',ascending=False).head(20),300,400)
        st.write('Best Defenders')
        st.dataframe(df[['web_name','rank']].sort_values('rank',ascending=False).head(20),300,400)
    with col2:
        st.write('Best Midfielders')
        st.dataframe(mf[['web_name','rank']].sort_values('rank',ascending=False).head(20),300,400)
        st.write('Best Forwards')
        st.dataframe(fw[['web_name','rank']].sort_values('rank',ascending=False).head(20),300,400)