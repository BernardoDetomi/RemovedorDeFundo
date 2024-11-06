# 🖼️ Removedor de Fundo de Imagem

Este é um script em Python que utiliza a biblioteca `rembg` para remover o fundo de uma imagem automaticamente. Ele carrega uma imagem de entrada (`imgfundo.jpg`), processa-a para remover o fundo e salva o resultado como uma nova imagem (`imgsemfundo.png`).

## 🚀 Funcionalidade Principal

1. **Remoção Automática de Fundo**:
   - Carrega uma imagem especificada pelo usuário.
   - Utiliza a biblioteca `rembg` para remover o fundo da imagem.
   - Salva o resultado em um novo arquivo sem fundo.

## 🖼️ Aplicativo

### Imagem teste - Imagem com fundo
<img src="./prints/imgfundo.jpg" alt="Imagem com fundo" width="600"/>

### Imagem depois do código executado - Imagem sem fundo
<img src="./prints/imgsemfundo.png" alt="Imagem sem fundo" width="600"/>

## 🛠️ Tecnologias Utilizadas

- **rembg**: Biblioteca em Python que usa técnicas de machine learning para remover o fundo de imagens.
- **Pillow (PIL)**: Biblioteca para manipulação e processamento de imagens.

## 📦 Instalação e Uso

1. Clone este repositório:
   ```bash
   git clone https://github.com/BernardoDetomi/RemovedorDeFundo.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd RemovedorDeFundo
   ```

3. Instale as dependências:
   ```bash
   pip install rembg pillow
   ```

   > **Nota**: Certifique-se de que está usando uma versão compatível do Python (entre 3.8 e 3.11).

4. Coloque a imagem da qual deseja remover o fundo no diretório do projeto e renomeie-a para `imgfundo.jpg` ou altere o nome no código para corresponder ao arquivo desejado.

5. Execute o script:
   ```bash
   python remover_fundo.py
   ```

6. A imagem com o fundo removido será salva como `imgsemfundo.png` no mesmo diretório.

## 📋 Estrutura do Código

- **Importações**:
   - `rembg`: Usado para processar e remover o fundo da imagem.
   - `Pillow`: Biblioteca para carregar e salvar a imagem.

- **Fluxo do Script**:
   - `Image.open('imgfundo.jpg')`: Carrega a imagem de entrada.
   - `remove(url)`: Remove o fundo da imagem.
   - `output.save('imgsemfundo.png')`: Salva a imagem sem fundo.

## 🆘 Suporte  

Se você encontrar algum problema ou tiver dúvidas, sinta-se à vontade para abrir uma issue no repositório ou entre em contato:  

- **Email**: bernardomd01@gmail.com 
- **Twitter**: @Bernardo_md  
- **Instagram**: @bernardoo.md  

## Contribuições  

Contribuições são bem-vindas! Sinta-se à vontade para contribuir com novas funcionalidade para o SmartBite.AI e para abrir problemas (issues) ou enviar pull requests com melhorias! Toda ajuda é bem-vinda.    

## Autores  
 
- Bernardo Maia Detomi.
