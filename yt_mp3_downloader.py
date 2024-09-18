import yt_dlp

url = input('Cole o link do youtube: ')

    # Opções para o yt-dlp, incluindo a conversão para mp3
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s'+'mp3',  # Define o nome do arquivo com base no título do vídeo
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}
# Baixando e convertendo o áudio
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download concluído e convertido para MP3!")
