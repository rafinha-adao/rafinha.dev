# Kit Currículo + Site + LinkedIn · Rafael de Oliveira Adão
### Gerado em agosto de 2026

Tudo o que construímos, organizado para uso.

## curriculo/
- **curriculo.html**: a fonte única do currículo. Edite aqui (pontos de edição marcados com comentários no código).
- **fontes/**: as fontes do documento (Space Grotesk para títulos, Inter para texto, JetBrains Mono para código), embutidas via @font-face. O build funciona em qualquer máquina sem instalar fontes no sistema.
- **build.py**: gera o PDF e o PNG. Uso: `python3 build.py` (requer `pip install weasyprint pikepdf` e poppler-utils para o PNG; instruções no topo do arquivo).
- **curriculo.pdf**: versão para enviar em vagas e e-mails. Links clicáveis (e-mail, telefone, site, GitHub, LinkedIn, NoShorts) e metadados de SEO nas propriedades do documento.
- **curriculo.png**: versão imagem para posts e pré-visualizações. Sem links (é imagem).

## site/
- **index.html**: o novo rafinha.dev, mesma identidade do currículo. Responsivo, HTML semântico, SEO completo (meta tags, Open Graph e JSON-LD schema.org embutidos).
- **llms.txt**: contexto público sobre você para crawlers de IA. Vai na raiz do site.
- **publicar.md**: passo a passo para publicar no GitHub Pages ou Cloudflare Pages e apontar o domínio rafinha.dev, com checklist pós-publicação.
- Lembrete: copie o `curriculo.pdf` para a pasta do site publicado (o botão de download aponta para `/curriculo.pdf`).

## linkedin/
- **guia-linkedin.md**: guia de otimização atualizado, com headline, Sobre e descrições prontas para colar, mais checklist de execução.

## Regras editoriais adotadas (para manter nas próximas edições)
1. Nada de números específicos que mudam com o tempo: use "centenas", "milhares", "dezenas".
2. Nada de detalhes internos de empresa: só o que é público nos sites delas.
3. Sem travessões no meio do texto; frases curtas e diretas.
4. Uma única referência dev no visual (o prompt do topo); o resto legível para qualquer pessoa.

## Fluxo de atualização futura
1. Edite `curriculo/curriculo.html`
2. Rode `python3 build.py`
3. Replique o trecho alterado em `site/index.html` (mesmas classes e seções)
4. Suba o novo `curriculo.pdf` junto com o site
5. Espelhe a mudança no LinkedIn
