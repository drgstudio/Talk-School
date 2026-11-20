# Publicar o site do Talk School

## 1. Gerar o APK
Android Studio > Build > Generate Signed Bundle / APK > APK > release.
Guarde a keystore em local seguro (sem ela não consegue atualizar o app).

## 2. Hospedar (grátis) — opção recomendada: GitHub
1. Crie um repositório público no GitHub (ex.: `talkschool`).
2. Envie o conteúdo desta pasta (index.html, img, robots.txt, etc.).
3. Settings > Pages > Source: `main` / root. O site fica em `https://SEU-USUARIO.github.io/talkschool/`.
4. Crie um **Release** (ex.: v1.0) e anexe o `TalkSchool.apk` (limite 2 GB por ficheiro).
5. No fim do `index.html`, no bloco CONFIG, troque:
   `apkUrl: "https://github.com/SEU-USUARIO/talkschool/releases/latest/download/TalkSchool.apk"`
   (assim o link nunca muda, mesmo em versões novas.)

Alternativas: Netlify ou Firebase Hosting (o ficheiro `_headers` já está pronto para o Netlify).
O APK já está em downloads/TalkSchool.apk (cerca de 2,5 MB), então o site e o app saem juntos em qualquer hospedagem.

## 3. Definir o endereço (domínio)
Dentro desta pasta: `python3 definir_dominio.py https://SEU-USUARIO.github.io/talkschool`
Isto troca o `SEU-DOMINIO` no canonical, sitemap, robots e dados estruturados.

## 4. Aparecer no Google
1. Abra https://search.google.com/search-console e adicione o site (propriedade "Prefixo do URL").
2. Verifique a propriedade (o Google dá um ficheiro HTML para enviar, ou uma meta tag).
3. Em "Sitemaps", envie `sitemap.xml`.
4. Em "Inspeção de URL", cole o endereço do site e clique em "Solicitar indexação".
A indexação leva de alguns dias a semanas. Pesquisar "Talk School" sozinho pode demorar,
porque o nome é comum; um domínio próprio e links de outros sites (redes sociais, WhatsApp) ajudam.

## 5. Nova versão do app
1. Aumente `versionCode` e `versionName` em `app/build.gradle.kts`.
2. Gere o APK novo e publique no Release.
3. No `index.html` (CONFIG) e no `version.json`, atualize versão, data e tamanho.

## Nota sobre instalação
O APK fora da Play Store mostra o aviso "fonte desconhecida", e o Google Play Protect pode pedir
confirmação. O site já explica o passo a passo. Para remover o aviso, só publicando na Google Play.
