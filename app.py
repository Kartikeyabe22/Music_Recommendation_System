import streamlit as st
import pickle
import pandas as pd

def recommend(musics):
    music_index = music[music['title'] == musics].index[0]
    distances = similarity[music_index]
    music_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_music = []
    
    for i in music_list:
        music_title = music.iloc[i[0]].title
        recommended_music.append(music_title)
    
    return recommended_music

# Load models and data
music_dict = pickle.load(open(r'E:\Main Downloads\musicrec.pkl', 'rb'))
music = pd.DataFrame(music_dict)

similarity = pickle.load(open(r'E:\Main Downloads\similarities.pkl', 'rb'))
st.title('Music Recommendation System')

selected_music_name = st.selectbox('Select a music you like', music['title'].values)

if st.button('Recommend'):
    with st.spinner("Generating recommendations..."):  # Show a spinner while processing
        names = recommend(selected_music_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown(f"**1.** {names[0]}")  # Using markdown to ensure the full text is visible
        st.write("")  # Adding space if needed
        
    with col2:
        st.markdown(f"**2.** {names[1]}")
        st.write("")
        
    with col3:
        st.markdown(f"**3.** {names[2]}")
        st.write("")
        
    with col4:
        st.markdown(f"**4.** {names[3]}")
        st.write("")
        
    with col5:
        st.markdown(f"**5.** {names[4]}")
        st.write("")
