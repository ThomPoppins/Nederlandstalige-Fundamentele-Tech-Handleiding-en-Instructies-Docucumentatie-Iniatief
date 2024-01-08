# 🚀 @astrojs/tailwind

Deze Astro-integratie brengt de utility CSS-klassen van Tailwind naar elk `.astro`-bestand en frameworkcomponent in jouw project, samen met ondersteuning voor het Tailwind-configuratiebestand.

## 💡 Waarom Tailwind?

Tailwind stelt je in staat om utility-klassen te gebruiken in plaats van CSS te schrijven. Deze utility-klassen komen meestal één op één overeen met een bepaalde CSS-eigenschapsinstelling. Bijvoorbeeld, het toevoegen van `text-lg` aan een element is equivalent aan het instellen van `font-size: 1.125rem` in CSS. Mogelijk vind je het makkelijker om je stijlen te schrijven en te onderhouden met behulp van deze vooraf gedefinieerde utility-klassen!

Als je niet van die vooraf gedefinieerde instellingen houdt, kun je het Tailwind-configuratiebestand aanpassen aan de ontwerpeisen van jouw project. Bijvoorbeeld, als de "grote tekst" in jouw ontwerp eigenlijk `2rem` is, kun je de `fontSize`-instelling voor `lg` wijzigen naar `2rem`.

Tailwind is ook een uitstekende keuze om stijlen toe te voegen aan React-, Preact- of Solid-componenten, die geen `<style>`-tag ondersteunen in het componentbestand.

**Opmerking:** Het wordt over het algemeen afgeraden om zowel Tailwind als een andere stylingsmethode (bijv. Styled Components) in hetzelfde bestand te gebruiken.
