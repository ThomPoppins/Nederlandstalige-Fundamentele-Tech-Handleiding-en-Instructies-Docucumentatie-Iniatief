Preact in Astro gebruiken

Om Preact in Astro te gebruiken, dien je Preact-componenten te importeren zoals je zou doen in een Preact-toepassing. Echter, je moet de `render`-functie van `preact/compat` gebruiken om de Preact-componenten in Astro te renderen. Hier is een voorbeeld:

```astro
---
import { h } from 'preact';
import { render } from 'preact/compat';
import YourPreactComponent from '../pad/naar/JouwPreactComponent';
---

<YourPreactComponent />
```

In dit voorbeeld is `YourPreactComponent` een Preact-component die je hebt geïmporteerd uit een ander bestand. Je kunt deze component in je Astro-markup gebruiken zoals elke andere component.

Vervang alsjeblieft `'../pad/naar/JouwPreactComponent'` door het daadwerkelijke pad naar je Preact-component.

Onthoud dat wanneer je Preact-componenten in Astro gebruikt, je de `render`-functie van `preact/compat` moet gebruiken om ze te renderen. Dit komt doordat Astro standaard geen Preact gebruikt om componenten te renderen.
