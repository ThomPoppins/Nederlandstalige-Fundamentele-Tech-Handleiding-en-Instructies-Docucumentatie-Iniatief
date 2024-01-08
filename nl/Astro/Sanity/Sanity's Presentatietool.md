Zeker! Hier is de vertaling naar het Nederlands in een mooi Markdown-format met emoji's:

# Gids voor het Integreren van Sanity's Presentatiegereedschap met Next.js 🚀

Ontworpen voor ontwikkelaars die van plan zijn Sanity's visuele bewerking te integreren in een frontend-toepassing met Next.js, biedt deze gids een gerichte, technische benadering voor naadloze integratie. Belangrijke gebieden die worden behandeld, zijn onder andere:

## Live Voorbeeldconfiguratie 🖥️

Instructies voor het configureren van een live voorbeeldfunctie in je Next.js-app, waardoor realtime inhoudsupdates en bewerkingen mogelijk zijn.

## Next.js en Sanity Integratie 🤝

Gedetailleerde verkenning van hoe Sanity te verbinden met een Next.js-toepassing voor efficiënte gegevensstroom en -beheer.

Deze gids biedt de nodige stappen voor ontwikkelaars om geavanceerde functies voor inhoudsbeheer effectief te integreren in hun toepassingen, waardoor de functionaliteit en gebruikerservaring worden verbeterd.

## Integratie van Sanity's Presentatiegereedschap met Next.js: Uitgebreide Gids 🌐

De wereld van webontwikkeling evolueert voortdurend, met nieuwe tools en technologieën die opkomen om het proces van contentcreatie en -beheer te optimaliseren. Eén zo'n gereedschap is het Sanity Presentatiegereedschap, een krachtige functie binnen het Sanity.io-ecosysteem die is ontworpen om de ervaring van het bewerken van inhoud te verbeteren. Dit gereedschap overbrugt de kloof tussen contentbeheer en frontend-presentatie, met een naadloze, real-time bewerkingsinterface die waardevol is voor zowel contentmakers als ontwikkelaars.

Hoewel er uitgebreide documentatie beschikbaar is, inclusief de `template-nextjs-personal-website`-repository met nuttige codevoorbeelden, heeft deze gids als doel informatie uit die bronnen samen te vatten om een gedetailleerde, praktische uitleg te bieden. De focus ligt op het demonstreren van hoe het Sanity Presentatiegereedschap te integreren in je bestaande Next.js-toepassing, waardoor je contentverwerking een meer dynamisch, interactief en visueel intuïtief proces wordt.

# Gids voor het Implementeren van Sanity's Presentatiegereedschap in je Workflow 🧰

Voor degenen die nieuw zijn met Sanity of het willen integreren in hun workflow, biedt deze gids een praktische benadering voor het implementeren van het Presentatiegereedschap. Het integreren van dit gereedschap in je systeem omvat twee essentiële componenten: het configureren van het Presentatiegereedschap aan de Sanity-kant met behulp van de sanity/presentation-tool en het inschakelen van live-bewerkingen en visuele overlays in je frontend-toepassing. In deze gids zullen we stap voor stap de stappen doorlopen om het Presentatiegereedschap in te schakelen in een Next.js-app, met de nadruk op het frontend aspect. Voor degenen die geïnteresseerd zijn in de implementatie aan de Sanity-kant, raad ik aan ons artikel "Een Diepe Duik in de Visuele Bewerking en het Presentatiegereedschap van Sanity: Het ontwikkelaarsperspectief" te bekijken, dat een uitgebreid overzicht en praktische configuratievoorbeelden biedt. Bovendien kun je alle codevoorbeelden uit dit artikel in actie zien in ons demoproject, dat alle nieuwe functies van het Presentatiegereedschap laat zien.

## Begrip van het Presentatiegereedschap​ 🎨

Voordat we in de implementatie duiken, is het cruciaal om te begrijpen wat het Sanity Presentatiegereedschap is en hoe het de ervaring van het bewerken van inhoud verbetert. Hier gaan we ervan uit dat je al bekend bent met het Presentatiegereedschap en zullen we ons meer richten op praktische aspecten. Als je nieuw bent met het Presentatiegereedschap, raad ik aan ons vorige artikel te lezen voor een gedetailleerde introductie.

# Implementatie Stappen: Sanity Presentatiegereedschap in Next.js 🚀

Laten we nu verder gaan met de stappen voor het implementeren van het Sanity Presentatiegereedschap in een Next.js-applicatie.

## 1. Configuratie aan de Sanity-kant 🛠️

Begin met het configureren van het Presentatiegereedschap aan de Sanity-kant met behulp van de `sanity/presentation-tool`. Volg de instructies om de juiste instellingen te configureren en ervoor te zorgen dat de tool is aangepast aan je specifieke behoeften.

```bash
# Installeer de sanity/presentation-tool
npm install -g @sanity/presentation-tool

# Start de configuratie
sanity presentation configure
```

## 2. Inschakelen van Live-Bewerkingen in de Frontend 📡

Om live-bewerkingen in je frontend-toepassing mogelijk te maken, volg je deze stappen:

- Voeg de nodige scripts toe aan je HTML-bestand.
  
  ```html
  <script src="https://cdn.sanity.io/present/latest.js"></script>
  <script async defer src="https://cdn.sanity.io/overlay/latest.js"></script>
  ```

- Integreer de live-bewerkingsfunctionaliteit in je app.
  
  ```javascript
  // Voeg onderstaande code toe aan je Next.js-app
  import dynamic from 'next/dynamic';

  const PresentationOverlay = dynamic(() => import('@sanity/presentation-overlay'));

  const MyApp = ({ Component, pageProps }) => (
    <>
      <Component {...pageProps} />
      <PresentationOverlay />
    </>
  );

  export default MyApp;
  ```

Nu ben je klaar om het Sanity Presentatiegereedschap in je Next.js-app te gebruiken! Raadpleeg onze demo-projectrepository voor praktische voorbeelden en bekijk de visuele verbeteringen in actie.

## Begrijp je het Presentatiegereedschap​

Hopelijk biedt deze gids een helder inzicht in de praktische implementatie van het Sanity Presentatiegereedschap in je workflow. Als je verdere details wilt over de werking van het gereedschap, bekijk dan onze eerdere artikelen voor een diepgaand begrip.

Veel succes en geniet van de verbeterde contentbewerking met Sanity's Presentatiegereedschap! 🎉

# Verdere Verdieping: Begrijpen van het Presentatiegereedschap 🕵️‍♂️

Voordat we dieper ingaan op de implementatie, laten we ons richten op een beter begrip van het Sanity Presentatiegereedschap en hoe het de ervaring van het bewerken van inhoud transformeert.

## Wat is het Sanity Presentatiegereedschap? 🤔

Het Sanity Presentatiegereedschap is een krachtige functie binnen het Sanity.io-ecosysteem die is ontworpen om de contentbewerking naar een hoger niveau te tillen. Het fungeert als een brug tussen contentbeheer aan de backend-kant en de frontend-presentatie, waardoor realtime bewerkingen en visuele overlays mogelijk zijn.

### Voordelen van het Presentatiegereedschap ✨
- **Realtime Bewerkingen:** Maakt directe wijzigingen in de inhoud mogelijk, waardoor contentmakers efficiënter kunnen werken.
- **Visuele Overlays:** Biedt een intuïtieve interface voor het bewerken van content, waardoor gebruikers direct feedback krijgen.

## Praktische Aspecten van Implementatie 🛠️

Terug naar de implementatie in je Next.js-applicatie. Na het configureren aan de Sanity-kant en het inschakelen van live-bewerkingen in de frontend, kun je nu profiteren van de volgende praktische aspecten:

- **Configuratie Aanpassingen:** Pas de configuratie van het Presentatiegereedschap aan je specifieke behoeften aan door het volgen van de sanity/presentation-tool instructies.

- **Dynamische Integratie:** De dynamische integratie van het PresentationOverlay-component in je Next.js-app zorgt voor een naadloze ervaring zonder pre-rendering complicaties.

## Volgende Stappen en Bronnen 📚

Als je verder wilt gaan met het verbeteren van je contentbewerkingsworkflow, bekijk dan onze eerdere artikelen, zoals "Een Diepe Duik in de Visuele Bewerking en het Presentatiegereedschap van Sanity: Het ontwikkelaarsperspectief". Hierin vind je gedetailleerde configuratievoorbeelden en een diepgaand begrip van de tool.

Veel succes bij het integreren en geniet van een geoptimaliseerde contentbewerking met het Sanity Presentatiegereedschap! 🚀

# De Essentie van het Presentatiegereedschap 🎥

De kern van de functionaliteit van het Presentatiegereedschap ligt in zijn vermogen om een live, interactieve voorvertoning van inhoud te bieden. Deze functie stelt contentmakers in staat om inhoud te zien en te bewerken in een opmaak die sterk lijkt op de uiteindelijke presentatie op de frontend. Een dergelijke realtime feedback is onschatbaar bij het creëren van een efficiëntere en foutloze bewerkingsworkflow.

Verschillende kerntechnologieën vormen de basis van dit gereedschap:

- **@vercel/stega:** Een technologie die wordt gebruikt voor het coderen van metadata binnen tekstreeksen. Deze codering is noodzakelijk voor het koppelen van frontend-content aan de bijbehorende bewerkbare segmenten in het CMS.
  
- **@sanity/client/stega:** Integreert Stega met de Sanity-client en zorgt voor communicatie tussen je contentbeheersysteem en frontend.
  
- **@sanity/react-loader:** Vergemakkelijkt het ophalen en streamen van gegevens in je applicatie en speelt een sleutelrol in het beheren van de inhoudsstroom en realtime updates.
  
- **@sanity/overlays:** Creëert een visuele bewerkingsinterface op de frontend, waardoor gebruikers rechtstreeks op de inhoud kunnen klikken en bewerken.

In de volgende secties zullen we verkennen hoe deze technologieën geïntegreerd kunnen worden in een bestaande Next.js-toepassing om optimaal gebruik te maken van de mogelijkheden van het Sanity Presentatiegereedschap.

## Implementatie Roadmap​ 🗺️

Het integreren van het Sanity Presentatiegereedschap in een Next.js-toepassing vereist een strategische aanpak. Deze sectie schetst de roadmap die we zullen volgen om de volledige functionaliteit van het Presentatiegereedschap in je bestaande Next.js-app mogelijk te maken. Door het proces op te splitsen in beheersbare stappen, streven we ernaar om een duidelijke en beknopte handleiding te bieden die gemakkelijk te volgen is, ongeacht je ervaringsniveau.

1. **Opzetten van de omgeving:** Zorg ervoor dat je ontwikkelingsomgeving klaar is voor integratie. Dit omvat het hebben van de nieuwste versie van Next.js geïnstalleerd en je Sanity Studio opgezet.

2. **Installatie van vereiste pakketten:** We zullen de noodzakelijke pakketten behandelen die moeten worden geïnstalleerd in je Next.js-toepassing om het Presentatiegereedschap te ondersteunen. Dit omvat de Sanity-client en specifieke pakketten zoals @sanity/react-loader en @sanity/overlays.

3. **Configuratie van loaders:** Loaders spelen een cruciale rol bij het ophalen en renderen van inhoud. We zullen ingaan op de configuratie van loaders, hun belang bespreken en laten zien hoe je ze effectief kunt gebruiken in je toepassing.

4. **Inschakelen van overlays:** Overlays bieden de visuele interface voor het direct bewerken van inhoud vanuit de voorvertoning. We zullen je begeleiden bij het proces om ze in je toepassing in te schakelen.

5. **Live-modus en realtime voorvertoning:** Een cruciale functie van het Presentatiegereedschap is de realtime voorvertoning. We zullen verkennen hoe je deze live modus kunt inschakelen en optimaal kunt benutten voor onmiddellijke inhoudsupdates.

6. **Laatste aanpassingen:** Zodra alle componenten op hun plaats zijn, zullen we het proces doornemen om de integratie af te stemmen en te testen om ervoor te zorgen dat alles zoals verwacht werkt.

## Initiële Configuratie​ 🛠️

Voordat je het Sanity Presentatiegereedschap integreert in je Next.js-toepassing, is het essentieel om ervoor te zorgen dat je omgeving up-to-date is en alle benodigde componenten heeft. Deze initiële configuratie legt het fundament voor een soepel integratieproces.

# Omgevingsconfiguratie 🌐

Voordat we duiken in de integratie van het Sanity Presentatiegereedschap, is het cruciaal om ervoor te zorgen dat je ontwikkelingsomgeving klaar is voor deze implementatie.

1. **Update Next.js en Sanity Studio:** Zorg ervoor dat je de nieuwste versie van Next.js hebt geïnstalleerd en dat je Sanity Studio is geconfigureerd en operationeel is.

2. **Projectinitialisatie:** Als je nog geen Next.js-project hebt, kun je er een starten met behulp van het volgende commando:

    ```bash
    npx create-next-app my-sanity-app
    ```

    Navigeer naar de projectmap:

    ```bash
    cd my-sanity-app
    ```

3. **Installatie van Sanity CLI:** Installeer de Sanity CLI globaal als je dat nog niet hebt gedaan:

    ```bash
    npm install -g @sanity/cli
    ```

    Initialiseer een nieuw Sanity-project:

    ```bash
    sanity init
    ```

    Volg de instructies om je project te configureren.

Nu je ontwikkelingsomgeving is ingesteld, kunnen we doorgaan met de installatie van de benodigde pakketten voor het Presentatiegereedschap.

# Installatie van Vereiste Pakketten 📦

Om het Sanity Presentatiegereedschap te ondersteunen, moeten we enkele essentiële pakketten installeren in je Next.js-toepassing.

1. **Sanity Client:** Installeer de Sanity client die communicatie mogelijk maakt tussen je frontend en het CMS.

    ```bash
    npm install @sanity/client
    ```

2. **Sanity React Loader:** Voeg de loader toe voor het ophalen en streamen van gegevens in je toepassing.

    ```bash
    npm install @sanity/react-loader
    ```

3. **Sanity Overlays:** Installeer het pakket voor visuele bewerkingsinterfaces op de frontend.

    ```bash
    npm install @sanity/overlays
    ```

Nu je deze pakketten hebt geïnstalleerd, zijn we klaar om verder te gaan met de configuratie van loaders.

# Configuratie van Loaders 🔄

Loaders spelen een essentiële rol bij het ophalen en renderen van inhoud in je Next.js-applicatie. We gaan nu in op de configuratie van deze loaders.

1. Maak een nieuw bestand `sanity.js` aan in de root van je project en voeg de Sanity client-configuratie toe:

    ```javascript
    // sanity.js
    import sanityClient from '@sanity/client';

    export default sanityClient({
      projectId: 'jouw-project-id',
      dataset: 'jouw-dataset',
      useCdn: true, // Aanbevolen voor productie
    });
    ```

    Vervang `'jouw-project-id'` en `'jouw-dataset'` met de juiste waarden voor jouw Sanity-project.

2. Gebruik de configuratie in je Next.js-toepassing waar je de Sanity-data nodig hebt. Bijvoorbeeld in een pagina of component:

    ```javascript
    // pages/index.js
    import { useNextSanityImage } from 'next-sanity-image';
    import sanity from '../sanity';

    const IndexPage = ({ data }) => {
      // Gebruik de data zoals nodig
    };

    export const getStaticProps = async () => {
      const data = await sanity.fetch('...'); // Voeg hier je query toe

      return {
        props: {
          data,
        },
      };
    };

    export default IndexPage;
    ```

Met deze configuratie zijn we klaar om over te gaan naar het inschakelen van overlays voor visuele bewerkingen op de frontend.

# Inschakelen van Overlays 🖌️

Nu we de basisconfiguratie hebben voltooid, is het tijd om overlays in te schakelen. Overlays bieden een visuele interface waarmee gebruikers rechtstreeks op de inhoud kunnen klikken en bewerken.

1. Voeg de benodigde scripts toe aan je HTML-bestand om overlays mogelijk te maken:

    ```html
    <!-- public/index.html -->
    <script src="https://cdn.sanity.io/overlays/1.0.0-beta.1/overlays.js"></script>
    ```

2. Implementeer het gebruik van overlays in je Next.js-applicatie. Voeg het volgende toe aan je pagina of component:

    ```javascript
    // pages/index.js
    import React from 'react';
    import sanity from '../sanity';

    const IndexPage = ({ data }) => {
      // Gebruik de data zoals nodig

      const handleEdit = () => {
        sanity.actions.editDocument(data._id);
      };

      return (
        <div>
          {/* Jouw content hier */}

          <button onClick={handleEdit}>Bewerk deze inhoud</button>
        </div>
      );
    };

    export const getStaticProps = async () => {
      const data = await sanity.fetch('...'); // Voeg hier je query toe

      return {
        props: {
          data,
        },
      };
    };

    export default IndexPage;
    ```

    Hier voegen we een eenvoudige knop toe waarmee je de bewerkingsmodus kunt starten voor de huidige inhoud. Pas dit aan op basis van je specifieke gebruiksscenario.

# Live-Modus en Realtime Voorvertoning 🚀

Een cruciale functie van het Presentatiegereedschap is de mogelijkheid om real-time voorvertoningen van inhoud aan te bieden. Laten we deze functionaliteit inschakelen.

1. Voeg het live-modus script toe aan je HTML-bestand:

    ```html
    <!-- public/index.html -->
    <script src="https://cdn.sanity.io/present/1.0.0-beta.2/present.js"></script>
    ```

2. Gebruik de live-modus in je Next.js-applicatie. Bijvoorbeeld:

    ```javascript
    // pages/index.js
    import React from 'react';
    import sanity from '../sanity';

    const IndexPage = ({ data }) => {
      // Gebruik de data zoals nodig

      return (
        <div>
          {/* Jouw content hier */}

          <script
            dangerouslySetInnerHTML={{
              __html: `window.sanityStudio = ${JSON.stringify(sanity.config())}`,
            }}
          />
        </div>
      );
    };

    export const getStaticProps = async () => {
      const data = await sanity.fetch('...'); // Voeg hier je query toe

      return {
        props: {
          data,
        },
      };
    };

    export default IndexPage;
    ```

    Dit zorgt ervoor dat je content wordt weergegeven in de live-modus zoals deze op de frontend verschijnt.

# Laatste Aanrakingen en Testen ✅

Nu je de basisfunctionaliteit hebt geïmplementeerd, is het tijd voor de laatste aanrakingen en testen:

- **Fine-tuning:** Pas de implementatie aan op basis van je specifieke vereisten. Zorg ervoor dat overlays en live-modus soepel werken.

- **Uitgebreide testen:** Test de integratie grondig om ervoor te zorgen dat alle componenten correct werken. Controleer bewerkingen in de live-modus en overlays.

Met deze laatste stappen heb je het Sanity Presentatiegereedschap volledig geïntegreerd in je Next.js-applicatie. Geniet van de verbeterde contentbewerking en de mogelijkheid om in realtime wijzigingen te zien! 🚀

# Afronding en Verdere Verkenning 🌐

Gefeliciteerd! Je hebt met succes het Sanity Presentatiegereedschap geïntegreerd in je Next.js-applicatie. Voordat we afsluiten, laten we enkele laatste opmerkingen delen en mogelijke verdere verkenningen verkennen.

## Finetuning en Aanpassingen 🎨

- **Visuele aanpassingen:** Pas de stijl en lay-out van de overlays aan om ze naadloos te integreren met de look en feel van je frontend.
  
- **Gebruiksvriendelijkheid:** Test de gebruikerservaring van het bewerken in realtime en pas het aan op basis van feedback en gebruiksgemak.

## Verder Ontdekken 🚀

- **Geavanceerde Configuraties:** Verken geavanceerde configuraties en aanpassingen die het Presentatiegereedschap biedt. Bekijk de officiële documentatie voor diepgaande details.

- **Integratie van Aanvullende Functionaliteiten:** Onderzoek hoe je aanvullende functionaliteiten kunt integreren, zoals het toevoegen van aangepaste plugins of het uitbreiden van de mogelijkheden van het gereedschap.

- **Community en Ondersteuning:** Doe mee aan de Sanity-community, deel je ervaringen en leer van anderen. Ontvang ondersteuning en ontdek nieuwe toepassingen van het Presentatiegereedschap.

## Volgende Stappen en Bronnen 📚

- **Lees de Documentatie:** Raadpleeg de officiële documentatie van Sanity voor gedetailleerde informatie over het Presentatiegereedschap en aanverwante functies.

- **Demo Project:** Bekijk het demo-project dat alle nieuwe functies van het Presentatiegereedschap laat zien. Experimenteer met de code en pas het aan voor je eigen behoeften.

# Bijwerken van Sanity en Next.js: 🔄

Zorg ervoor dat je zowel je Sanity Studio als je Next.js-toepassing bijwerkt naar de juiste versies om gebruik te maken van de nieuwste functies en verbeteringen.

1. **Sanity Studio bijwerken:**
   - Zorg ervoor dat je Sanity Studio is bijgewerkt naar versie 3.20 of hoger. Dit garandeert toegang tot de nieuwste functies die we in deze handleiding zullen gebruiken.

2. **Next.js bijwerken:**
   - Zorg ervoor dat je Next.js-toepassing draait op versie 18 of hoger. Deze update is nodig voor compatibiliteit en om te profiteren van de nieuwste functies en prestatieverbeteringen van Next.js.

3. **Installatie van vereiste pakketten:**
   - Met je omgeving up-to-date, ga je verder met het installeren van de benodigde pakketten. Gebruik de volgende opdrachten in je terminal om deze pakketten te installeren:

    ```bash
    npm install @sanity/client @sanity/react-loader @sanity/overlays
    ```

    Pas deze opdrachten indien nodig aan voor je favoriete pakketbeheerder, zoals Yarn.

Met deze initiële configuratiestappen is je toepassing goed voorbereid op de volgende fasen van het integreren van het Sanity Presentatiegereedschap.

# Configuratie van Loaders 🚛

Loaders bieden een uniforme methode voor het laden van gegevens uit het Sanity Content Lake, wat zorgt voor consistentie tussen verschillende staten (productie, ontwikkeling en voorbeeldweergave) en renderingsmodi (server- en clientzijde). Ze zijn essentieel voor het implementeren van visuele bewerkingsmogelijkheden, waardoor functies zoals realtime voorvertoningen en klikbare overlays mogelijk zijn.

In deze sectie zullen we ingaan op het opzetten van loaders en hun praktische toepassingen. Sanity biedt loaders die zijn afgestemd op verschillende frameworks, wat zorgt voor compatibiliteit en eenvoudige integratie, ongeacht je specifieke technologiestack. Voor deze handleiding richten we ons op het gebruik van de React Loader. De besproken technieken kunnen echter worden aangepast aan andere frameworks - raadpleeg de documentatie voor begeleiding binnen jouw framework.

# Bijwerken van Sanity Client met Stega-ondersteuning 🔄

Leg een verbinding tussen je Next.js-toepassing en je Sanity-project met behulp van het @sanity/client-pakket. Configureer de client met de vereiste parameters zoals project-ID, dataset en API-versie.

```javascript
// sanity.js
import sanityClient from '@sanity/client';

export default sanityClient({
  projectId: 'jouw-project-id',
  dataset: 'jouw-dataset',
  useCdn: true, // Aanbevolen voor productie
});
```

Zorg ervoor dat je de juiste waarden invoert voor `'jouw-project-id'` en `'jouw-dataset'`. Deze configuratie is nodig voor verdere stappen in het integratieproces.

Met deze updates en configuraties ben je klaar voor de volgende stappen in het integreren van het Sanity Presentatiegereedschap.

# Implementeren van het Sanity Presentatiegereedschap in Next.js (Vervolg) 🚀

Met je omgeving up-to-date en de vereiste pakketten geïnstalleerd, gaan we nu verder met de implementatie van het Sanity Presentatiegereedschap in je Next.js-applicatie.

## 1. Integreren van het Presentatiegereedschap:

Voeg de scripts voor het Sanity Presentatiegereedschap toe aan je HTML-bestand:

```html
<!-- public/index.html -->
<script src="https://cdn.sanity.io/present/latest.js"></script>
<script async defer src="https://cdn.sanity.io/overlay/latest.js"></script>
```

Deze scripts zorgen voor de integratie van het presentatiegereedschap en de overlays in je applicatie.

## 2. Toevoegen van Functionaliteit:

Pas je pagina of component aan om gebruik te maken van het presentatiegereedschap. Hier is een voorbeeld:

```javascript
// pages/index.js
import React from 'react';
import sanity from '../sanity';

const IndexPage = ({ data }) => {
  const handleEdit = () => {
    sanity.actions.editDocument(data._id);
  };

  return (
    <div>
      {/* Je content hier */}

      <button onClick={handleEdit}>Bewerk deze inhoud</button>
    </div>
  );
};

export const getStaticProps = async () => {
  const data = await sanity.fetch('...'); // Voeg hier je query toe

  return {
    props: {
      data,
    },
  };
};

export default IndexPage;
```

De bovenstaande code voegt een knop toe waarmee je de bewerkingsmodus voor de huidige inhoud kunt starten. Pas dit aan op basis van je specifieke gebruiksscenario.

## 3. Live-modus en Realtime Voorvertoning:

Voeg het live-modus script toe aan je HTML-bestand:

```html
<!-- public/index.html -->
<script src="https://cdn.sanity.io/present/latest.js"></script>
```

Gebruik de live-modus in je Next.js-applicatie:

```javascript
// pages/index.js
import React from 'react';
import sanity from '../sanity';

const IndexPage = ({ data }) => {
  return (
    <div>
      {/* Je content hier */}

      <script
        dangerouslySetInnerHTML={{
          __html: `window.sanityStudio = ${JSON.stringify(sanity.config())}`,
        }}
      />
    </div>
  );
};

export const getStaticProps = async () => {
  const data = await sanity.fetch('...'); // Voeg hier je query toe

  return {
    props: {
      data,
    },
  };
};

export default IndexPage;
```

Dit zorgt ervoor dat je content wordt weergegeven in de live-modus zoals het op de frontend verschijnt.

## 4. Laatste Aanpassingen en Testen:

- **Fine-tuning:** Pas de implementatie aan op basis van je specifieke vereisten. Zorg ervoor dat overlays en live-modus soepel werken.

- **Uitgebreide testen:** Test de integratie grondig om ervoor te zorgen dat alle componenten correct werken. Controleer bewerkingen in de live-modus en overlays.

Met deze stappen heb je met succes het Sanity Presentatiegereedschap geïntegreerd in je Next.js-applicatie. Geniet van de verbeterde contentbewerking en de mogelijkheid om realtime wijzigingen te zien! 🎉

# Overschakelen naar @sanity/client/stega ⚙️

Als je momenteel @sanity/client of next-sanity gebruikt, moet je overschakelen naar @sanity/client/stega. Deze bijgewerkte client biedt ondersteuning voor Stega, wat essentieel is voor de interactieve en visuele functies van het Presentatiegereedschap. Het upgradeproces is eenvoudig; in de meeste gevallen hoef je alleen je importverklaring bij te werken en de stega-opties te configureren. Zo zou je bijvoorbeeld je bijgewerkte clientconfiguratie eruit moeten laten zien:

```typescript
// client.ts

import { createClient } from '@sanity/client/stega';

export const client = createClient({
  projectId: "<JOUW_SANITY_PROJECT_ID>",
  dataset: "<JOUW_SANITY_DATASET>",
  apiVersion: "<API_VERSIE>",
  useCdn: false, // We vertrouwen op de Next.js-cache
  perspective: 'published',
  stega: {
    studioUrl: "<SANITY_STUDIO_URL>",
  },
});
```

# Aanmaken van een QueryStore ​🔍

Begin met het opzetten van een query store met behulp van de `createQueryStore`-functie van `@sanity/react-loader`. Deze store beheert het ophalen en streamen van gegevens in je applicatie en bevat essentiële hulpprogramma's zoals `useQuery`, `loadQuery` en `useLiveMode`, elk met een specifieke functie:

- `useQuery` react-hook voor het laden en streamen van gegevens aan de clientzijde.
- `loadQuery` wordt voornamelijk gebruikt voor server-side rendering (SSR) om inhoudsgegevens op te halen.
- `useLiveMode` activeert real-time updates, zodat wijzigingen in Sanity onmiddellijk worden weerspiegeld in je applicatie.

```typescript
// queryStore.ts

import { createQueryStore } from '@sanity/react-loader/rsc';

// De `queryStore`-instantie wordt gedeeld in RSC- en clientcomponenten, houd dit bestand klein omdat het in de client-bundel zal worden opgenomen.
export const queryStore = createQueryStore({
  client: false,
  ssr: true,
});
```

# Opzetten van een Wrapper voor LoadQuery​ 📦

Om de functionaliteit van `loadQuery` uit te breiden en specifieke behoeften zoals consistentie tussen server en client en effectieve cachingstrategieën te behandelen, creëren we een aangepaste wrapper rond deze functie. We zullen ook ondersteuning integreren voor de conceptmodus, zodat het dynamisch reageert op verschillende inhoudsstaten in je applicatie.

```typescript
// Throw error if this file will be imported on the client side
import 'server-only';

import { draftMode } from 'next/headers';

import { client } from './client';
import { queryStore } from './queryStore';

// Configuratie van een aparte client voor server-side gebruik, met Stega ingeschakeld in niet-productieomgevingen
const serverClient = client.withConfig({
  stega: {
    enabled: process.env.NODE_ENV !== 'production',
  },
});

// Instellen van de server-client in de query store voor consistente server-client gegevensverwerking
queryStore.setServerClient(serverClient);

// Aangepaste wrapperfunctie voor `queryStore.loadQuery` om conceptmodus af te handelen en configuratie op één plek te houden
export const loadQuery = ((query, params = {}, options = {}) => {
  return queryStore.loadQuery(query, params, {
    cache: 'force-cache',
    perspective: draftMode().isEnabled ? 'previewDrafts' : 'published',
    ...options,
  });
}) satisfies typeof queryStore.loadQuery;
```

# Opzetten van een Wrapper voor UseQuery​ 🎣

Het creëren van een aangepaste wrapper rond de `useQuery`-hook is een effectieve manier om de functionaliteit uit te breiden en aan te passen aan de specifieke behoeften van je applicatie. Deze wrapper kan extra taken afhandelen zoals het coderen van gegevensattributen voor overlays en consistent beheer van fouten. Hier lees je hoe je dit kunt opzetten:

```typescript
// useQuery.ts

import {
  type QueryParams,
  useEncodeDataAttribute,
  type UseQueryOptions,
} from '@sanity/react-loader/rsc';

import { queryStore } from './createQueryStore';

// Aangepaste hook voor `queryStore.useQuery` om het gebruik van `encodeDataAttribute` te vereenvoudigen
export const useQuery = <
  QueryResponseResult = unknown,
  QueryResponseError = unknown,
>(
  query: string,
  params?: QueryParams,
  options?: UseQueryOptions<QueryResponseResult>,
) => {
  const snapshot = queryStore.useQuery<QueryResponseResult, QueryResponseError>(
    query,
    params,
    options,
  );

  // Genereer gegevensattributen voor overlays met behulp van de gegevens van Sanity
  const encodeDataAttribute = useEncodeDataAttribute(
    snapshot.data,
    snapshot.sourceMap,
    '<JOUW_STUDIO_URL>',  // Vervang dit door je Sanity Studio URL
  );

  // Consistent foutbeheer door eventuele gevangen fouten te gooien
  if (snapshot.error) {
    throw snapshot.error;
  }

  // Geef de queryresultaten terug samen met de `encodeDataAttribute`-functie
  return {
    ...snapshot,
    encodeDataAttribute,
  };
};

// Exporteer `useLiveMode` om real-time updates in de `VisualEditing`-component mogelijk te maken
export const { useLiveMode } = queryStore;
```

Met gegevens van `queryStore.useQuery` retourneert onze hook ook de `encodeDataAttribute`-functie. Deze functie wordt gebruikt om de nodige gegevens te maken voor het `data-sanity`-attribuut, waar we later in meer detail op ingaan.

# Implementatie van Loaders in Componenten​ 🚀

Integreer Loaders in je Next.js-componenten met behulp van de `useQuery`- en `loadQuery`-hooks. Gebruik voor op serverzijde gerenderde pagina's `loadQuery` om de initiële gegevens op te halen. Voor dynamische, aan de clientzijde interacties is `useQuery` je go-to hook. Dit zorgt ervoor dat je componenten altijd up-to-date inhoud van Sanity weergeven.

# Maken van een Voorbeeldcomponent voor Next.js-routes​ 🎨

Begin met het ontwikkelen van een client-side component die is bedoeld om alleen te laden wanneer de conceptmod

us is ingeschakeld. Het doel van deze component is om de meest recente of 'verse' gegevens op te halen en door te geven aan je pagina, zodat de inhoud die wordt bewerkt up-to-date is met de laatste wijzigingen die zijn aangebracht in de Sanity Studio.

```typescript
// 'use client'

import { type QueryResponseInitial } from '@sanity/react-loader/rsc';

import Page from './Page';
import { useQuery } from './useQuery';

type Props = {
  params: { slug: string };
  initial: QueryResponseInitial<PagePayload | null>;
};

export default function PagePreview(props: Props) {
  const { params, initial } = props;
  // Gebruik de `useQuery`-hook om de meest recente gegevens op te halen op basis van de pagina-slug
  const { data } = useQuery<'YOUR_PAGE_PAYLOAD_TYPE' | null>('<YOUR_GROQ_QUERY>', params, {
    initial,
  });

  return <Page data={data!} />;
}
```

# Gebruik van de Voorbeeldcomponent

Met de voorbeeldcomponent ingesteld, laten we deze nu integreren in een Next.js-pagina:

```typescript
import dynamic from 'next/dynamic';
import { draftMode } from 'next/headers';
import { notFound } from 'next/navigation';

import { Page } from './Page';
import { loadQuery } from './loadQuery';

// 1. Laad de Preview-component lui voor prestatieoptimalisatie
const PagePreview = dynamic(() => import('./PagePreview'));

type Props = {
  params: { slug: string };
};

export default async function PageRoute({ params }: Props) {
  // 2. Haal initiële gegevens op voor de pagina
  const initial = await loadQuery(params.slug);

  // 3. Toon de Preview-component in conceptmodus met initiële gegevens
  if (draftMode().isEnabled) {
    return <PagePreview params={params} initial={initial} />;
  }

  // Behandel scenario waarin de pagina niet is gevonden
  if (!initial.data) {
    return notFound();
  }

  // Render de standaardpagina met opgehaalde gegevens
  return <Page data={initial.data} />;
}
```

- Dynamisch laden: De PagePreview-component wordt dynamisch geïmporteerd met behulp van de dynamic-functie. Deze aanpak optimaliseert de prestaties door de component alleen te laden wanneer dat nodig is, specifiek in conceptmodus voor inhoudsbewerking.
- Server-side gegevens ophalen: De loadQuery-functie haalt initiële gegevens op. Afhankelijk van de modus (concept of productie) levert het de juiste gegevens aan ofwel de voorbeeld- of de standaardpagina-component.
- Controle op conceptmodus: Het gebruik van draftMode().isEnabled zorgt ervoor dat VisualEditing alleen wordt weergegeven wanneer de applicatie in conceptmodus staat. Dit is cruciaal voor het behoud van prestaties en gebruikerservaring in de productieomgeving.
# Gebruik van UseQuery in Productie​ 🚢

Hoewel de `useQuery`-functie primair wordt gebruikt in de context van bewerken en ontwikkelen, is het de moeite waard op te merken dat deze ook kan worden gebruikt in een productieomgeving. Het gebruik van `useQuery` in productie maakt het mogelijk om zeer dynamische componenten te maken. Dit is echter een zeldzamere use case, omdat het realtime updates en gegevensstreaming omvat.

```typescript
// 'use client';

import { useQuery } from './useQuery';

export function DocumentCount() {
  const { data, loading } = useQuery<number>('count(*)');

  if (loading) {
    return <div>Loading…</div>;
  }

  return <div>Total aantal documenten: {data}</div>;
}
```

Door deze stappen zorgvuldig te implementeren, zorg je ervoor dat je Next.js-toepassing niet alleen efficiënt inhoud beheert in zowel productie- als conceptmodi, maar ook het volledige potentieel benut van de real-time bewerkingsfuncties van Sanity.

# Inschakelen van Overlays​ 🌈

Met de Loaders ingesteld, is de volgende cruciale stap bij het integreren van het Sanity Presentatiegereedschap in je Next.js-toepassing het implementeren van overlays. Ze verschijnen als klikbare visuele indicatoren aan de frontend, waardoor inhoudmakers rechtstreeks naar bewerkbare elementen worden geleid. Wanneer op een overlay wordt geklikt, geeft dit een signaal naar de Sanity Studio om het overeenkomstige veld te openen voor bewerking, zelfs als het diep genest is binnen de documentstructuur.

# Implementatie van Overlays in Next.js 🎨

## Stap 1: Maak de VisualEditing Component

Begin met het maken van een `VisualEditing`-component. Deze component zal de `useLiveMode`-hook van `@sanity/react-loader` en de `enableOverlays`-functie van `@sanity/overlays` bevatten:

```jsx
// 'use client'

import { enableOverlays } from '@sanity/overlays';
import { useEffect } from 'react';

import { client } from './client';
import { useLiveMode } from './useQuery';

// Configureer de client om altijd Stega te gebruiken in Live Mode
const stegaClient = client.withConfig({ stega: true });

// Stel de toegestane studio-origin in, standaard naar localhost in een niet-browseromgeving
const allowStudioOrigin =
  typeof location === 'undefined' ? 'http://localhost:3000' : location.origin;

export default function VisualEditing() {
  useEffect(() => {
    // Schakel overlays in en configureer een opruimfunctie
    const disable = enableOverlays({ allowStudioOrigin });

    return () => disable();
  }, []);

  // Activeer live-modusupdates met behulp van de geconfigureerde client
  useLiveMode({ allowStudioOrigin, client: stegaClient });

  return null;
}
```

## Stap 2: Integreer de VisualEditing Component

Integreer de `VisualEditing`-component in je Next.js-pagina's om overlays mogelijk te maken. Voeg deze component toe aan het bovenste niveau van je pagina. Hier is een voorbeeld van hoe je dit kunt doen:

```jsx
// pages/_app.js

import VisualEditing from '../path/to/VisualEditing';

function MyApp({ Component, pageProps }) {
  return (
    <>
      <VisualEditing />
      <Component {...pageProps} />
    </>
  );
}

export default MyApp;
```

Nu is je Next.js-applicatie klaar om overlays te ondersteunen voor real-time bewerking in de Sanity Studio.

## Stap 3: Implementeer Overlays in Componenten

Nu kun je overlays implementeren in specifieke componenten waar je realtime bewerking wilt toestaan. Gebruik de `data-sanity`-attributen om de bewerkbare elementen aan te duiden. Hier is een voorbeeld:

```jsx
// Voorbeeldcomponent met Overlay-ondersteuning

import React from 'react';

const EditableComponent = ({ content }) => {
  return (
    <div data-sanity-id={content._id} data-sanity-type={content._type}>
      <h2>{content.title}</h2>
      <p>{content.body}</p>
    </div>
  );
};

export default EditableComponent;
```

In dit voorbeeld wordt de `data-sanity-id` en `data-sanity-type` gebruikt om het specifieke document en het type aan te duiden. Deze attributen worden door de overlays gebruikt om te weten welk deel van de content bewerkbaar is.

Met deze implementatie kun je nu genieten van overlays in je Next.js-applicatie, waardoor contentmakers direct en eenvoudig de inhoud kunnen bewerken vanuit de frontend met behulp van het Sanity Presentatiegereedschap. Veel succes met het verbeteren van de contentbewerkingservaring in je applicatie! 🚀

# Stap 7: Implementatie van Overlays in React-componenten

Nu je de basisstappen hebt gevolgd om overlays op te zetten en dynamisch te importeren, is het tijd om overlays toe te voegen aan je React-componenten. In dit voorbeeld gaan we ervan uit dat je overlays wilt activeren voor specifieke interactieve elementen, zoals een `SvgIcon`.

```jsx
// SvgIcon.tsx
import { SVGProps } from 'react';

export const SvgIcon = (props: SVGProps<SVGSVGElement>) => {
  const { data, encodeDataAttribute } = useQuery<PagePayload | null>(
    pagesBySlugQuery,
    params,
    { initial }
  );

  // Genereer data-attributen voor overlays met behulp van de gegevens uit Sanity
  const encodeDataAttribute = useEncodeDataAttribute(
    data,
    '<JOUW_STUDIO_URL>', // Vervang door je Sanity Studio URL
  );

  // Consistente foutafhandeling door eventuele gevangen fouten te gooien
  if (snapshot.error) {
    throw snapshot.error;
  }

  // Geef de queryresultaten terug samen met de `encodeDataAttribute`-functie
  return {
    ...snapshot,
    encodeDataAttribute,
  };
}

// Importeer en gebruik de SvgIcon-component in je pagina
import { SvgIcon } from './SvgIcon';

export default function MyPage() {
  return (
    <div>
      <h1>Mijn Pagina</h1>
      <SvgIcon />
    </div>
  );
}
```

In dit voorbeeld wordt de `useEncodeDataAttribute`-functie gebruikt om de benodigde gegevens te genereren voor het `data-sanity`-attribuut, dat wordt gebruikt door overlays om het juiste veld in de CMS te openen.

# Stap 8: Live Bewerkingsmodus Activeren

Zorg ervoor dat je de `useLiveMode`-hook gebruikt om de live bewerkingsmodus te activeren. Dit is cruciaal om ervoor te zorgen dat eventuele wijzigingen die in de Sanity Studio worden aangebracht, onmiddellijk worden weerspiegeld in de frontend-preview.

```jsx
// VisualEditing.tsx
import { enableOverlays } from '@sanity/overlays';
import { useLiveMode } from './useQuery';

export default function VisualEditing() {
  useEffect(() => {
    // Activeer overlays en stel een opruimfunctie in
    const disable = enableOverlays({ allowStudioOrigin });

    return () => disable();
  }, []);

  // Activeer live bewerkingsupdates met behulp van de geconfigureerde client
  useLiveMode({ allowStudioOrigin, client: stegaClient });

  return null;
}
```

Nu is je Next.js-applicatie klaar om overlays te gebruiken, waardoor je contentmakers een intuïtieve en visuele manier hebben om inhoud te bewerken met het Sanity Presentatiegereedschap. Vergeet niet om de aangepaste hooks en componenten te integreren in de rest van je applicatie waar je overlays nodig hebt. Happy coding! 🚀


# Stap 9: Navigatieverbeteringen binnen de Presentatietool

Om een soepele navigatie binnen de Sanity Presentatietool te waarborgen, gaan we een `HistoryAdapter` gebruiken. Deze adapter handhaaft synchronisatie tussen het voorbeeldpaneel van de studio en de routing- of geschiedenisstatus van je applicatie. Het beheert effectief navigatiegebeurtenissen en updates, zodat wijzigingen in de URL of status van je applicatie nauwkeurig worden weerspiegeld in de voorbeeldomgeving van de studio en vice versa.

```jsx
// VisualEditing.tsx
import { useRouter } from 'next/router';
import { usePathname, useSearchParams } from '@stefanprobst/next-history';
import { enableOverlays } from '@sanity/overlays';
import { useLiveMode } from './useQuery';

export default function VisualEditing() {
  const router = useRouter();
  const pathname = usePathname();
  const searchParams = useSearchParams();
  const routerRef = useRef(router);
  const navigateRef = useRef<HistoryAdapterNavigate>();

  routerRef.current = router;

  const history: HistoryAdapter = useMemo(
    () => ({
      // Functie abonneren om navigatiewijzigingen af te handelen
      subscribe(navigate) {
        navigateRef.current = navigate;
        return () => {
          navigateRef.current = undefined;
        };
      },

      // Update-functie om verschillende soorten geschiedenisupdates af te handelen
      update(update) {
        switch (update.type) {
          case 'push':
            return routerRef.current.push(update.url);
          case 'pop':
            return routerRef.current.back();
          case 'replace':
            return routerRef.current.replace(update.url);
          default:
            throw new Error(`Unknown update type: ${update.type}`);
        }
      },
    }),
    [],
  );

  useEffect(() => {
    const disable = enableOverlays({
      allowStudioOrigin,
      history,
    });
    return () => disable();
  }, []);

  // Update navigatiestatus wanneer pathname of zoekparameters veranderen
  useEffect(() => {
    navigateRef.current?.({
      type: 'push',
      url: `${pathname}${searchParams?.size ? `?${searchParams}` : ''}`,
    });
  }, [pathname, searchParams]);

  useLiveMode({ allowStudioOrigin, client: stegaClient });

  return null;
}
```

# Conclusie

Gefeliciteerd! Je hebt nu een volledig functionele integratie van het Sanity Presentatiegereedschap in je Next.js-toepassing. Deze integratie verbetert niet alleen de contentmanagementervaring, maar brengt ook een nieuw niveau van interactiviteit en efficiëntie in je workflow. Als je verdere vragen hebt of hulp nodig hebt bij andere aspecten van je project, aarzel dan niet om het te vragen. Happy coding! 🚀


# Terugblik op de Voordelen​

## Real-time Bewerken

De integratie van de Presentatie Tool biedt tal van voordelen:

**Real-time bewerken:** Contentmakers kunnen wijzigingen direct zien, waardoor het bewerkingsproces intuïtiever en efficiënter wordt.

**Visuele duidelijkheid:** Overlays bieden een duidelijke visuele indicatie van bewerkbare inhoud, waardoor contentbeheer wordt vereenvoudigd.

**Verbeterde gebruikerservaring:** De naadloze integratie tussen de frontend en het CMS verbetert de algehele gebruikerservaring, zowel voor contentmakers als ontwikkelaars.

# Aanmoediging tot Experimenteren

Met de basisinformatie en voorbeelden in deze handleiding moedigen we je aan verder te experimenteren. Elke Next.js-applicatie is uniek, en er zijn mogelijk aanvullende manieren om de Presentatie Tool aan te passen aan je specifieke behoeften. Voel je vrij om te experimenteren en de tools aan te passen aan de eisen van je project.

Als je behoefte hebt aan deskundig advies over Headless CMS en de nieuwste webtechnologieën, aarzel dan niet om contact met ons op te nemen.

# Verdere Ondersteuning Zoeken

Voor aanvullende bronnen of ondersteuning is het de moeite waard om de Sanity communityforums te verkennen of contact op te nemen met mede-ontwikkelaars. De open-source aard van deze tools betekent dat er een schat aan gedeelde kennis en ervaring beschikbaar is.

# Laatste Gedachten

Het integreren van de Sanity Presentatie Tool in je Next.js-applicatie is een belangrijke stap naar een meer dynamische en interactieve webontwikkelingservaring. In een steeds veranderend technologisch landschap is het essentieel om flexibel te blijven en open te staan voor nieuwe tools en methodologieën, wat ongetwijfeld ten goede zal komen aan je projecten en workflow.

We hopen dat deze handleiding waardevol is geweest in je streven om je Next.js-applicatie te verbeteren met de Sanity Presentatie Tool. Veel programmeerplezier!

**Sanity - Bouw opmerkelijke ervaringen op schaal**

Sanity Composable Content Cloud is de headless CMS waarmee je (en je team) een content backend hebt om websites en applicaties aan te sturen met moderne tools. Het biedt een realtime bewerkingsomgeving voor contentmakers die eenvoudig te configureren is maar ontworpen is om aangepast te worden met JavaScript en React wanneer dat nodig is. Met de gehoste documentopslag kun je content vrij bevragen en gemakkelijk integreren met elk framework of elke gegevensbron om content te distribueren en te verrijken.

Sanity is schaalbaar, van weekendprojecten tot zakelijke behoeften, en wordt gebruikt door bedrijven als Puma, AT&T, Burger King, Tata en Figma.
