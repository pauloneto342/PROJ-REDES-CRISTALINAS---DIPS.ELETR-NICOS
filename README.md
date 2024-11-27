
# Visualização de Redes Cristalinas em 3D

Este repositório contém uma implementação em Python para a visualização de diferentes tipos de redes cristalinas tridimensionais (3D) usando **matplotlib** e **NumPy**. O objetivo do projeto é criar gráficos 3D que representam as redes cúbica, tetragonal, ortorrômbica, monoclínica, triclínica, trigonal (R e C) e hexagonal.

## Tipos de Redes Cristalinas

O código gera visualizações para os seguintes tipos de redes cristalinas:

1. **Rede Cúbica Simples (Cubic Simple)**
2. **Rede Tetragonal P (Tetragonal P)**
3. **Rede Ortorrômbica P (Orthorhombic P)**
4. **Rede Monoclínica P (Monoclinic P)**
5. **Rede Triclínica P (Triclinic P)**
6. **Rede Trigonal R (Trigonal R)**
7. **Rede Trigonal C (Trigonal C)**
8. **Rede Hexagonal P (Hexagonal P)**

Essas redes são modeladas com base em parâmetros de comprimento de célula unitária e ângulos entre os eixos, permitindo a visualização das estruturas cristalinas em 3D.

## Requisitos

Para rodar o código, é necessário ter o Python instalado juntamente com as bibliotecas **NumPy** e **matplotlib**. Você pode instalar essas bibliotecas utilizando o **pip**:

```bash
pip install numpy matplotlib
```

## Como Usar

1. Clone o repositório para o seu computador:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

2. Navegue até o diretório do projeto:

```bash
cd nome-do-repositorio
```

3. Execute o script Python para gerar as visualizações das redes cristalinas:

```bash
python nome_do_arquivo.py
```

Isso abrirá as visualizações das redes cristalinas em gráficos 3D usando **matplotlib**. Você pode interagir com os gráficos para explorar as estruturas.

## Estrutura do Código

O código está organizado da seguinte forma:

- **Funções de geração de pontos da rede**: Cada tipo de rede é representado por um conjunto de pontos no espaço tridimensional. A função `generate_lattice_points` é responsável por gerar esses pontos com base nas células unitárias definidas pelos vetores \(a\), \(b\) e \(c\).

- **Funções de plotagem**: As funções como `plot_cubic_simple`, `plot_tetragonal_p`, `plot_orthorhombic_p`, entre outras, geram as visualizações específicas de cada tipo de rede.

- **Função principal**: A função `main` executa todas as funções de plotagem para exibir as diferentes redes em sequência.

## Contribuições

Contribuições são bem-vindas! Se você quiser contribuir para este projeto, siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature: `git checkout -b minha-feature`.
3. Faça commit das suas alterações: `git commit -am 'Adicionando minha feature'`.
4. Envie a branch para o seu fork: `git push origin minha-feature`.
5. Abra um pull request explicando as mudanças.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Para dúvidas ou sugestões, entre em contato:

- **Email**: seu-email@example.com
- **GitHub**: [seu-usuario](https://github.com/seu-usuario)
