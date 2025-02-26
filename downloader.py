import streamlit as st
from pytubefix import YouTube

def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        filename = stream.download()
        return filename
    except Exception as e:
        st.error(f"Error: {e}")
        return None

def main():
    st.title("YouTube Video Downloader")
    
    url = st.text_input("Enter YouTube Video URL:")
    
    if st.button("Download Video"):
        if url:
            filename = download_video(url)
            if filename:
                with open(filename, "rb") as file:
                    st.download_button(label="Download File", data=file, file_name=filename, mime="video/mp4")
        else:
            st.warning("Please enter a valid YouTube URL")

if __name__ == "__main__":
    main()
