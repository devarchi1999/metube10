import streamlit as st
from googleapiclient.discovery import build
import pafy
import vlc
import time


# Api keys
youtube_key = 'AIzaSyC5U5fP5mTI_dpNDJn4wCr9QPe5ulpdRHI'
cloudconvert_key = 'nH56ZHB1V1an079FFpmYbgm3PnPSD1sfGVBhXFAb5Li1BidXWSbfNakiY2dSxdGr'
# setting the page initial layout
st.set_page_config(layout="wide",initial_sidebar_state='collapsed',page_title='MeTube')

# Creating the title and the necessary header sections of the webapp
st.title('MeTube : Music for People')
st.markdown('---')


# Creating the SideBar
st.sidebar.markdown('# Login Id')
email = st.sidebar.text_input(label='Enter the email id')

st.markdown(
"""
<br><br/>
""", unsafe_allow_html=True)

st.sidebar.markdown('# Password')
password = st.sidebar.text_input(label='Enter the Password')


# Creating the Search Bar
st.beta_container()
st.write('# Search Music')
search_music = st.text_input(label='')

if st.button('Search'):
    # Creating the search keyword
    search_music = search_music.strip().split()
    key = ''
    for word in search_music:
        key += word + '+'

    # Creating the search object
    youtube = build('youtube', 'v3', developerKey=youtube_key)
    request = youtube.search().list(
        part="snippet",
        q=key,
        maxResults=20,
    )


    # Getting the response to the search request
    response = request.execute()
    id_list = []
    desp_list = []
    for item in response['items']:
        try:
            id_list.append(str(item['id']['videoId']))
            desp_list.append([str(item['snippet']['title']), str(item['snippet']['channelTitle'])])
        except Exception :
            pass
    video_desp = dict(zip(id_list,desp_list))
    # st.write(video_desp)
    for item in id_list:
        print(video_desp[item])
    search_string = 'https://www.youtube.com/watch?v=' + id_list[0]
    # mega = Mega()
    # m = mega.login('devarchi1999@gmail.com', 'growup1999')
    # folder = m.find('Playlist 1')

    url = search_string
    video = pafy.new(url)
    best = video.getbest()
    playurl = best.url
    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    player.play()
    time.sleep(10)
    player.stop()
    # if st.button('Stop'):
    #     player.stop()
    # col1,col2,col3 = st.beta_columns(3)
    # # while True:
    #
    # if col1.button('Play',key='Play'):
    #     player.play()
    # if col2.button('Pause',key='Pause'):
    #     player.pause()
    # if col3.button('Stop',key='Stop'):
    #     player.stop()

    # song_ids = []
    # song_names = []
    # for key,value in video_desp.items():
    #     song_names.append(value[0])
    #     song_ids.append('https://www.youtube.com/watch?v='+str(key))
    # search_songs_dict = dict(zip(song_ids,song_names))
    #
    # search_string = st.selectbox('', list(search_songs_dict.keys()),format_func=search_songs_dict.get)
    # st.write(search_string)
    # url = search_string
    # video = pafy.new(url)
    # best = video.getbest()
    # playurl = best.url
    # Instance = vlc.Instance()
    # player = Instance.media_player_new()
    # Media = Instance.media_new(playurl)
    # Media.get_mrl()
    # player.set_media(Media)
    # while True:
    #     if st.button('Play'):
    #         player.play()
    #     if st.button('Pause'):
    #         player.pause()
    #     if st.button('Stop'):
    #         player.stop()
        # user = input('').strip()
        # if user == 'Play':
        #     player.play()
        # if user == 'Pause':
        #     player.pause()
        # if user == 'Stop':
        #     player.stop()
        #     break

    # Collecting audio from video searched
    # for item in id_list:
    #     print(video_desp[item])
    # song_name = [video_desp[i][0] for i in id_list]
    # song_id = ['https://www.youtube.com/watch?v='+i for i in id_list]
    # # search_string = 'https://www.youtube.com/watch?v='+id_list[0]
    # st.write(song_name)
    # st.write(song_id)
    # st.write(search_string)
    # option = st.selectbox(
    # 'How would you like to be contacted?',
    # ('Email', 'Home phone', 'Mobile phone'))
    # st.write('You selected:', option)

# url = search_string
# video = pafy.new(url)
# best = video.getbest()
# playurl = best.url
# Instance = vlc.Instance()
# player = Instance.media_player_new()
# Media = Instance.media_new(playurl)
# Media.get_mrl()
# player.set_media(Media)















