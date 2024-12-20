import cv2
import os
import csv

# Diretório para salvar as imagens capturadas
IMAGE_DIR = "cadastros"
CSV_FILE = "dados.csv"

# Criar o diretório de imagens se não existir
os.makedirs(IMAGE_DIR, exist_ok=True)

def capturar_imagem(nome):
    # Inicia a captura de vídeo
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Erro ao acessar a câmera.")
        return None
    
    print("Pressione 'SPACE' para capturar a imagem ou 'ESC' para sair.")
    imagem_capturada = None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Falha ao capturar imagem.")
            break

        # Exibir a imagem capturada em uma janela
        cv2.imshow("Captura de Imagem", frame)

        # Verificar tecla pressionada
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC para sair
            break
        elif key == 32:  # SPACE para capturar
            imagem_capturada = frame
            break

    cap.release()
    cv2.destroyAllWindows()

    if imagem_capturada is not None:
        # Salvar a imagem com o nome fornecido
        file_path = os.path.join(IMAGE_DIR, f"{nome}.jpg")
        cv2.imwrite(file_path, imagem_capturada)
        print(f"Imagem salva em {file_path}")
        return file_path
    else:
        print("Nenhuma imagem foi capturada.")
        return None

def salvar_dados(nome, idade, file_path):
    # Salvar os dados em um arquivo CSV
    dados = [nome, idade, file_path]
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Nome", "Idade", "Imagem"])
        writer.writerow(dados)

    print(f"Dados salvos: {dados}")

def main():
    print("Sistema de Cadastro")
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")

    # Captura a imagem da pessoa
    file_path = capturar_imagem(nome)
    if file_path:
        salvar_dados(nome, idade, file_path)
        print("Cadastro concluído com sucesso!")
    else:
        print("Falha no cadastro.")

if __name__ == "__main__":
    main()
