# Configuratie van Dependabot-versie-updates 🛠️

## Over versie-updates voor afhankelijkheden ℹ️

Afhankelijkheidsversies worden automatisch bijgewerkt door Dependabot in te schakelen voor je repository. Hier lees je hoe je dit kunt configureren en beheren.

## Activeren van Dependabot-versie-updates 🔄

Om Dependabot-versie-updates in te schakelen, voeg je een `dependabot.yml` configuratiebestand toe aan de `.github`-directory van je repository. Dit bestand bevat instructies voor Dependabot over welke afhankelijkheden bijgewerkt moeten worden en hoe vaak dit moet gebeuren.

## Status van versie-updates controleren 🕵️‍♂️

Zodra je versie-updates hebt ingeschakeld, kun je de status ervan controleren. Dependabot zal pull-aanvragen genereren om de afhankelijkheden up-to-date te houden. Deze kunnen binnen enkele minuten na het toevoegen van het configuratiebestand verschijnen, afhankelijk van het aantal manifestbestanden dat je hebt geconfigureerd voor updates.

## Uitschakelen van Dependabot-versie-updates 🚫

Als je besluit Dependabot-versie-updates uit te schakelen, kun je dit doen via de configuratie in het `dependabot.yml` bestand. Alleen mensen met schrijfrechten voor de repository kunnen Dependabot-versie-updates in- of uitschakelen.

Zorg ervoor dat je ook bekijkt hoe je Dependabot kunt configureren voor beveiligingsupdates in het artikel "Configuring Dependabot Security Updates." 🔒

## Beheersen van het aantal pull-aanvragen 🔄

Om pull-aanvragen beheersbaar en gemakkelijk te beoordelen te houden, genereert Dependabot maximaal vijf pull-aanvragen om afhankelijkheden naar de nieuwste versie te brengen. Als je sommige van deze pull-aanvragen samenvoegt vóór de volgende geplande update, worden de resterende pull-aanvragen geopend bij de volgende update, tot aan dat maximum. Je kunt het maximale aantal open pull-aanvragen wijzigen door de configuratieoptie `open-pull-requests-limit` in te stellen.

## Groeperen van afhankelijkheden 🤝

Om het aantal pull-aanvragen verder te verminderen, kun je de configuratieoptie `groups` gebruiken om sets van afhankelijkheden samen te voegen (per pakketecosysteem). Dependabot genereert dan één pull-aanvraag om zoveel mogelijk afhankelijkheden in de groep tegelijkertijd bij te werken naar de nieuwste versies. Zie "Aanpassen van afhankelijkheidsupdates" voor meer informatie.

## Fouten bij Dependabot-run 🚨

Soms, als gevolg van een onjuiste configuratie of een incompatibele versie, kan het voorkomen dat een Dependabot-run mislukt. Na 30 mislukte runs slaat Dependabot versie-updates geplande runs over totdat je handmatig een controle voor updates van de afhankelijkheidsgrafiek start. Dependabot-beveiligingsupdates blijven zoals gewoonlijk worden uitgevoerd.
## Aanpassen van de te updaten dependencies 🔄

Standaard worden alleen directe afhankelijkheden die expliciet zijn gedefinieerd in een manifest bijgewerkt door Dependabot-versie-updates. Je kunt ervoor kiezen om updates te ontvangen voor indirecte afhankelijkheden die zijn gedefinieerd in lock-bestanden. Raadpleeg "Configuratieopties voor het `dependabot.yml`-bestand" voor meer informatie.


Hier is een voorbeeld van een eenvoudige `dependabot.yml`-configuratie voor een Astro-project. Houd er rekening mee dat dit een basisconfiguratie is en je deze naar wens kunt aanpassen op basis van de behoeften van je project.

```yaml
version: 2
updates:
  - package-ecosystem: "astro"
    directory: "/"
    schedule:
      interval: "daily"
    open-pull-requests-limit: 5
    # Customize further if needed
```

In dit voorbeeld:

- We specificeren dat het pakketecosysteem Astro is met de sleutel `package-ecosystem`.
- `directory` geeft aan dat we alle bestanden in de repository willen scannen (`/` staat voor de hoofdmap).
- `schedule` stelt in dat Dependabot dagelijks moet controleren op updates. Je kunt dit aanpassen aan je eigen voorkeur, bijvoorbeeld `"weekly"` of `"monthly"`.
- `open-pull-requests-limit` beperkt het aantal tegelijk geopende pull-aanvragen tot 5, maar dit kan worden aangepast op basis van jouw voorkeur.

Zorg ervoor dat je de configuratie aanpast aan de structuur en behoeften van je Astro-project. Voor meer geavanceerde configuratieopties, zoals het groeperen van afhankelijkheden, kun je de [officiële documentatie van Dependabot](https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/configuration-options-for-dependency-updates) raadplegen.





