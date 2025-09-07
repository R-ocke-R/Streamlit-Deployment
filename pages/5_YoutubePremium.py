import streamlit as st
import yt_dlp
import tempfile
import os

def download_youtube_bytes(url: str, file_format: str = "mp3"):
    """Download into a temp folder, read bytes, and return (bytes, filename, mime, sizeMB)."""
    with tempfile.TemporaryDirectory() as tmpdir:
        if file_format == "mp3":
            ydl_opts = {
                "format": "bestaudio/best",
                "outtmpl": os.path.join(tmpdir, "%(title)s.%(ext)s"),
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }],
                "quiet": True,
            }
            mime = "audio/mpeg"
        else:
            ydl_opts = {
                "format": "bestvideo+bestaudio/best",
                "outtmpl": os.path.join(tmpdir, "%(title)s.%(ext)s"),
                "merge_output_format": "mp4",
                "quiet": True,
            }
            mime = "video/mp4"

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            outfilename = ydl.prepare_filename(info)
            if file_format == "mp3":
                outfilename = os.path.splitext(outfilename)[0] + ".mp3"
            else:
                outfilename = os.path.splitext(outfilename)[0] + ".mp4"

        with open(outfilename, "rb") as f:
            data = f.read()

        size_mb = round(len(data) / (1024 * 1024), 2)

    return data, os.path.basename(outfilename), mime, size_mb


# ---- Streamlit App ----
st.set_page_config(page_title="YouTube Downloader", page_icon="⬇️", layout="wide")

st.markdown("<h1 style='text-align: center;'>⬇️ YouTube Downloader</h1>", unsafe_allow_html=True)
st.write("Paste a YouTube link and download it directly as MP3 (audio) or MP4 (video).")

youtube_url = st.text_input("🎥 Enter YouTube video URL:")

col1, col2 = st.columns(2)

if youtube_url:
    with col1:
        if st.button("Download MP3 🎵"):
            with st.spinner("Fetching and converting to MP3..."):
                try:
                    data, filename, mime, size_mb = download_youtube_bytes(youtube_url, "mp3")
                    st.success(f"Ready: {filename} ({size_mb} MB)")
                    st.download_button(
                        label=f"⬇️ Download {filename}",
                        data=data,
                        file_name=filename,
                        mime=mime,
                        use_container_width=True,
                    )
                except Exception as e:
                    st.error(f"Download failed: {e}")

    with col2:
        if st.button("Download MP4 🎬"):
            with st.spinner("Fetching MP4..."):
                try:
                    data, filename, mime, size_mb = download_youtube_bytes(youtube_url, "mp4")
                    st.success(f"Ready: {filename} ({size_mb} MB)")
                    st.download_button(
                        label=f"⬇️ Download {filename}",
                        data=data,
                        file_name=filename,
                        mime=mime,
                        use_container_width=True,
                    )
                except Exception as e:
                    st.error(f"Download failed: {e}")




st.container(border=False, height=200)
st.markdown(
    """
    <footer style="text-align: center; margin-top: 20px;">
        <p style="font-size: 12px; color: #777;">Disclaimer: I don't think this is ethical - please use it only for personal use. </p>
    </footer>
    """,
    unsafe_allow_html=True
)