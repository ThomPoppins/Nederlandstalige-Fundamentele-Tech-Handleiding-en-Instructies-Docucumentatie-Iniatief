```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width-device-width, inital-scale=1.0, shrink-to-fit=no">
    <style type="text/css">
      #main-content {
        margin: 0 auto;
      }

      .responsive {
        width: 100%;
        height: 0;
        padding-bottom: 100%;
        position: relative;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        align-items: center;
      }

      .responsive iframe {
        position: absolute;
        height: 100%;
        width: 100%;
      }
      
      @media only screen and (min-width: 700px) {
        .responsive iframe {
          width: 700px;
        }
      }
    </style>
  </head>
  <body>
    Hello world!
    <div class="responsive">
      <iframe src="https://bandcamp.com/EmbeddedPlayer/album=2504581908/size=large/bgcol=ffffff/linkcol=0687f5/tracklist=false/transparent=true/" seamless><a href="http://gobsaudio.bandcamp.com/album/the-austerity-ep">The Austerity EP by Gobs</a></iframe>
    </div>
    <p>This is some text below me</p>
  </body>
</html>
```

