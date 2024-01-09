oEmbed is een formaat dat het mogelijk maakt om een ingebedde representatie van een URL op externe sites toe te staan. De eenvoudige API stelt een website in staat ingebedde inhoud (zoals foto's of video's) weer te geven wanneer een gebruiker een koppeling naar die bron plaatst, zonder de bron rechtstreeks te hoeven analyseren.

Dit document is opgeslagen op GitHub.

## Inhoudsopgave
1. [Snel voorbeeld](#snel-voorbeeld)
2. [Volledige specificatie](#volledige-specificatie)
3. [Beveiligingsoverwegingen](#beveiligingsoverwegingen)
4. [Ontdekking](#ontdekking)
5. [Meer voorbeelden](#meer-voorbeelden)
6. [Auteurs](#auteurs)
7. [Implementaties](#implementaties)

## 1. Snel voorbeeld
Een consument (bijv. WordPress) doet het volgende HTTP-verzoek:

```
http://www.flickr.com/services/oembed/?format=json&url=http%3A//www.flickr.com/photos/bees/2341623661/
```

De aanbieder (bijv. Flickr) reageert vervolgens met een oEmbed-respons:

```json
{
	"version": "1.0",
	"type": "photo",
	"width": 240,
	"height": 160,
	"title": "ZB8T0193",
	"url": "http://farm4.static.flickr.com/3123/2341623661_7c99f48bbf_m.jpg",
	"author_name": "Bees",
	"author_url": "http://www.flickr.com/photos/bees/",
	"provider_name": "Flickr",
	"provider_url": "http://www.flickr.com/"
}
```

Dit stelt de consument in staat om een URL naar een Flickr-fotopagina om te zetten in gestructureerde gegevens om die foto in de website van de consument in te sluiten.

## 2. Volledige specificatie
Deze specificatie is onderverdeeld in drie delen: configuratie, het verzoek van de consument en de respons van de aanbieder.

### 2.1. Configuratie
De configuratie voor oEmbed is zeer eenvoudig. Aanbieders moeten één of meer URL-schema's en API-eindpuntparen specificeren. Het URL-schema beschrijft welke URL's die door de service worden aangeboden, een ingebedde representatie kunnen hebben. Het API-eindpunt beschrijft waar de consument representaties voor die URL's kan opvragen.

Bijvoorbeeld:

- URL-schema: http://www.flickr.com/photos/*
- API-eindpunt: http://www.flickr.com/services/oembed/

Het URL-schema kan één of meer wildcards bevatten (aangegeven met een asterisk). Wildcards kunnen aanwezig zijn in het domeingedeelte van de URL of in het pad. Binnen het domeingedeelte kunnen wildcards alleen worden gebruikt voor subdomeinen. Wildcards mogen niet worden gebruikt in het schema (om HTTP en HTTPS te ondersteunen, moet u twee URL/eindpuntparen opgeven).

Enkele voorbeelden:

- http://www.flickr.com/photos/* OK
- http://www.flickr.com/photos/*/foo/ OK
- http://*.flickr.com/photos/* OK
- http://*.com/photos/* NIET OK
- *://www.flickr.com/photos/* NIET OK

Het API-eindpunt moet wijzen naar een URL met een HTTP- of HTTPS-schema dat de hieronder beschreven API implementeert.

### 2.2. Verzoek van de consument
Verzoeken die naar het API-eindpunt worden gestuurd, moeten HTTP GET-verzoeken zijn, waarbij alle argumenten als queryparameters worden verzonden. Alle argumenten moeten urlencoded zijn (volgens RFC 1738).

De volgende queryparameters zijn gedefinieerd als onderdeel van de specificatie:

- url (verplicht): De URL om informatie voor inbedden op te halen.
- maxwidth (optioneel): De maximale breedte van de ingebedde bron. Geldt alleen voor sommige brontypen (zoals hieronder gespecificeerd). Voor ondersteunde brontypen moet deze parameter worden gerespecteerd door aanbieders.
- maxheight (optioneel): De maximale hoogte van de ingebedde bron. Geldt alleen voor sommige brontypen (zoals hieronder gespecificeerd). Voor ondersteunde brontypen moet deze parameter worden gerespecteerd door aanbieders.
- format (optioneel): Het vereiste responsformaat. Wanneer niet gespecificeerd, kan de aanbieder elk geldig responsformaat retourneren. Wanneer gespecificeerd, moet de aanbieder gegevens retourneren in het verzoekformaat, anders een fout retourneren (zie hieronder voor foutcodes).
   
   Providers moeten alle andere argumenten negeren die ze niet verwachten. Providers mogen aangepaste aanvullende parameters ondersteunen.
   
Enkele voorbeelden:

- http://flickr.com/services/oembed?url=http%3A//flickr.com/photos/bees/2362225867/
- http://flickr.com/services/oembed?url=http%3A//flickr.com/photos/bees/2362225867/&maxwidth=300&maxheight=400&format=json

Merk op: Aanbieders kunnen ervoor kiezen om het formaat te specificeren als onderdeel van de eindpunt-URL zelf, in plaats van als een querystringparameter.

### 2.3. Respons van de aanbieder
De respons die door de aanbieder wordt geretourneerd, kan in JSON- of XML-indeling zijn. Elk formaat specificeert een manier om naam-waardeparen te coderen die de responsgegevens vormen. Elk formaat heeft een bijbehorend mime-type dat samen met de respons moet worden geretourneerd in de Content-type-header.

### 2.3.1. JSON-respons
JSON-responsen moeten geldige JSON bevatten en moeten het mime-type application/json gebruiken. Het JSON-responsformaat kan worden opgevraagd door de consument door een formaat van json te specificeren.

Bijvoorbeeld:

```json
{
	"foo": "bar",
	"baz": 1
}
```

De te retourneren naam-waardeparen worden hieronder gespecificeerd. Alle tekst moet worden gecodeerd in UTF-8.

### 2.3.

2. XML-respons
XML-responsen moeten het mime-type text/xml gebruiken. Het XML-responsformaat kan worden opgevraagd door de consument door een formaat van xml te specificeren. Het responslichaam moet geldige XML bevatten met een rootelement genaamd oembed en kindelementen voor elke sleutel die de waarde bevat binnen het elementlichaam.

Bijvoorbeeld:

```xml
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<oembed>
	<foo>bar</foo>
	<baz>1</baz>
</oembed>
```

De te retourneren naam-waardeparen worden hieronder gespecificeerd. Alle tekst moet worden gecodeerd in UTF-8. Waarden moeten worden geëscaped als PCDATA.

### 2.3.4. Reactieparameters
Reacties kunnen een brontype specificeren, zoals foto of video. Elk type heeft specifieke parameters die eraan zijn gekoppeld. De volgende reactieparameters zijn geldig voor alle soorten reactietypen:

- type (verplicht): Het brontype. Geldige waarden, samen met specifieke parameters voor waarden, worden hieronder beschreven.
- version (verplicht): Het oEmbed-versienummer. Dit moet 1.0 zijn.
- title (optioneel): Een teksttitel die de bron beschrijft.
- author_name (optioneel): De naam van de auteur/eigenaar van de bron.
- author_url (optioneel): Een URL voor de auteur/eigenaar van de bron.
- provider_name (optioneel): De naam van de bronleverancier.
- provider_url (optioneel): De URL van de bronleverancier.
- cache_age (optioneel): De voorgestelde cache-levensduur voor deze bron, in seconden. Consumenten kunnen ervoor kiezen om deze waarde wel of niet te gebruiken.
- thumbnail_url (optioneel): Een URL naar een miniatuurafbeelding die de bron vertegenwoordigt. De miniatuur moet voldoen aan eventuele maxwidth- en maxheight-parameters. Als deze parameter aanwezig is, moeten ook thumbnail_width en thumbnail_height aanwezig zijn.
- thumbnail_width (optioneel): De breedte van de optionele miniatuur. Als deze parameter aanwezig is, moeten ook thumbnail_url en thumbnail_height aanwezig zijn.
- thumbnail_height (optioneel): De hoogte van de optionele miniatuur. Als deze parameter aanwezig is, moeten ook thumbnail_url en thumbnail_width aanwezig zijn.

Aanbieders kunnen optioneel alle parameters bevatten die niet zijn gespecificeerd in dit document (zolang ze dezelfde sleutel-waarde-indeling gebruiken) en consumenten kunnen ervoor kiezen deze te negeren. Consumenten moeten parameters negeren die ze niet begrijpen.

(Vertaling van sectie 2.3.4 en vervolg)

### 2.3.4.1. Het fototype
Dit type wordt gebruikt voor het weergeven van statische foto's. De volgende parameters zijn gedefinieerd:

- url (verplicht): De bron-URL van de afbeelding. Consumenten moeten in staat zijn om deze URL in een <img> element in te voegen. Alleen HTTP- en HTTPS-URL's zijn geldig.
- width (verplicht): De breedte in pixels van de afbeelding die is gespecificeerd in de url-parameter.
- height (verplicht): De hoogte in pixels van de afbeelding die is gespecificeerd in de url-parameter.

Reacties van dit type moeten voldoen aan de maxwidth- en maxheight-verzoekparameters.

### 2.3.4.2. Het videotype
Dit type wordt gebruikt voor het weergeven van afspeelbare video's. De volgende parameters zijn gedefinieerd:

- html (verplicht): De vereiste HTML om een videospeler in te sluiten. De HTML mag geen padding of marges hebben. Consumenten kunnen ervoor kiezen om de HTML in een off-domein iframe te laden om XSS-kwetsbaarheden te voorkomen.
- width (verplicht): De breedte in pixels vereist om de HTML weer te geven.
- height (verplicht): De hoogte in pixels vereist om de HTML weer te geven.

Reacties van dit type moeten voldoen aan de maxwidth- en maxheight-verzoekparameters. Als een aanbieder wil dat de consument alleen een miniatuur verstrekt in plaats van een inbedbare speler, moeten ze in plaats daarvan een fotoreactietype retourneren.

```markdown
(Vertaling van secties 2.3.4.3 tot en met 7.3)

### 2.3.4.3. Het linktype
Reacties van dit type stellen een aanbieder in staat om algemene ingesloten gegevens (zoals titel en auteur_naam) terug te geven, zonder de url- of html-parameter te verstrekken. De consument kan vervolgens naar de bron linken, met gebruikmaking van de URL die is gespecificeerd in het oorspronkelijke verzoek.

### 2.3.4.4. Het rich-type
Dit type wordt gebruikt voor rijke HTML-inhoud die niet onder een van de andere categorieën valt. De volgende parameters zijn gedefinieerd:

- html (verplicht): De HTML vereist om de bron weer te geven. De HTML mag geen padding of marges hebben. Consumenten kunnen ervoor kiezen om de HTML in een off-domein iframe te laden om XSS-kwetsbaarheden te voorkomen. De opmaak moet geldig XHTML 1.0 Basic zijn.
- width (verplicht): De breedte in pixels vereist om de HTML weer te geven.
- height (verplicht): De hoogte in pixels vereist om de HTML weer te geven.

Reacties van dit type moeten voldoen aan de maxwidth- en maxheight-verzoekparameters.

### 2.3.5. Fouten
Aanbieders moeten eventuele foutvoorwaarden retourneren als HTTP-statuscodes. De volgende statuscodes zijn gedefinieerd als onderdeel van de oEmbed-specificatie:

- 404 Niet gevonden: De aanbieder heeft geen reactie voor de opgevraagde url-parameter. Dit stelt aanbieders in staat om breed te zijn in hun URL-schema, en vervolgens op aanroeptijd te bepalen of ze een representatie hebben om terug te geven.
- 501 Niet geïmplementeerd: De aanbieder kan geen respons retourneren in het gevraagde formaat. Dit moet worden verzonden wanneer (bijvoorbeeld) het verzoek formaat=xml bevat en de aanbieder geen ondersteuning biedt voor XML-responsen. Aanbieders worden echter aangemoedigd zowel JSON als XML te ondersteunen.
- 401 Niet geautoriseerd: De gespecificeerde URL bevat een privé (niet-openbare) bron. De consument moet rechtstreeks een link naar de bron verstrekken in plaats van extra informatie in te sluiten, en vertrouwen op de aanbieder voor toegangscontrole.

### 3. Beveiligingsoverwegingen
Wanneer een consument URL's weergeeft, willen ze waarschijnlijk het URL-schema filteren om een van de volgende te zijn: http, https of mailto, hoewel aanbieders vrij zijn om elk geldig URL-schema te specificeren. Zonder filteren kunnen URL's in de stijl van Javascript:... worden gebruikt voor XSS-aanvallen.

Wanneer een consument HTML weergeeft (zoals bij video-insluitingen), is er een vector voor XSS-aanvallen vanuit de aanbieder. Om dit te voorkomen, wordt aanbevolen dat consumenten de HTML weergeven in een iframe, gehost vanaf een ander domein. Hierdoor kan de HTML geen cookies van het consumentendomein benaderen.

### 4. Ontdekking
oEmbed-aanbieders kunnen ervoor kiezen om hun oEmbed-ondersteuning ontdekt te maken door <link>-elementen toe te voegen aan de kop van hun bestaande (X)HTML-documenten of door Link-headers in te stellen.

Voorbeeld van een element:

```html
<link rel="alternate" type="application/json+oembed"
  href="http://flickr.com/services/oembed?url=http%3A%2F%2Fflickr.com%2Fphotos%2Fbees%2F2362225867%2F&format=json"
  title="Bacon Lollys oEmbed Profile" />
<link rel="alternate" type="text/xml+oembed"
  href="http://flickr.com/services/oembed?url=http%3A%2F%2Fflickr.com%2Fphotos%2Fbees%2F2362225867%2F&format=xml"
  title="Bacon Lollys oEmbed Profile" />
```

Voorbeeld van een header:

```html
Link: <http://flickr.com/services/oembed?url=http%3A%2F%2Fflickr.com%2Fphotos%2Fbees%2F2362225867%2F&format=json>; rel="alternate"; type="application/json+oembed"; title="Bacon Lollys oEmbed Profile"
Link: <http://flickr.com/services/oembed?url=http%3A%2F%2Fflickr.com%2Fphotos%2Fbees%2F2362225867%2F&format=xml>; rel="alternate"; type="text/xml+oembed"; title="Bacon Lollys oEmbed Profile"
```

De URL's in het href-attribuut of uri-referentie tussen haakjes moeten het volledige oEmbed-eindpunt plus URL zijn en eventuele benodigde formaatparameters. Geen andere verzoekparameters mogen in deze URL worden opgenomen.

Het type-attribuut moet ofwel application/json+oembed bevatten voor JSON-responsen, ofwel text/xml+oembed voor XML.

### 5. Meer voorbeelden
#### 5.1. Videovoorbeeld
Verzoek:

```
https://www.youtube.com/oembed?url=https%3A//youtube.com/watch%3Fv%3DM3r2XDceM6A&format=json
```

Reactie:

```json
{
	"version": "1.0",
	"type": "video",
	"provider_name": "YouTube",
	"provider_url": "https://youtube.com/",
	"width": 425,
	"height": 344,
	"title": "Amazing Nintendo Facts",
	"author_name": "ZackScott",
	"author_url": "https://www.youtube.com/user/ZackScott",
	"html": "<object width=\"425\" height=\"344\"><param name=\"movie\" value=\"https://www.youtube.com/v/M3r2XDceM6A&fs=1\"></param><param name=\"allowFullScreen\" value=\"true\"></param><param name=\"allowscriptaccess\" value=\"always\"></param><embed src=\"https://www.youtube.com/v/M3r2XDceM6A&fs=1\" type=\"application/x-shockwave-flash\" width=\"425\" height=\"344\" allowscriptaccess=\"always\" allowfullscreen=\"true

\"></embed></object>"
}
```

#### 5.2. Linkvoorbeeld
Verzoek:

```
http://iamcal.com/oembed/?url=http%3A//www.iamcal.com/linklog/1206113631/&format=xml
```

Reactie:

```xml
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<oembed>
	<version>1.0</version>
	<type>link</type>
	<author_name>Cal Henderson</author_name>
	<author_url>http://iamcal.com/</author_url>
	<cache_age>86400</cache_age>
	<provider_name>iamcal.com</provider_name>
	<provider_url>http://iamcal.com/</provider_url>
</oembed>
```

### 6. Auteurs
Cal Henderson (cal [at] iamcal.com)
Mike Malone (mjmalone [at] gmail.com)
Leah Culver (leah.culver [at] gmail.com)
Richard Crowley (r [at] rcrowley.org)

### 7. Implementaties
#### 7.1. Aanbieders
Aanbieders zijn programmatisch beschikbaar als een json-bestand: https://oembed.com/providers.json.

Om nieuwe aanbieders toe te voegen, fork dit repository op GitHub en voeg/wijzig providers/*.yml.

Er zijn momenteel 298 aanbieders in het register. Aanbieders en consumenten worden sterk aangemoedigd om het ontdekkingsmechanisme te gebruiken, in plaats van het register.

#### 7.2. Consumenten
Veel diensten consumeren oEmbed-informatie om linkinformatie weer te geven, waaronder WordPress en Slack.

Er zijn ook enkele tools specifiek gebouwd rond het beheren van URL-insluitingen:

- Iframely (http://iframely.com/)
- OEmbed Link Viewer (https://oembed.link/)

#### 7.3. Bibliotheken
Er zijn verschillende bibliotheken beschikbaar voor diverse programmeertalen om oEmbed te ondersteunen, zoals:

- PHP: php-oembed (http://code.google.com/p/php-oembed/)
- Python: pyoembed (http://github.com/rafaelmartins/pyoembed/)
- Ruby: oembed_links (http://github.com/netshade/oembed_links)
- Java: java-oembed (https://github.com/michael-simons/java-oembed)
- En nog veel meer...

Voor verdere informatie over implementaties, raadpleeg de officiële bronnen en documentatie.

Deze documentatie is opgeslagen op GitHub. Gelieve de mailinglijst te raadplegen, fork en bijdragen.

#### 7.3. Bibliotheken (Vervolg)
Andere beschikbare bibliotheken voor het ondersteunen van oEmbed in verschillende programmeertalen zijn onder andere:

- .Net: oEmbed API Wrapper (http://oembed.codeplex.com/)
- JQuery: oEmbed API Wrapper (https://github.com/starfishmod/jquery-oembed-all)
- Node.js: oEmbed API Gateway (https://github.com/itteco/iframely)
- Elixir: furlex (https://github.com/claytongentry/furlex)
- Elixir: elixir-oembed (https://github.com/r8/elixir-oembed)
- Django: micawber (https://github.com/coleifer/micawber)
- PHP: Services_oEmbed (http://pear.php.net/package/Services_oEmbed)
- PHP: Essence (https://github.com/felixgirault/essence)
- PHP: Embera (https://github.com/mpratt/Embera)
- Python: PyEmbed (http://pyembed.github.io)
- Python: python-oembed (https://github.com/abarmat/python-oembed)
- Perl: Web-oEmbed (http://search.cpan.org/~miyagawa/Web-oEmbed/)

Voor verdere informatie over implementaties, raadpleeg de officiële bronnen en documentatie.

### 8. Pers en Links
- [Officiële oEmbed mailinglijst](https://groups.google.com/group/oembed)
- [Webmonkey-tutorial](https://www.webmonkey.com/2010/02/oembed_a_simple_way_to_embed_content_from_other_sites/)
- [Leah's blog](https://leahculver.com/)
- [Ajaxian](https://ajaxian.com/)
