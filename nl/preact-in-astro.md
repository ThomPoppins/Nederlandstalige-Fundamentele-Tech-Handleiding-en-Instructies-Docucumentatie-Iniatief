# Preact in Astro

## Preact

"A different kind of library
metal
Closer to the DOM"

### Down the rabbithole

Preact biedt de dunst mogelijke Virtual DOM abstractie boven op de DOM. Het bouwt voort op stabiele platformfuncties, registreert echte event handlers en werkt goed samen met andere bibliotheken.

Preact kan rechtstreeks in de browser worden gebruikt zonder enige transpilatiestappen.

grootte
Kleine omvang
De meeste UI-frameworks zijn groot genoeg om het grootste deel van de JavaScript-code van een app te vormen. Preact is anders: het is klein genoeg zodat jouw code het grootste deel van jouw toepassing is.

Dat betekent minder JavaScript om te downloaden, te parseren en uit te voeren - met meer tijd voor jouw code, zodat je een ervaring kunt bouwen die je definieert zonder te hoeven vechten om een framework onder controle te houden.

#### #### Naadloze Integratie: Preact Biedt Directe Browserfunctionaliteit Zonder Transpilatiezorgen

**Transpilatie verwijst naar het proces waarbij de broncode van een programma geschreven in een bepaalde programmeertaal wordt omgezet (vertaald) naar een andere programmeertaal, waarbij de functionele betekenis behouden blijft. In het geval van JavaScript worden transpilatiestappen vaak gebruikt om code geschreven in een moderne JavaScript-variant (bijvoorbeeld ECMAScript 2015 of hoger) om te zetten naar een oudere versie die compatibel is met oudere browsers.**

Hier zijn de algemene stappen van JavaScript-transpilatie:

_1. **Schrijven van Broncode:**
   _- Een ontwikkelaar schrijft broncode in een moderne JavaScript-variant, zoals ES6 (ECMAScript 2015) of hoger._

_2. **Transpilatie:**
   _- De geschreven code wordt vervolgens door een transpiler (een specifiek type compiler voor broncodevertaling) verwerkt._
   _- De transpiler converteert de moderne JavaScript-code naar een oudere versie, zoals ES5 (ECMAScript 5) dat breder wordt ondersteund door oudere webbrowsers._

_3.**Uitvoering:**
   _- De getranspileerde code kan nu worden uitgevoerd in browsers die mogelijk geen __ondersteuning bieden voor de nieuwere JavaScript-functies, maar wel voor oudere standaarden._

#### De definitie van _compatible_ is Preact

In het geval van Preact, zoals aangegeven in de oorspronkelijke tekst, is het bijzondere dat Preact direct in de browser kan worden gebruikt zonder de noodzaak van transpilatiestappen. Dit betekent dat je de Preact-bibliotheek rechtstreeks kunt integreren in je project zonder je zorgen te maken over het omzetten van de broncode naar een oudere JavaScript-versie voor browsercompatibiliteit.

Om Preact in Astro te gebruiken, dien je Preact-componenten te importeren zoals je zou doen in een Preact-toepassing. Echter, je moet de `render`-functie van `preact/compat` gebruiken om de Preact-componenten in Astro te renderen. Hier is een voorbeeld:

```astro
---
import { h } from 'preact';
import { render } from 'preact/compat';
import YourPreactComponent from '../pad/naar/JouwPreactComponent';
---

<JouwPreactComponent />
```

In dit voorbeeld is `JouwPreactComponent` een Preact-component die je hebt geïmporteerd uit een ander bestand. Je kunt deze component in je Astro-markup gebruiken zoals elke andere component.

Vervang alsjeblieft `'../pad/naar/JouwPreactComponent'` door het daadwerkelijke pad naar je Preact-component.

Onthoud dat wanneer je Preact-componenten in Astro gebruikt, je de `render`-functie van `preact/compat` moet gebruiken om ze te renderen. Dit komt doordat Astro standaard geen Preact gebruikt om componenten te renderen.
