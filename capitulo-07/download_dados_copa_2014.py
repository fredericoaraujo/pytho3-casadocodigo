import io
import sys
import urllib.request as request


BUFFER_SIZE = 1024

def download_length(response, output, length):
    times = length // BUFFER_SIZE
    if length % BUFFER_SIZE > 0:
        times += 1

    for time in range(times):
        output.write(response.read(BUFFER_SIZE))
        print("Downloaded {}".format(time * BUFFER_SIZE / length * 100))


def download():
    total_download = 0
    while True:
        data = response.read(BUFFER_SIZE)
        total_downloaded += len(data)
        if not data:
            break

        out_file.write(data)
        print("Downloaded {bytes}".format(bytes = total_downloaded))


def main():
    response = request.urlopen(sys.argv[1])
    out_file = io.FileIO("saida.zip", mode="w")

    print(response, out_file)

    content_length = response.getheader('Content-Length')

    try:
        if content_length:
            length = int(content_length)
            download_length(response, out_file, length)
        else:
            download(response, out_file)
    except Exception as e:
        print("Ocorreu um erro durante o download do arquivo {}"
                .format(sys.argv[1]))
    finally:
        response.close()
        out_file.close()

    print("Finished")


if __name__ == "__main__":
    main()

"""
Comando para executar o programa
python download_dados_copa.py http://livropython.com.br/dados.zip
"""
