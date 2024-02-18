Certainly! Here is the provided documentation translated to Dutch:

```markdown
# Astro op Vercel

Leer hoe je Vercel's functies kunt gebruiken met Astro. Astro is een alles-in-één webframework waarmee je performante statische websites kunt bouwen. Mensen kiezen voor Astro wanneer ze rijk aan content zijnde ervaringen willen creëren met zo min mogelijk JavaScript.

Je kunt een statische Astro-app naar Vercel implementeren zonder configuratie.

## Aan de slag met Astro op Vercel

Om aan de slag te gaan met Astro op Vercel:

1. Als je al een project hebt met Astro, installeer dan de Vercel CLI en voer het commando `vercel` uit vanuit de hoofdmap van je project.
2. Kloon een van onze Astro-voorbeeldrepositories naar je favoriete Git-provider en implementeer het op Vercel met de onderstaande knop:

   - [Implementeer onze Astro-sjabloon](#), of bekijk een live voorbeeld.
   - Of kies een sjabloon uit de marktplaats van Vercel.

## Gebruik van Vercel's functies met Astro

Om een servergerende Astro-app of een statische Astro-site te implementeren met Vercel-functies zoals Web Analytics en Image Optimization, volg je deze stappen:

1. Voeg de Astro Vercel-adapter toe aan je project met een van de volgende methoden:

   ```bash
   # Gebruik astro add (aanbevolen)
   pnpm astro add vercel
   ```

   Of installeer handmatig het pakket:

   ```bash
   pnpm i @astrojs/vercel
   ```

2. Configureer je project in `astro.config.ts`. Importeer de serverloze of statische plugin en stel de uitvoer in op server of statisch:

   ```typescript
   import { defineConfig } from 'astro/config';
   import vercelServerless from '@astrojs/vercel/serverless';

   export default defineConfig({
     output: 'server',
     adapter: vercelServerless(),
   });
   ```

3. Schakel de functies van Vercel in met behulp van de configuratieopties van Astro. Hier is een voorbeeld waarbij Web Analytics wordt ingeschakeld en een maximale duur voor Serverless Function-routes wordt ingesteld:

   ```typescript
   import { defineConfig } from 'astro/config';
   import vercel from '@astrojs/vercel/serverless';

   export default defineConfig({
     output: 'server',
     adapter: vercel({
       webAnalytics: {
         enabled: true,
       },
       maxDuration: 8,
     }),
   });
   ```

### Configuratieopties

De volgende configuratieopties schakelen de functies van Vercel in voor Astro-implementaties:

- `maxDuration`: (nummer, Serverless) - Verlengt of beperkt de maximale duur (in seconden) dat Serverless Functions kunnen draaien voordat ze time-out raken.
- `webAnalytics`: ({ enabled: boolean }, Statisch, Serverless) - Schakelt Web Analytics van Vercel in.
- `imageService`: (boolean, Statisch, Serverless) - Schakelt een automatisch geconfigureerde service in om je afbeeldingen te optimaliseren (voor Astro-versies 3 en hoger).
- `devImageService`: (string, Statisch, Serverless) - Configureert de imageservice die wordt gebruikt om je afbeeldingen te optimaliseren in je ontwikkelomgeving (voor Astro-versies 3 en hoger).
- `imagesConfig`: (VercelImageConfig, Statisch, Serverless) - Definieert het gedrag van de Image Optimization API, waardoor on-demand optimalisatie op runtime mogelijk is.
- `functionPerRoute`: (boolean, Serverless) - API-routes worden standaard gebundeld in één functie. Zet dit op true om elke route in afzonderlijke functies op te splitsen.
- `edgeMiddleware`: (boolean, Serverless) - Zet dit op true om Astro-middleware automatisch om te zetten naar Edge Middleware.
- `includeFiles`: (string[], Serverless) - Forceer bestanden om te worden gebundeld met je Serverless functies.
- `excludeFiles`: (string[], Serverless) - Sluit bestanden uit van bundeling met je Serverless functies. Ook beschikbaar met .vercelignore.

Voor meer details over de configuratieopties, zie [de documentatie van Astro](#).

## Server-Side Rendering

Het gebruik van SSR, of on-demand rendering zoals Astro het noemt, stelt je in staat om je routes als Serverless Functions op Vercel te implementeren. Hiermee kun je dynamische elementen aan je app toevoegen, zoals gebruikersaanmeldingen en gepersonaliseerde content.

Je kunt SSR inschakelen door de Vercel-adapter aan je project toe te voegen.

Als je Astro-project statisch wordt gerenderd, kun je individuele routes kiezen. Doe het volgende:

1. Stel je output-optie in op hybride in je `astro.config.ts`:

   ```typescript
   import { defineConfig } from 'astro/config';
   import vercel from '@astrojs/vercel/serverless';

   export default defineConfig({
     output: 'hybrid',
     adapter: vercel({
       edgeMiddleware: true,
     }),
   });
   ```



2. Voeg `export const prerender = false;` toe aan je componenten:

   ```typescript
   // src/pages/mypage.astro

   export const prerender = false;
   // ...
   ```

SSR met Astro op Vercel:

- Schalen naar nul wanneer niet in gebruik
- Schalen automatisch mee met toenemend verkeer
- Ondersteunt zero-configuratie voor Cache-Control headers, inclusief stale-while-revalidate
- Leer meer over [Astro SSR](#)

## Statische weergave

Statisch weergegeven of vooraf weergegeven Astro-apps kunnen zonder configuratie naar Vercel worden geïmplementeerd. Om Vercel-functies zoals Image Optimization of Web Analytics in te schakelen, zie [Het gebruik van Vercel's functies met Astro](#).

Je kunt individuele routes kiezen voor statische weergave met `export const prerender = true` zoals hieronder getoond:

```typescript
// src/pages/mypage.astro

export const prerender = true;
// ...
```

Statisch weergegeven Astro-sites op Vercel:

- Vereisen geen configuratie om te implementeren
- Kunnen Vercel-functies gebruiken met `astro.config.ts`
- Leer meer over [Astro Statische Weergave](#)

## Serverless Functions

Serverless Functions gebruiken resources die op- en afschalen op basis van verkeerseisen. Wanneer je SSR inschakelt met Astro's Vercel-adapter, worden standaard al je routes servergerend als Serverless Functions. Astro's Server Endpoints zijn de beste manier om Serverless API-routes te definiëren met Astro op Vercel.

Bij het definiëren van een Endpoint moet je elke functie de naam geven van de HTTP-methode die het vertegenwoordigt. Het volgende voorbeeld definieert basis-HTTP-methoden in een Server Endpoint:

```typescript
// src/pages/methods.json.ts

import { APIRoute } from 'astro/dist/@types/astro';

export const GET: APIRoute = ({ params, request }) => {
  return new Response(
    JSON.stringify({
      bericht: 'Dit was een GET!',
    }),
  );
};

export const POST: APIRoute = ({ request }) => {
  return new Response(
    JSON.stringify({
      bericht: 'Dit was een POST!',
    }),
  );
};

export const DELETE: APIRoute = ({ request }) => {
  return new Response(
    JSON.stringify({
      bericht: 'Dit was een DELETE!',
    }),
  );
};

// ALL komt overeen met elke methode die je niet hebt geïmplementeerd.
export const ALL: APIRoute = ({ request }) => {
  return new Response(
    JSON.stringify({
      bericht: `Dit was een ${request.method}!`,
    }),
  );
};
```

Serverless Functions met Astro op Vercel:

- Schalen naar nul wanneer niet in gebruik
- Schalen automatisch mee met toenemend verkeer
- Leer meer over [Serverless Functions](#)

## Edge Functions

Edge Functions zijn een snelle, schaalbare oplossing voor het leveren van dynamische inhoud aan gebruikers.

Standaard worden Edge Functions wereldwijd geïmplementeerd en worden ze aangeroepen in een van de Edge-regio's van Vercel bij de bezoekers van je site.

Astro ondersteunt momenteel Edge Functions niet van nature, maar je kunt de `/api`-map gebruiken om Edge Functions te definiëren met elk framework op Vercel. Zie de [Edge Functions snelstart](#) om aan de slag te gaan.

Edge Functions met Nuxt op Vercel:

- Bieden kostenbesparingen door minder middelen te gebruiken dan Serverless Functions
- Kunnen worden uitgevoerd in de regio die het dichtst bij je gebruikers of het dichtst bij de afhankelijkheden van gegevensbronnen ligt, op basis van je configuratie
- Hebben toegang tot de geolocatie en het IP-adres van bezoekers, waardoor locatiegebaseerde personalisatie mogelijk is
- Leer meer over [Edge Functions](#)

Hier is de vertaalde tekst:

```markdown
# Afbeeldingsoptimalisatie

Afbeeldingsoptimalisatie helpt u snellere paginaladingen te bereiken door de grootte van afbeeldingen te verminderen en moderne afbeeldingsformaten te gebruiken. Bij implementatie op Vercel worden afbeeldingen automatisch geoptimaliseerd op aanvraag, waardoor uw bouwtijden snel blijven terwijl de paginaprestaties en Core Web Vitals worden verbeterd.

Afbeeldingsoptimalisatie met Astro op Vercel wordt standaard ondersteund met Astro's Image-component. Zie de [Afbeeldingsoptimalisatie snelstart](#) voor meer informatie.

Afbeeldingsoptimalisatie met Astro op Vercel:

- Vereist geen configuratie voor afbeeldingsoptimalisatie bij gebruik van de Astro Image-component
- Helpt uw team om standaard uitstekende prestaties te garanderen
- Houdt uw bouwtijden snel door afbeeldingen on-demand te optimaliseren
- Meer informatie over [Afbeeldingsoptimalisatie](#)

# Middleware

Edge Middleware is code die wordt uitgevoerd voordat een verzoek op een site wordt verwerkt, waardoor u de respons kunt aanpassen. Omdat het vóór de cache wordt uitgevoerd, is Edge Middleware een effectieve manier om statisch gegenereerde inhoud te personaliseren.

Astro-middleware stelt u in staat om informatie in te stellen en te delen over uw eindpunten en pagina's met een `middleware.ts`-bestand in uw `src`-directory. Het volgende voorbeeld bewerkt het wereldwijde locals-object door gegevens toe te voegen die beschikbaar zullen zijn in elk `.astro`-bestand:

```typescript
// src/middleware.ts

// Deze helper typt middleware parameters automatisch
import { defineMiddleware } from 'astro:middleware';

export const onRequest = defineMiddleware(({ locals }, next) => {
  // onderschept gegevens van een verzoek
  // optioneel, wijzig de eigenschappen in `locals`
  locals.title = 'Nieuwe titel';

  // retourneer een Response of het resultaat van het oproepen van `next()`
  return next();
});
```

Astro-middleware is niet hetzelfde als Vercel Edge Middleware, die in de hoofdmap van uw project moet worden geplaatst, buiten `src`.

Om aangepaste eigenschappen aan locals toe te voegen in `middleware.ts`, moet u een wereldwijde namespace declareren in uw `env.d.ts`-bestand:

```typescript
// src/env.d.ts

declare namespace App {
  interface Locals {
    title?: string;
  }
}
```

U kunt vervolgens toegang krijgen tot de gegevens die u aan locals heeft toegevoegd in elk `.astro`-bestand, zoals hier:

```typescript
// src/pages/middleware-title.astro

---
const { title } = Astro.locals;
---
<h1>{title}</h1>
<p>De naam van deze pagina komt uit middleware.</p>
```

## Implementatie van middleware aan de rand

U kunt Astro's middleware aan de rand implementeren, zodat u toegang heeft tot gegevens in de RequestContext en Request en gebruik kunt maken van de Edge Middleware-helpers van Vercel, zoals `geolocation()` of `ipAddress()`.

Om Astro's middleware aan de rand te gebruiken, stelt u `edgeMiddleware: true` in in uw `astro.config.ts`-bestand:

```typescript
// astro.config.ts

import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel/serverless';

export default defineConfig({
  output: 'server',
  adapter: vercel({
    edgeMiddleware: true,
  }),
});
```

Als u Vercel's Edge Middleware gebruikt, hoeft u `edgeMiddleware: true` niet in te stellen in uw `astro.config.ts`-bestand.

Zie de [docs van Astro](#) voor de beperkingen en beperkingen bij het gebruik van middleware aan de rand, evenals hun probleemoplossingstips.

## Gebruik van Astro.locals in Edge Middleware

Het object `Astro.locals` maakt gegevens beschikbaar voor uw `.astro`-componenten, waardoor u uw inhoud dynamisch kunt aanpassen met middleware. Om wijzigingen aan te brengen in `Astro.locals` in de middleware van Astro aan de rand:

1. Voeg een nieuw middleware-bestand toe naast uw `src/middleware.ts` en noem het `src/vercel-edge-middleware.ts`. Deze bestandsnaam is vereist om wijzigingen aan `Astro.locals` aan te brengen. Als u `Astro.locals` niet wilt bijwerken, is deze stap niet vereist.

2. Retourneer een object met de eigenschappen die u aan `Astro.locals` wilt toevoegen.

   Voor TypeScript moet u het pakket `@vercel/edge` installeren:

   ```bash
   pnpm i @vercel/edge
   ```

   Typ vervolgens uw middleware-functie als volgt:

   ```typescript
   // src/vercel-edge-middleware.ts

   import type { RequestContext } from '@vercel/edge';

   // Let op: de parameters verschillen van standaard Astro-middleware
   export default function ({
     request,
     context,
   }: {
     request: Request;
     context: RequestContext;
   }) {
     // Retourneer een Astro.locals-object met een `title`-eigenschap
     return {
       title: "Blog van Spider-man",
     };
   }
   ```

## Gebruik van Vercel's Edge Middleware

De middleware van Astro, die in `src/middleware.ts` moet staan, verschilt van de Vercel Edge Middleware, die een `middleware.ts`-bestand moet zijn in de hoofdmap van uw project.

Vercel raadt aan om oplossingen die native zijn voor het framework

 te gebruiken. U zou de middleware van Astro moeten gebruiken in plaats van de Vercel Edge Middleware waar mogelijk.

Als u nog steeds Vercel's Edge Middleware wilt gebruiken, zie dan de [Quickstart](#) om te leren hoe.

# Herschrijvingen

Herschrijvingen werken alleen voor statische bestanden met Astro. U moet Vercel's Edge Middleware gebruiken voor herschrijvingen. U moet `vercel.json` niet gebruiken om URL-paden te herschrijven met Astro-projecten; dit leidt tot onvoorspelbaar gedrag en wordt niet officieel ondersteund.

# Doorverwijzingen

In het algemeen raadt Vercel aan om oplossingen te gebruiken die native zijn voor het framework, en Astro heeft ingebouwde ondersteuning voor doorverwijzingen. Dat gezegd hebbende, kunt u ook doorverwijzingen maken met Vercel's Edge Middleware.

## Doorverwijzingen in uw Astro-configuratie

U kunt doorverwijzingen maken met Astro in `astro.config.ts` met behulp van de `redirects`-configuratieoptie, zoals hieronder weergegeven:

```typescript
// astro.config.ts

import { defineConfig } from 'astro/config';

export default defineConfig({
  redirects: {
    '/oude-pagina': '/nieuwe-pagina',
  },
});
```

## Doorverwijzingen in Server Endpoints

U kunt ook een doorverwijzing retourneren vanuit een Server Endpoint met behulp van het `redirect`-hulpprogramma:

```typescript
// src/pages/links/[id].ts

export async function GET({ params, redirect }): APIRoute {
  return redirect('/omleidingspad', 307);
}
```

## Doorverwijzingen in componenten

U kunt doorverwijzen vanuit Astro-componenten met `Astro.redirect()`:

```typescript
// src/pages/account.astro

---
import { isLoggedIn } from '../utils';

const cookie = Astro.request.headers.get('cookie');

// Als de gebruiker niet is ingelogd, doorverwijzen naar de inlogpagina
if (!isLoggedIn(cookie)) {
  return Astro.redirect('/login');
}
---

<h1>Je kunt deze pagina alleen zien als je bent ingelogd</h1>
```

Zeker! Hier is de verstrekte documentatie opgemaakt in Markdown:

```markdown
# Serverless Functions

Serverless Functions maken gebruik van resources die op- en afschalen op basis van verkeersvraag. Dit maakt ze betrouwbaar tijdens piekuren en kostenefficiënt tijdens rustige perioden.

Wanneer u SSR inschakelt met de Vercel-adapter van Astro, worden al uw routes standaard server-side gerenderd als Serverless Functions. Astro's Server Endpoints zijn de beste manier om Serverless API-routes te definiëren met Astro op Vercel.

Bij het definiëren van een Endpoint moet u elke functie een naam geven op basis van de HTTP-methode die deze vertegenwoordigt. Het volgende voorbeeld definieert basis-HTTP-methoden in een Server Endpoint:

```typescript
// src/pages/methods.json.ts

import { APIRoute } from 'astro/dist/@types/astro';

export const GET: APIRoute = ({ params, request }) => {
  return new Response(
    JSON.stringify({
      message: 'Dit was een GET!',
    }),
  );
};

export const POST: APIRoute = ({ request }) => {
  return new Response(
    JSON.stringify({
      message: 'Dit was een POST!',
    }),
  );
};

export const DELETE: APIRoute = ({ request }) => {
  return new Response(
    JSON.stringify({
      message: 'Dit was een DELETE!',
    }),
  );
};

// ALL komt overeen met elke methode die u niet heeft geïmplementeerd.
export const ALL: APIRoute = ({ request }) => {
  return new Response(
    JSON.stringify({
      message: `Dit was een ${request.method}!`,
    }),
  );
};
```

Astro verwijdert het uiteindelijke bestand tijdens het bouwproces, dus de naam van het bestand moet de extensie van de gegevens bevatten die u wilt serveren (bijvoorbeeld `example.png.js` wordt `/example.png`).

## Serverless Functions met Astro op Vercel:

- Schalen naar nul wanneer niet in gebruik
- Schalen automatisch bij toenemend verkeer
- [Meer informatie over Serverless Functions](#)

# Edge Functions

Edge Functions zijn een snelle, schaalbare oplossing voor het leveren van dynamische inhoud aan gebruikers. Standaard worden Edge Functions wereldwijd ingezet en worden ze aangeroepen in een van de Edge-regio's van Vercel, dicht bij de bezoekers van uw site.

Astro ondersteunt momenteel Edge Functions niet op een ingebouwde manier, maar u kunt de `/api`-directory gebruiken om Edge Functions te definiëren met elk framework op Vercel. Zie de Edge Functions snelstart om aan de slag te gaan.

## Edge Functions met Nuxt op Vercel:

- Bieden kostenvoordelen door minder middelen te gebruiken dan Serverless Functions
- Kunnen worden uitgevoerd in de regio die het dichtst bij uw gebruikers of het dichtst bij de gegevensbronnen die ze nodig hebben, op basis van uw configuratie
- Hebben toegang tot de geolocatie en het IP-adres van bezoekers, waardoor locatiegebaseerde personalisatie mogelijk is
- [Meer informatie over Edge Functions](#)

# Afbeeldingsoptimalisatie

Afbeeldingsoptimalisatie helpt u snellere paginaladingen te bereiken door de grootte van afbeeldingen te verminderen en moderne afbeeldingsformaten te gebruiken. Bij implementatie op Vercel worden afbeeldingen automatisch geoptimaliseerd op aanvraag, waardoor uw bouwtijden snel blijven terwijl de paginaprestaties en Core Web Vitals worden verbeterd.

Afbeeldingsoptimalisatie met Astro op Vercel wordt standaard ondersteund met Astro's Image-component. Zie de Afbeeldingsoptimalisatie snelstart voor meer informatie.

## Afbeeldingsoptimalisatie met Astro op Vercel:

- Vereist geen configuratie voor afbeeldingsoptimalisatie bij gebruik van Astro's Image-component
- Helpt uw team om standaard uitstekende prestaties te garanderen
- Houdt uw bouwtijden snel door afbeeldingen on-demand te optimaliseren
- [Meer informatie over Afbeeldingsoptimalisatie](#)

# Middleware

Edge Middleware is code die wordt uitgevoerd voordat een verzoek wordt verwerkt op een site, waardoor u de respons kunt aanpassen. Omdat het vóór de cache wordt uitgevoerd, is Edge Middleware een effectieve manier om statisch gegenereerde inhoud te personaliseren.

Astro-middleware stelt u in staat om informatie in te stellen en te delen over uw eindpunten en pagina's met een `middleware.ts`-bestand in uw `src`-directory. Het volgende voorbeeld bewerkt het wereldwijde locals-object door gegevens toe te voegen die beschikbaar zullen zijn in elk `.astro`-bestand:

```typescript
// src/middleware.ts

// Deze helper typt middleware parameters automatisch
import { defineMiddleware } from 'astro:middleware';

export const onRequest = defineMiddleware(({ locals }, next) => {
  // onderschept gegevens van een verzoek
  // optioneel, wijzig de eigenschappen in `locals`
  locals.title = 'Nieuwe titel';

  // retourneer een Response of het resultaat van het oproepen van `next()`
  return next();
});
```

Astro-middleware is niet hetzelfde als Vercel's Edge Middleware, die in de hoofdmap van uw project moet worden geplaatst, buiten `src`.

Om aangepaste eigenschappen aan locals toe te voegen in `middleware.ts`, moet u een wereldwijde namespace declareren in uw `env.d.ts`-bestand:

```typescript
// src/env.d.ts

declare namespace App {
  interface Locals {
    title?: string;
  }
}
```

U kunt vervolgens toegang krijgen tot de gegevens die u aan locals heeft toegevoegd in elk `.astro`-bestand, zoals hier:

```typescript
// src/pages/middleware-title.astro

---
const { title } = Astro.locals;
---
<h1>{title}</h1>
<p>De naam van deze pagina komt uit middleware.</p>
```

## Implementatie van middleware aan de rand

U kunt Astro's middleware aan de rand implementeren, zodat u toegang heeft tot gegevens in de RequestContext en Request en gebruik kunt maken van de Edge Middleware-helpers van Vercel, zoals `geolocation()` of `ipAddress()`.

Om Astro's middleware aan de rand te gebruiken, stelt u `edgeMiddleware: true` in in uw `astro.config.ts`-bestand:

```typescript
// astro.config.ts

import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel/serverless';

export default defineConfig({
  output: 'server',
  adapter: vercel({
    edgeMiddleware: true,
  }),
});
```

Als u Vercel's Edge Middleware gebruikt, hoeft u `edgeMiddleware: true` niet in te stellen in uw `astro.config.ts`-bestand.

Zie de [docs van Astro](#) voor de beperkingen en beperkingen bij het gebruik van middleware aan de rand, evenals hun probleemoplossingstips.

## Gebruik van Astro.locals in Edge Middleware

Het object `Astro.locals` maakt gegevens beschikbaar voor uw `.astro`-componenten, waardoor u uw inhoud dynamisch kunt aanpassen met middleware. Om wijzigingen aan te brengen in `Astro.locals` in de middleware van Astro aan de rand:

1. Voeg een nieuw middleware-bestand toe naast uw `src/middleware.ts` en noem het `src/vercel-edge-middleware.ts`. Deze bestandsnaam is vereist om wijzigingen aan `Astro.locals` aan te brengen. Als u `Astro.locals` niet wilt bijwerken, is deze stap niet vereist.

2. Retourneer een object met de eigenschappen die u aan `Astro.locals` wilt toevoegen.

   Voor TypeScript moet u het pakket `@vercel/edge` installeren:

   ```bash
   pnpm i @vercel/edge
   ```

   Typ vervolgens uw middleware-functie als volgt:

   ```typescript
   // src/vercel-edge-middleware.ts

   import type { RequestContext } from '@vercel/edge';

   // Let op: de parameters verschillen van standaard Astro-middleware
   export default function ({
     request,
     context,
   }: {
     request: Request;
     context: RequestContext;
   }) {
     // Retourneer een Astro.locals-object met een `title`-eigenschap
     return {
       title: "Blog van Spider-man",
     };
   }
   ```

## Gebruik van Vercel's Edge Middleware

De middleware van Astro, die in `src/middleware.ts` moet staan, verschilt van de Vercel Edge Middleware, die een `middleware.ts`-bestand moet zijn in de hoofdmap van uw project.

Vercel raadt aan om oplossingen die native zijn voor het framework te gebruiken. U zou de middleware van Astro moeten gebruiken in plaats van de Vercel Edge Middleware waar mogelijk.

Als u nog steeds Vercel's Edge Middleware wilt gebruiken, zie dan de [Quickstart](#) om te leren hoe.

# Herschrijvingen

Herschrijvingen werken alleen voor statische

 bestanden met Astro. U moet Vercel's Edge Middleware gebruiken voor herschrijvingen. U moet `vercel.json` niet gebruiken om URL-paden te herschrijven met Astro-projecten; dit leidt tot inconsistent gedrag en wordt niet officieel ondersteund.

# Doorverwijzingen

In het algemeen raadt Vercel aan om oplossingen te gebruiken die native zijn voor het framework, en Astro heeft ingebouwde ondersteuning voor doorverwijzingen. Dat gezegd hebbende, kunt u ook doorverwijzingen maken met Vercel's Edge Middleware.

## Doorverwijzingen in uw Astro-configuratie

U kunt doorverwijzingen maken met Astro in `astro.config.ts` met behulp van de `redirects`-configuratieoptie, zoals hieronder weergegeven:

```typescript
// astro.config.ts

import { defineConfig } from 'astro/config';

export default defineConfig({
  redirects: {
    '/oude-pagina': '/nieuwe-pagina',
  },
});
```

## Doorverwijzingen in Server Endpoints

U kunt ook een doorverwijzing retourneren vanuit een Server Endpoint met behulp van het `redirect`-hulpprogramma:

```typescript
// src/pages/links/[id].ts

export async function GET({ params, redirect }): APIRoute {
  return redirect('/omleidingspad', 307);
}
```

## Doorverwijzingen in componenten

U kunt doorverwijzen vanuit Astro-componenten met `Astro.redirect()`:

```typescript
// src/pages/account.astro

---
import { isLoggedIn } from '../utils';

const cookie = Astro.request.headers.get('cookie');

// Als de gebruiker niet is ingelogd, doorverwijzen naar de inlogpagina
if (!isLoggedIn(cookie)) {
  return Astro.redirect('/login');
}
---

<h1>Je kunt deze pagina alleen zien als je bent ingelogd</h1>
```

## Astro Middleware op Vercel:

- Voert uit voordat een verzoek wordt verwerkt op een site, waardoor u reacties op gebruikersverzoeken kunt aanpassen
- Voert uit op alle verzoeken, maar kan worden beperkt tot specifieke paden via een matcher-configuratie
- Gebruikt de lichte Edge Runtime van Vercel om kosten laag en reacties snel te houden
- [Meer informatie over Edge Middleware](#)

# Caching

Vercel cacht automatisch statische bestanden aan de rand na het eerste verzoek en slaat ze tot 31 dagen op in het Edge Network van Vercel. Dynamische inhoud kan ook worden gecachet, en zowel het gedrag van dynamische als statische caching kan worden geconfigureerd met Cache-Control-headers.

De volgende Astro-component laat elke 10 seconden een nieuwe tijd zien. Dit wordt bereikt door een maximale leeftijd van 10 seconden in te stellen voor de inhoud van de pagina, en vervolgens verouderde inhoud te serveren terwijl nieuwe inhoud wordt gegenereerd op de server wanneer die leeftijd wordt overschreden.

[Meer informatie over Cache Control-opties](#)

```typescript
// src/pages/ssr-with-swr-caching.astro

---
Astro.response.headers.set('Cache-Control', 's-maxage=10, stale-while-revalidate');
const time = new Date().toLocaleTimeString();
---

<h1>{time}</h1>
```

## CDN Cache-Control-headers

U kunt ook controleren hoe de cache zich gedraagt op eventuele CDNs die u buiten het Edge Network van Vercel gebruikt, met CDN Cache-Control Headers.

Het volgende voorbeeld vertelt downstream CDNs om de inhoud 60 seconden te cachen, en Vercel's Edge Network om het 3600 seconden te cachen:

[Meer informatie over CDN Cache-Control-headers](#)

```typescript
// src/pages/ssr-with-swr-caching.astro

---
Astro.response.headers.set('Vercel-CDN-Cache-Control', 'max-age=3600',);
Astro.response.headers.set('CDN-Cache-Control', 'max-age=60',);
const time = new Date().toLocaleTimeString();
---

<h1>{time}</h1>
```

[Meer informatie over CDN Cache-Control-headers](#)

## Caching op Vercel:

- Optimaliseert en cacht automatisch bronnen voor de beste prestaties
- Vereist geen extra services om aan te schaffen of in te stellen
- Ondersteunt rollouts zonder downtime
- [Meer informatie over Caching](#)

# Speed Insights

Vercel Speed Insights biedt u een gedetailleerd overzicht van de prestatiegegevens van uw website, waardoor u geïnformeerde beslissingen kunt nemen voor optimalisatie. Door Speed Insights in te schakelen, krijgt u toegang tot het Speed Insights-dashboard, dat gedetailleerde informatie biedt over scores en individuele metingen zonder dat u code hoeft te wijzigen of het dashboard hoeft te verlaten.

Om Speed Insights in te schakelen met Astro, zie de Speed Insights snelstart.

Samenvattend, door Speed Insights te gebruiken met Astro op Vercel:

- Kun je verkeersprestatiegegevens volgen, zoals First Contentful Paint of First Input Delay
- Kunt u prestatiegegevens bekijken op paginaniveau en URL-niveau voor gedetailleerdere analyse
- Toont een score voor de prestaties van uw app op elke geregistreerde meting, die u kunt gebruiken om verbeteringen of regressies bij te houden
- [Meer informatie over Speed Insights](#)

# Meer voordelen

Bekijk onze [Frameworks-documentatiepagina](#) om meer te leren over de voordelen die beschikbaar zijn voor alle frameworks wanneer u implementeert op Vercel.

# Meer bronnen

Leer meer over het implementeren van Astro-projecten op Vercel met de volgende bronnen:

- [Vercel CLI](#): Leer hoe je jouw Astro-project kunt implementeren met Vercel CLI.
- [Documentatie voor Serverless Functions](#): Ontdek meer over de SSR-mogelijkheden van Vercel.
- [Astro-documentatie](#): Bekijk de volledige documentatie van Astro voor informatie over hun Vercel-adapter.

Laatst bijgewerkt op 2 maart 2023
