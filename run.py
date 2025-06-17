from pathlib import Path

# Parâmetros de entrada
qtd_caracteres = 3  # Exemplo: nome com 2 caracteres antes do domínio
dominio_tipo = ".com.br"  # Exemplo: você quer domínios com o tipo "com.br"
incluir_numeros = None  # Defina como True para permitir números, False para excluir
comecar_com = None  # Ex: "ab" para nomes que comecem com "ab", ou None para ignorar
terminar_com = None  # Ex: "cd" para nomes que terminem com "cd", ou None para ignorar
ocorrencia = ''  # Ex: "app" para buscar nomes que contenham "app", ou None para ignorar

# Caminho da pasta (cole direto do Windows)
caminho_pasta = r'C:\Users\Win\Documents\Agencia\Registro\listas\12-06-2025'

# Nome do arquivo (troque somente aqui quando quiser mudar de arquivo)
nome_arquivo = 'lista-processo-liberacao.txt'

# Junta o caminho com o nome do arquivo no formato universal
arquivo_txt = Path(caminho_pasta) / nome_arquivo
arquivo_txt = arquivo_txt.as_posix()

def filtrar_dominios(arquivo, qtd_caracteres=None, dominio_tipo=None,
                     incluir_numeros=True, comecar_com=None, terminar_com=None,
                     ocorrencia=None):
    try:
        with open(arquivo, "r", encoding="utf-8") as file:
            domains = file.read().splitlines()
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
        return ""
    
    resultados = []
    
    for domain in domains:
        nome, *extensao = domain.split(".")
        extensao = "." + ".".join(extensao)  # Reconstruir a extensão (ex: ".com.br")

        if qtd_caracteres and len(nome) != qtd_caracteres:
            continue
        
        if dominio_tipo and not domain.endswith(dominio_tipo):
            continue

        if not incluir_numeros and any(char.isdigit() for char in nome):
            continue

        if comecar_com and not nome.startswith(comecar_com):
            continue

        if terminar_com and not nome.endswith(terminar_com):
            continue

        if ocorrencia and ocorrencia not in nome:
            continue
        
        resultados.append(domain)
    
    return "\n".join(resultados)

# Chamar a função para filtrar os domínios
resultado = filtrar_dominios(
    arquivo_txt,
    qtd_caracteres=qtd_caracteres,
    dominio_tipo=dominio_tipo,
    incluir_numeros=incluir_numeros,
    comecar_com=comecar_com,
    terminar_com=terminar_com,
    ocorrencia=ocorrencia
)

# Exibir a saída
print(resultado)
