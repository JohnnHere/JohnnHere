# Ferramenta de Desfoque de Fundo

Uma ferramenta Python para desfocar o fundo de imagens mantendo a pessoa em foco.

## Recursos

- Detecção e segmentação automática de pessoas
- Efeito de desfoque suave no fundo
- Força de desfoque ajustável
- Interface de linha de comando fácil de usar

## Instalação

Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

## Uso

Uso básico:
```bash
python blur_background.py imagem_entrada.jpg
```

Especificar arquivo de saída:
```bash
python blur_background.py imagem_entrada.jpg imagem_saida.jpg
```

Ajustar a força do desfoque (padrão é 35):
```bash
python blur_background.py imagem_entrada.jpg imagem_saida.jpg 45
```

## Como funciona

A ferramenta usa:
- **MediaPipe Selfie Segmentation** para detecção precisa de pessoas
- **OpenCV** para processamento de imagem e efeitos de desfoque
- Desfoque gaussiano para efeito de fundo suave
- Suavização automática de bordas para resultados naturais

## Requisitos

- Python 3.7+
- OpenCV
- MediaPipe
- NumPy
- Pillow

Veja `requirements.txt` para versões específicas.

## Exemplo

1. Coloque sua imagem no diretório do projeto
2. Execute o comando:
   ```bash
   python blur_background.py sua_foto.jpg foto_desfocada.jpg
   ```
3. A imagem com fundo desfocado será salva como `foto_desfocada.jpg`

## Verificar Instalação

Para verificar se todas as dependências estão instaladas corretamente:

```bash
python check_installation.py
```
