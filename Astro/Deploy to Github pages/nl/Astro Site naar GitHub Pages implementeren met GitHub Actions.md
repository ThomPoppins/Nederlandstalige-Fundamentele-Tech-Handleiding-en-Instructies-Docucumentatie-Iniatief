

[Astro](https://astro.build/) is een modern front-end framework waarmee je snelle, geoptimaliseerde websites kunt bouwen. Het stelt je in staat om componenten te schrijven met je favoriete JavaScript-framework (zoals React, Vue of Svelte), maar rendert ze als statische HTML tijdens het bouwen voor snellere paginaladingen. Bovendien biedt Astro mogelijkheden voor server-side rendering en integreert het goed met populaire tools en frameworks, waardoor prestaties en SEO worden verbeterd.

[Deze blog](https://github.com/aatmmr/aatmmr.github.io) is gebouwd met [Astro](https://astro.build/) en geïmplementeerd op [GitHub Pages](https://pages.github.com/) met behulp van [GitHub Actions](https://github.com/features/actions). Zoals beloofd in mijn [oorspronkelijke bericht](https://xebia.com/blog/deploy-an-astro-site-to-github-pages-using-github-actions/start-blogging), zal ik beschrijven hoe deze site wordt geïmplementeerd en welke configuratie nodig is om te slagen, zelfs met een aangepast domein in gedachten. Astro zelf biedt [gedetailleerde instructies](https://docs.astro.build/en/guides/deploy/github/) die ook moeten worden gebruikt.

## Project voorbereiden

Een werkende Astro-site in een GitHub-repository is nodig voor de volgende stappen. Als je een project nodig hebt om mee te beginnen, kun je de volgende opdracht gebruiken:

```bash
npm create astro@latest -- --template satnaing/astro-paper
```

Dit maakt de basiscode van deze blog met het [Astro Paper-thema](https://astro.build/themes/details/astro-paper).

Kies de repositorynaam als `{jouw-handle}.github.io`, omdat GitHub dit herkent als je persoonlijke pagina en het bijbehorende domein gratis levert. Je kunt echter elke andere naam kiezen als je een aangepast domein gebruikt zonder de URL van GitHub nodig te hebben, of als je tevreden bent met de standaard-URL waarop je pagina beschikbaar zal zijn: `https://{jouw-handle}.github.io/{naam-van-repository}`.

Deze tutorial gebruikt `{jouw-handle}.github.io` als repositorynaam voor eenvoud.

> Let op dat de repository openbaar moet zijn als je de gratis GitHub-plan gebruikt. De repository kan privé zijn als je een betaald GitHub-plan hebt, zoals GitHub Pro voor persoonlijk gebruik van GitHub Teams, of als de repository zich in een organisatie bevindt.

## GitHub Pages inschakelen

GitHub Pages moet worden ingeschakeld voor de repository.

1. Ga naar _Settings > Pages_ van de repository (1).
2. Selecteer _GitHub Actions_ als bron (2) en (3).

![GitHub Pages inschakelen met GitHub Actions als bron](https://xebia.com/wp-content/uploads/2024/01/enable-github-pages-with-github-actions@3x-1024x456.jpg)

Standaard mag er geen workflow beschikbaar zijn in de repository van een Astro-pagina, en daarom gebeurt er niets nadat je GitHub Actions als bron hebt geselecteerd.

## Workflow toevoegen voor implementatie

Nu GitHub Actions is geselecteerd als bron voor GitHub Pages, moet er een workflow aan de repository worden toegevoegd. Maak een nieuw workflowbestand, bijvoorbeeld `.github/workflows/deploy-website.yml`, en plak de volgende code in het nieuwe bestand. Commit deze wijzigingen naar de standaardtak. Let op dat de workflow op de standaardtak moet staan, in mijn geval `main`, om correct te werken. Als dat niet het geval is, wordt er niets geïmplementeerd.

```yaml
name: Deploy Website to GitHub Pages

on:
  push:
    branches: [main]
    paths-ignore:
      - README.md
  workflow_dispatch:

jobs:
  build:
    name: Build
    runs-on: ubuntu-latest
    steps:
      - name: Repository ophalen
        uses: actions/checkout@v4
        with:
          show-progress: false
      - name: Installeren, bouwen en site uploaden
        uses: withastro/action@v1

  deploy:
    name: Implementeren
    needs: build
    runs-on: ubuntu-latest
    permissions:
      pages: write
      id-token: write
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - name: Implementeren naar GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v2
```

Deze workflow maakt gebruik van de [withastro/action](https://github.com/withastro/action) Action die door Astro wordt geleverd en het project klaarmaakt om te worden geïmplementeerd naar GitHub Pages. Zodra de pagina succesvol is gebouwd in de eerste taak, implementeert de [actions/deploy-pages](https://github.com/actions/deploy-pages) Action van GitHub de site naar GitHub Pages. Let op dat de opgegeven `permissions` en de informatie over de `environment` nodig zijn voor de implementatie naar GitHub Pages.

Om te controleren of het werkt, ga je naar het _Actions_-tabblad van de repository en controleer je of de workflow wordt uitgevoerd. Als de workflow slaagt, is de pagina beschikbaar op `https://{jouw-handle}.github.io` of het domein dat GitHub levert als je de specifieke repositorynaam niet gebruikt. De eenvoudigste manier is om naar de hoofdmap van je repository te gaan in de GitHub UI en te zoeken naar de URL in het _About_-gedeelte, zoals te zien is in de onderstaande screenshot.

![URL in Repository-root](https://xebia.com/wp-content/uploads/2024/01/url-in-repository-root@3x-1024x492.png)

## Gebruik van een aangepast domein

GitHub Pages kan de site leveren op een domein dat je opgeeft. De [documentatie](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site) is gedetailleerd, en de volgende stappen zijn bedoeld om alle benodigde stappen beknopt weer te geven. Het vereist een domein naar keuze en toegang tot de DNS-instellingen van dat domein.

Laat je niet in de war brengen, omdat we `{jouw-handle}.github.io` als doel gaan instellen voor je aangepaste domein in sommige van de onderstaande stappen . Dit is vereist omdat het domein `{jouw-handle}.github.io` naast het aangepaste domein bestaat, en de site nog steeds bereikbaar is op dit domein.

### DNS voorbereiden

De DNS-instellingen voor je domein moeten worden voorbereid. Afhankelijk van of je een subdomein wilt gebruiken, zoals `www` en `blog`, of als je een hoofddomein wilt gebruiken (zonder subdomein), hebben de DNS-instellingen respectievelijke invoeren nodig. Ik wil deze instructies duidelijk maken omdat de documentatie in het begin niet duidelijk voor me was. Begin met het openen van de DNS-instellingen van je domein en voeg, afhankelijk van je gewenste opstelling, de volgende invoeren toe.

> Houd er rekening mee dat DNS-updates enkele uren kunnen duren om van kracht te worden.

#### Alleen Subdomein of in combinatie met Apex-domein (`CNAME`)

Als je alleen een subdomein wilt gebruiken, voeg dan een `CNAME`-recordtype toe voor het gewenste subdomein dat verwijst naar je GitHub-pagina, met de waarde:

```
{jouw-handle}.github.io
```

Als je zowel het hoofddomein als het subdomein wilt gebruiken, voeg dit record toe onder je hoofddomein. Als je dat niet doet, ben je klaar en kun je doorgaan naar [Voeg domeinconfiguratie toe aan het project](https://xebia.com/blog/deploy-an-astro-site-to-github-pages-using-github-actions/#add-domain-configuration-to-project).

#### Hoofddomein gebruiken

Om een hoofddomein te kunnen gebruiken, heb je verschillende opties:

- `ANAME`- of `ALIAS`-record,
- `A`-record (IPv4),
- `AAAA`-record (IPv6).

Lees de volgende opties zorgvuldig door en voeg enkele parallel toe als dat nodig of aanbevolen is.

**`ANAME`- of `ALIAS`-record**

Voeg een `ANAME`- of `ALIAS`-record toe en stel het subdomein in op `@`. Voer als waarde in:

```
{jouw-handle}.github.io
```

Dat is alles en je kunt doorgaan met de sectie [Voeg domeinconfiguratie toe aan het project](https://xebia.com/blog/deploy-an-astro-site-to-github-pages-using-github-actions/#add-domain-configuration-to-project). Als je DNS-instellingen geen `ANAME`- of `ALIAS`-recordtype bieden, voeg dan een `A`- of `AAAA`-record toe zoals hieronder beschreven.

**`A`-record (IPv4)**

In plaats van `ALIAS` of `ANAME` kun je `A`-records (`IPv4`) invoeren met `@` als subdomein. Voeg elk van de IP's toe als afzonderlijke invoeren:

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

**`AAAA`-record (IPv6)**

Als je `IPv6`-ondersteuning wilt toevoegen, voeg dan de volgende IP's toe als `AAAA`-recordtype en `@` als subdomein. Voeg ook een `A`-record toe zoals hierboven beschreven, omdat `IPv6` langzaam wordt aangenomen.

```
2606:50c0:8000::153
2606:50c0:8001::153
2606:50c0:8002::153
2606:50c0:8003::153
```

De onderstaande schermafbeelding is een praktisch voorbeeld van mijn DNS-instellingen van deze site met al deze genoemde instellingen. Houd er rekening mee dat mijn DNS-instellingen geen `ANAME` (of alternatief `ALIAS`) bieden, dus voegde ik in plaats daarvan de `A`- en `AAAA`-records toe.

![GitHub Pages relevante DNS-instellingen](https://xebia.com/wp-content/uploads/2024/01/dns-settings@3x-1024x643.png)

### Voeg domeinconfiguratie toe aan het project

Het aangepaste domein moet worden toegevoegd aan de siteconfiguratie van je Astro-project. Open het bestand `astro.config.ts` in de hoofdmap van het project en voeg je domein (`{jouw-domein}`) toe als `site`.

```ts
export default defineConfig({
  site: {jouw-domein},
```

Voeg daarnaast een bestand genaamd `CNAME` (zonder bestandsextensie) toe in de `public`-map en voeg als inhoud het domein (`{jouw-domein}`) van je site toe:

```
{jouw-domein}
```

### Voeg aangepast domein toe aan instellingen

Nu alles is ingesteld en geconfigureerd, moet het aangepaste domein worden toegevoegd aan de GitHub Pages-instellingen van de repository. Ga terug naar _Settings > Pages_ en voeg je aangepaste domein toe in het tekstveld in het gedeelte _Custom Domain_.

![Voeg aangepast domein toe in GitHub Pages-instellingen](https://xebia.com/wp-content/uploads/2024/01/add-custom-domain-to-github-pages@3x-1024x569.png)

## Verifieer en beveilig je aangepaste domein

Het is mogelijk dat je domein kan worden overgenomen of misbruikt terwijl GitHub Pages is uitgeschakeld. Om te voorkomen dat andere GitHub-gebruikers je domein gebruiken met hun pagina-configuraties, biedt GitHub een verificatie voor je aangepaste domeinen.

Open je persoonlijke pagina-instellingen via _Avatar > Settings > Pages_ en voeg je domein toe. GitHub geeft `TXT`-recordinstellingen die je moet toevoegen aan de DNS-instellingen van je domein.

![Verificatiegegevens voor aangepast domein gebruikt met GitHub Pages](https://xebia.com/wp-content/uploads/2024/01/verify-custom-domain-for-github-pages@3x-1024x479.jpg)

Zodra je DNS-instellingen live zijn, kun je op _Verify_ klikken. Als de verificatie slaagt, wordt het domein respectievelijk vermeld en is het beveiligd.

![Geverifieerd aangepast domein gebruikt met GitHub Pages](https://xebia.com/wp-content/uploads/2024/01/verify-custom-domain-for-github-pages-verified@3x-1024x298.png)

Dat is het - je bent klaar, je site is live en het domein is beveiligd! 🥳