oEmbed is een open standaard om eenvoudig inhoud van oEmbed-providers in uw site in te sluiten. Het SoundCloud oEmbed-eindpunt zal de widget-insluitcode leveren voor elke SoundCloud-URL die verwijst naar een gebruiker, set of afspeellijst. Voor meer informatie over de oEmbed-standaard, bekijk [oEmbed.com](https://oembed.com).

Het SoundCloud oEmbed-eindpunt bevindt zich op `https://soundcloud.com/oembed`. Het accepteert elke URL die wijst naar een gebruiker, set of track en ondersteunt JSON (CORS) en JSONP als responsindeling.


    https://soundcloud.com/oembed


Een basisverzoek-/responsvoorbeeld:

```bash
$ curl "https://soundcloud.com/oembed" \\
       -d 'format=json' \\
       -d 'url=https://soundcloud.com/forss/flickermood'
```

```json
{
  "version": 1.0,
  "type": "rich",
  "provider_name": "Soundcloud",
  "provider_url": "https://soundcloud.com",
  "height": 81,
  "width": "100%",
  "title": "Flickermood by Forss",
  "description": "test",
  "html": "test"
}
```

## Parameters

| Naam       | Standaard | Omschrijving                                                                                       |
|------------|-----------|----------------------------------------------------------------------------------------------------|
| url        | -         | Een Soundcloud-URL voor een track, set, gebruiker.                                                   |
| format     | json      | (optioneel) Ofwel json of js (voor JSONP).                                                           |
| callback   | -         | (optioneel) Een functienaam voor de JSONP-callback.                                                  |
| maxwidth   | 100%      | (optioneel) De maximale breedte in px.                                                               |
| maxheight  | 166 of 450| (optioneel) De maximale hoogte in px. De standaard is 166px voor tracks en 450px voor sets. Als u de flash-widget gebruikt, is de standaard 81px voor tracks en 305px voor sets. |
| color      | -         | (optioneel) De primaire kleur van de widget als hexadecimaal triplet. (Bijvoorbeeld: ff0066).        |
| auto_play  | false     | (optioneel) Of de widget afspeelt bij laden.                                                          |
| show_comments | true    | (optioneel) Of de speler getimede opmerkingen weergeeft.                                             |

[Status](https://status.soundcloud.com)
[Privacy](/docs/api/privacy)
[Cookies](/docs/api/cookies)
[Imprint](https://soundcloud.com/imprint)

[@SoundCloudDev](https://twitter.com/soundclouddev)
```

Let op: enkele links zijn relatief en kunnen mogelijk niet correct worden weergegeven in de Markdown-opmaak zonder de juiste context of paden. Pas deze aan indien nodig.