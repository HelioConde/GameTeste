# Eclipse Vanguard — protótipo original de ação 2D

Projeto **Godot 4.7.2** em desenvolvimento, inspirado na dinâmica de ação, combos, mobilidade e plataformas de jogos como Grand Chase. Usa personagens, cenário e identidade originais: não reutiliza personagens, marcas ou artes de terceiros.

## Primeira versão

- Arena lateral de 3.200 pixels com plataformas atravessáveis por baixo.
- Herói com andar, salto, combo de três golpes, ataque forte, dash e especial em área.
- Adversários com perseguição, animação de preparação do golpe, dano, recuo e barra de vida.
- Ondas crescentes, inimigos de elite, experiência, evolução, recuperação e pontuação.
- HUD de vida, energia, EXP, nível, ondas e tempos de recarga.
- Gráficos provisórios desenhados diretamente no Godot, sem dependências de assets externos.
- GitHub Actions com importação do projeto e smoke test do combate.

## Jogar

1. Instale o **Godot 4.7.2** (versão padrão, sem .NET).
2. Abra a pasta do repositório pelo Gerenciador de Projetos do Godot.
3. Pressione **F6** na cena Main ou **F5** para jogar o projeto.

| Controle | Tecla |
| --- | --- |
| Caminhar | A / D ou setas |
| Saltar | W, seta para cima ou Espaço |
| Combo básico | J (toques sequenciais) |
| Ataque forte | K |
| Esquiva rápida | Shift |
| Especial em área | L (consome 35 de energia) |
| Reiniciar após perder | R ou Enter |

## Sprites com PixelLab

O projeto está preparado para usar **sprites PNG originais gerados pelo PixelLab** para herói e inimigos, com animações de corrida e ataques, mantendo os desenhos existentes como fallback.

1. Coloque seu token da API do PixelLab como segredo `PIXELLAB_API_KEY` em **Settings → Secrets and variables → Actions**.
2. Abra a Action **PixelLab — gerar sprites e criar PR** e execute primeiro com `generate=false` (simulação gratuita).
3. Para gerar os sprites reais, execute novamente com `generate=true`. **A geração consome créditos da conta PixelLab**.
4. Confira os PNGs no artefato/PR produzidos pela Action. Após a integração da PR, o Godot usa as animações na versão Web.

Detalhes: [assets/pixellab/README.md](assets/pixellab/README.md).

## Testar localmente

~~~sh
godot --headless --editor --path . --quit
godot --headless --path . --script res://tests/smoke_test.gd
~~~

O workflow `.github/workflows/godot-checks.yml` faz essa conferência nos pushes e pull requests.

## Organização

- `project.godot`: configuração do motor.
- `scenes/Main.tscn`: ponto de entrada.
- `scripts/arena.gd`: cenário, UI, spawn e progressão das ondas.
- `scripts/hero.gd`: movimentação, combate e evolução.
- `scripts/foe.gd`: comportamento dos adversários.
- `tests/smoke_test.gd`: verificação automatizada.
- `docs/ROADMAP.md`: evolução planejada.

O objetivo é desenvolver uma experiência própria e ampliar os sistemas de combate de forma incremental, preservando a jogabilidade testável a cada alteração.
