oEmbed is an open standard to easily embed content from oEmbed providers into your site. The SoundCloud oEmbed endpoint will serve the widget embed code for any SoundCloud URL pointing to a user, set, or a playlist. To find out more about the oEmbed standard, have a look at [oEmbed.com](https://oembed.com).

The SoundCloud oEmbed endpoint is located at `https://soundcloud.com/oembed`. It accepts any URL pointing to a user, set, or track and supports JSON (CORS) and JSONP as a response format.

A basic request/response example:

```bash
$ curl "https://soundcloud.com/oembed" \
       -d 'format=json' \
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

### Parameters

| Name          | Default     | Description                                                                                |
|---------------|-------------|--------------------------------------------------------------------------------------------|
| url           | -           | A Soundcloud URL for a track, set, user.                                                    |
| format        | json        | (optional) Either json or js (for JSONP).                                                   |
| callback      | -           | (optional) A function name for the JSONP callback.                                           |
| maxwidth      | 100%        | (optional) The maximum width in px.                                                         |
| maxheight     | 166 or 450  | (optional) The maximum height in px. The default is 166px for tracks and 450px for sets. If using the flash widget, the default is 81px for tracks and 305px for sets. |
| color         | -           | (optional) The primary color of the widget as a hex triplet. (For example: ff0066).         |
| auto_play     | false       | (optional) Whether the widget plays on load.                                                 |
| show_comments | true        | (optional) Whether the player displays timed comments.                                        |

[Status](https://status.soundcloud.com)
[Privacy](/docs/api/privacy)
[Cookies](/docs/api/cookies)
[Imprint](https://soundcloud.com/imprint)

[@SoundCloudDev](https://twitter.com/soundclouddev)
