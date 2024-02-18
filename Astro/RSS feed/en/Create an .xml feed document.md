
[Section titled Create an .xml feed document](https://docs.astro.build/en/tutorial/5-astro-api/4/#create-an-xml-feed-document)

1. Create a new file in `src/pages/` called `rss.xml.js`
    
2. Copy the following code into this new document. Customize the `title` and `description` properties, and if necessary, specify a different language in `customData`:
    
    `src/pages/rss.xml.js`
    
```jsx
import rss, { pagesGlobToRssItems } from '@astrojs/rss';

export async function GET(context) {  return rss({    title: 'Astro Learner | Blog',    description: 'My journey learning Astro',    site: context.site,    items: await pagesGlobToRssItems(import.meta.glob('./**/*.md')),    customData: `<language>en-us</language>`,  });}
```
    
3. Add the `site` property to the Astro config with your site’s own unique Netlify URL.
    
    `astro.config.mjs`
    
    ```jsx
    import { defineConfig } from "astro/config";
    export default defineConfig({  site: "https://example.com"});
    ```
    
4. This `rss.xml` document is only created when your site is built, so you won’t be able to see this page in your browser during development. Quit the dev server and run the following commands to first, build your site locally and then, view a preview of your build:


    ```bash
    pnpm run build
    pnpm run preview
    ```
    
5. Visit `http://localhost:4321/rss.xml` and verify that you can see (unformatted) text on the page with an `item` for each of your `.md` files. Each item should contain blog post information such as `title`, `url`, and `description`.
    
    View your RSS feed in a reader
    
    Download a feed reader, or sign up for an online feed reader service and subscribe to your site by adding your own Netlify URL. You can also share this link with others so they can subscribe to your posts, and be notified when a new one is published.
    
6. Be sure to quit the preview and restart the dev server when you want to view your site in development mode again.
    

## Checklist

[Section titled Checklist](https://docs.astro.build/en/tutorial/5-astro-api/4/#checklist)

- I can install an Astro package using the command line.
- I can create an RSS feed for my website.

### Resources

[Section titled Resources](https://docs.astro.build/en/tutorial/5-astro-api/4/#resources)

- [RSS item generation in Astro](https://docs.astro.build/en/guides/rss/#using-glob-imports)