Certainly! Below is the documentation text formatted in Markdown:

```markdown
# Astro on Vercel

Learn how to use Vercel's features with Astro. Astro is an all-in-one web framework that enables you to build performant static websites. People choose Astro when they want to build content-rich experiences with as little JavaScript as possible.

You can deploy a static Astro app to Vercel with zero configuration.

## Get Started with Astro on Vercel

To get started with Astro on Vercel:

1. If you already have a project with Astro, install Vercel CLI and run the `vercel` command from your project's root directory.
2. Clone one of our Astro example repos to your favorite git provider and deploy it on Vercel with the button below:

   - [Deploy our Astro template](#), or view a live example.
   - Or, choose a template from Vercel's marketplace.

## Using Vercel's features with Astro

To deploy a server-rendered Astro app or a static Astro site with Vercel features like Web Analytics and Image Optimization, follow these steps:

1. Add Astro's Vercel adapter to your project using either of the following methods:

   ```bash
   # Using astro add (recommended)
   pnpm astro add vercel
   ```

   Or manually install the package:

   ```bash
   pnpm i @astrojs/vercel
   ```

2. Configure your project in `astro.config.ts`. Import either the serverless or static plugin, and set the output to server or static respectively:

   ```typescript
   import { defineConfig } from 'astro/config';
   import vercelServerless from '@astrojs/vercel/serverless';

   export default defineConfig({
     output: 'server',
     adapter: vercelServerless(),
   });
   ```

3. Enable Vercel's features using Astro's configuration options. Here's an example enabling Web Analytics and setting a maximum duration for Serverless Function routes:

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

### Configuration options

The following configuration options enable Vercel's features for Astro deployments:

- `maxDuration`: (number, Serverless) - Extends or limits the maximum duration (in seconds) that Serverless Functions can run before timing out.
- `webAnalytics`: ({ enabled: boolean }, Static, Serverless) - Enables Vercel's Web Analytics.
- `imageService`: (boolean, Static, Serverless) - Enables an automatically configured service to optimize your images (for Astro versions 3 and up).
- `devImageService`: (string, Static, Serverless) - Configures the image service used to optimize your images in your dev environment (for Astro versions 3 and up).
- `imagesConfig`: (VercelImageConfig, Static, Serverless) - Defines the behavior of the Image Optimization API, allowing on-demand optimization at runtime.
- `functionPerRoute`: (boolean, Serverless) - API routes are bundled into one function by default. Set this to true to split each route into separate functions.
- `edgeMiddleware`: (boolean, Serverless) - Set to true to automatically convert Astro middleware to Edge Middleware.
- `includeFiles`: (string[], Serverless) - Force files to be bundled with your Serverless functions.
- `excludeFiles`: (string[], Serverless) - Exclude files from being bundled with your Serverless functions. Also available with .vercelignore.

For more details on the configuration options, see [Astro's docs](#).

## Server-Side Rendering

Using SSR, or on-demand rendering as Astro calls it, enables you to deploy your routes as Serverless Functions on Vercel. This allows you to add dynamic elements to your app, such as user logins and personalized content.

You can enable SSR by adding the Vercel adapter to your project.

If your Astro project is statically rendered, you can opt individual routes. To do so:

1. Set your output option to hybrid in your `astro.config.ts`:

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

2. Add `export const prerender = false;` to your components:

   ```typescript
   // src/pages/mypage.astro

   export const prerender = false;
   // ...
   ```

SSR with Astro on Vercel:

- Scales to zero when not in use
- Scales automatically with traffic increases
- Has zero-configuration support for Cache-Control headers, including stale-while-revalidate
- Learn more about [Astro SSR](#)

## Static rendering

Statically rendered, or pre-rendered, Astro apps can be deployed to Vercel with zero configuration. To enable Vercel features like Image Optimization or Web Analytics, see [Using Vercel's features with Astro](#).

You can opt individual routes into static rendering with `export const prerender = true` as shown below:

```typescript
// src/pages/mypage.astro

export const prerender = true;
// ...
```

Statically rendered Astro sites on Vercel:

- Require zero configuration to deploy
- Can use Vercel features with `astro.config.ts`
- Learn more about [Astro Static Rendering](#)

## Serverless Functions

Serverless Functions use resources that scale up and down based on traffic demands. When you enable SSR with Astro's Vercel adapter, all of your routes will be server-rendered as Serverless Functions by default. Astro's Server Endpoints are the best way to define Serverless API routes with Astro on Vercel.

When defining an Endpoint, you must name each function after the HTTP method it represents. The following example defines basic HTTP methods in a Server Endpoint:

```typescript
// src/pages/methods.json.ts

import { APIRoute } from 'astro/dist/@types/astro';

export const GET: APIRoute = ({ params, request }) => {
  return new Response(
    JSON.stringify({
      message: 'This was a GET!',
    }),
  );
};

export const POST: APIRoute = ({ request }) => {
  return new Response(
    JSON.stringify({
      message: 'This was a POST!',
    }),
  );
};

export const DELETE: APIRoute = ({ request }) => {
  return new Response(
    JSON.stringify({
      message: 'This was a DELETE!',
    }),
  );
};

// ALL matches any method that you haven't implemented.
export const ALL: APIRoute = ({ request }) => {
  return new Response(
    JSON.stringify({
      message: `This was a ${request.method}!`,
    }),
  );
};
```

Serverless Functions with Astro on Vercel:

- Scale to zero when not in use
- Scale automatically as traffic increases
- Learn more about [Serverless Functions](#)

## Edge Functions

Edge Functions are a fast, scalable solution for delivering dynamic content to users

. By default, Edge Functions are deployed globally, and will be invoked in one of Vercel's Edge regions near your site's visitors.

Astro does not currently support Edge Functions natively, however you can use the `/api` directory to define Edge Functions with any framework on Vercel. See the [Edge Functions quickstart](#) to get started.

Edge Functions with Nuxt on Vercel:

- Offer cost savings by using fewer resources than Serverless Functions
- Can execute in the region nearest to your users or nearest to data sources they depend on, based on your configuration
- Have access to the geolocation and IP address of visitors, enabling location-based personalization
- Learn more about [Edge Functions](#)

## Image Optimization

Image Optimization helps you achieve faster page loads by reducing the size of images and using modern image formats. When deploying to Vercel, images are automatically optimized on demand, keeping your build times fast while improving your page load performance and Core Web Vitals.

Image Optimization with Astro on Vercel is supported out of the box with Astro's Image component. See the [Image Optimization quickstart](#) to learn more.

Image Optimization with Astro on Vercel:

- Requires zero-configuration for Image Optimization when using Astro's Image component
- Helps your team ensure great performance by default
- Keeps your builds fast by optimizing images on-demand
- Learn more about [Image Optimization](#)

## Middleware

Edge Middleware is code that executes before a request is processed on a site, enabling you to modify the response. Because it runs before the cache, Edge Middleware is an effective way to personalize statically generated content.

Astro middleware allows you to set and share information across your endpoints and pages with a `middleware.ts` file in your `src` directory. The following example edits the global locals object, adding data which will be available in any `.astro` file:

```typescript
// src/middleware.ts

// This helper automatically types middleware params
import { defineMiddleware } from 'astro:middleware';

export const onRequest = defineMiddleware(({ locals }, next) => {
  // intercept data from a request
  // optionally, modify the properties in `locals`
  locals.title = 'New title';

  // return a Response or the result of calling `next()`
  return next();
});
```

Astro middleware is not the same as Vercel's Edge Middleware, which has to be placed at the root directory of your project, outside `src`.

To add custom properties to locals in `middleware.ts`, you must declare a global namespace in your `env.d.ts` file:

```typescript
// src/env.d.ts

declare namespace App {
  interface Locals {
    title?: string;
  }
}
```

You can then access the data you added to locals in any `.astro` file, like so:

```typescript
// src/pages/middleware-title.astro

const { title } = Astro.locals;

<h1>{title}</h1>
<p>The name of this page is from middleware.</p>
```

### Deploying middleware at the Edge

You can deploy Astro's middleware at the Edge, giving you access to data in the `RequestContext` and `Request`, and enabling you to use Vercel's Edge Middleware helpers, such as `geolocation()` or `ipAddress()`.

To use Astro's middleware at the Edge, set `edgeMiddleware: true` in your `astro.config.ts` file:

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

If you're using Vercel's Edge Middleware, you do not need to set `edgeMiddleware: true` in your `astro.config.ts` file.

See Astro's [docs](#) on the limitations and constraints for using middleware at the Edge, as well as their troubleshooting tips.

### Using Astro.locals in Edge Middleware

The `Astro.locals` object exposes data to your `.astro` components, allowing you to dynamically modify your content with middleware. To make changes to `Astro.locals` in Astro's middleware at the edge:

1. Add a new middleware file next to your `src/middleware.ts` and name it `src/vercel-edge-middleware.ts`. This file name is required to make changes to `Astro.locals`. If you don't want to update `Astro.locals`, this step is not required.
2. Return an object with the properties you want to add to `Astro.locals`.

For TypeScript, you must install the `@vercel/edge` package:

```bash
pnpm i @vercel/edge
```

Then, type your middleware function like so:

```typescript
// src/vercel-edge-middleware.ts

import type { RequestContext } from '@vercel/edge';

// Note the parameters are different from standard Astro middleware
export default function ({
  request,
  context,
}: {
  request: Request;
  context: RequestContext;
}) {
  // Return an `Astro.locals` object with a `title` property
  return {
    title: "Spider-man's blog",
  };
}
```

### Using Vercel's Edge Middleware

Astro's middleware, which should be in `src/middleware.ts`, is distinct from Vercel Edge Middleware, which should be a `middleware.ts` file at the root of your project.

Vercel recommends using framework-native solutions. You should use Astro's middleware over Vercel's Edge Middleware wherever possible.

If you still want to use Vercel's Edge Middleware, see the [Quickstart](#) to learn how.

## Rewrites

Rewrites only work for static files with Astro. You must use Vercel's Edge Middleware for rewrites. You should not use `vercel.json` to rewrite URL paths with astro projects; doing so produces inconsistent behavior, and is not officially supported.

## Redirects

In general, Vercel recommends using framework-native solutions, and Astro has built-in support for redirects. That said, you can also do redirects with Vercel's Edge Middleware.

### Redirects in your Astro config

You can do redirects on Astro with `astro.config.ts` using the `redirects` config option as shown below:

```typescript
// astro.config.ts

import { defineConfig } from 'astro/config';

export default defineConfig({
  redirects: {
    '/old-page': '/new-page',
  },
});
```

### Redirects in Server Endpoints

You can also return a redirect from a Server Endpoint using the `redirect` utility:

```typescript
// src/pages/links/[id].ts

export async function GET({ params, redirect }): APIRoute {
  return redirect('/redirect-path', 307);
}
```

### Redirects in components

You can redirect from within Astro components with `Astro.redirect()`:

```typescript
// src/pages/account.astro

import { isLoggedIn } from '../utils';

const cookie = Astro.request.headers.get('cookie');

// If the user is not logged in, redirect them to the login page
if (!isLoggedIn(cookie)) {
  return Astro.redirect('/login');
}

<h1>You can only see this page while logged in</h1>
```

Certainly! Here is the provided documentation formatted in Markdown:

```markdown
# Serverless Functions

Serverless Functions use resources that scale up and down based on traffic demands. This makes them reliable during peak hours but low cost during slow periods.

When you enable SSR with Astro's Vercel adapter, all of your routes will be server-rendered as Serverless Functions by default. Astro's Server Endpoints are the best way to define Serverless API routes with Astro on Vercel.

When defining an Endpoint, you must name each function after the HTTP method it represents. The following example defines basic HTTP methods in a Server Endpoint:

```typescript
// src/pages/methods.json.ts

import { APIRoute } from 'astro/dist/@types/astro';

export const GET: APIRoute = ({ params, request }) => {
  return new Response(
    JSON.stringify({
      message: 'This was a GET!',
    }),
  );
};

export const POST: APIRoute = ({ request }) => {
  return new Response(
    JSON.stringify({
      message: 'This was a POST!',
    }),
  );
};

export const DELETE: APIRoute = ({ request }) => {
  return new Response(
    JSON.stringify({
      message: 'This was a DELETE!',
    }),
  );
};

// ALL matches any method that you haven't implemented.
export const ALL: APIRoute = ({ request }) => {
  return new Response(
    JSON.stringify({
      message: `This was a ${request.method}!`,
    }),
  );
};
```

Astro removes the final file during the build process, so the name of the file should include the extension of the data you want to serve (for example, `example.png.js` will become `/example.png`).

## Serverless Functions with Astro on Vercel:

- Scale to zero when not in use
- Scale automatically as traffic increases
- [Learn more about Serverless Functions](#)

# Edge Functions

Edge Functions are a fast, scalable solution for delivering dynamic content to users. By default, Edge Functions are deployed globally and will be invoked in one of Vercel's Edge regions near your site's visitors.

Astro does not currently support Edge Functions natively, however, you can use the `/api` directory to define Edge Functions with any framework on Vercel. See the Edge Functions quickstart to get started.

## Edge Functions with Nuxt on Vercel:

- Offer cost savings by using fewer resources than Serverless Functions
- Can execute in the region nearest to your users or nearest to data sources they depend on, based on your configuration
- Have access to the geolocation and IP address of visitors, enabling location-based personalization
- [Learn more about Edge Functions](#)

# Image Optimization

Image Optimization helps you achieve faster page loads by reducing the size of images and using modern image formats. When deploying to Vercel, images are automatically optimized on demand, keeping your build times fast while improving your page load performance and Core Web Vitals.

Image Optimization with Astro on Vercel is supported out of the box with Astro's Image component. See the Image Optimization quickstart to learn more.

## Image Optimization with Astro on Vercel:

- Requires zero-configuration for Image Optimization when using Astro's Image component
- Helps your team ensure great performance by default
- Keeps your builds fast by optimizing images on-demand
- [Learn more about Image Optimization](#)

# Middleware

Edge Middleware is code that executes before a request is processed on a site, enabling you to modify the response. Because it runs before the cache, Edge Middleware is an effective way to personalize statically generated content.

Astro middleware allows you to set and share information across your endpoints and pages with a `middleware.ts` file in your `src` directory. The following example edits the global locals object, adding data that will be available in any `.astro` file:

```typescript
// src/middleware.ts

// This helper automatically types middleware params
import { defineMiddleware } from 'astro:middleware';

export const onRequest = defineMiddleware(({ locals }, next) => {
  // intercept data from a request
  // optionally, modify the properties in `locals`
  locals.title = 'New title';

  // return a Response or the result of calling `next()`
  return next();
});
```

Astro middleware is not the same as Vercel's Edge Middleware, which has to be placed at the root directory of your project, outside `src`.

To add custom properties to locals in `middleware.ts`, you must declare a global namespace in your `env.d.ts` file:

```typescript
// src/env.d.ts

declare namespace App {
  interface Locals {
    title?: string;
  }
}
```

You can then access the data you added to locals in any `.astro` file, like so:

```typescript
// src/pages/middleware-title.astro

---
const { title } = Astro.locals;
---
<h1>{title}</h1>
<p>The name of this page is from middleware.</p>
```

## Deploying middleware at the Edge

You can deploy Astro's middleware at the Edge, giving you access to data in the RequestContext and Request and enabling you to use Vercel's Edge Middleware helpers, such as `geolocation()` or `ipAddress()`.

To use Astro's middleware at the Edge, set `edgeMiddleware: true` in your `astro.config.ts` file:

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

If you're using Vercel's Edge Middleware, you do not need to set `edgeMiddleware: true` in your `astro.config.ts` file.

See Astro's docs on the limitations and constraints for using middleware at the Edge, as well as their troubleshooting tips.

## Using Astro.locals in Edge Middleware

The `Astro.locals` object exposes data to your `.astro` components, allowing you to dynamically modify your content with middleware. To make changes to `Astro.locals` in Astro's middleware at the edge:

1. Add a new middleware file next to your `src/middleware.ts` and name it `src/vercel-edge-middleware.ts`. This file name is required to make changes to `Astro.locals`. If you don't want to update `Astro.locals`, this step is not required.

2. Return an object with the properties you want to add to `Astro.locals`.

   For TypeScript, you must install the `@vercel/edge` package:

   ```bash
   pnpm i @vercel/edge
   ```

   Then, type your middleware function like so:

   ```typescript
   // src/vercel-edge-middleware.ts

   import type { RequestContext } from '@vercel/edge';

   // Note the parameters are different from standard Astro middleware
   export default function ({
     request,
     context,
   }: {
     request: Request;
     context: RequestContext;
   }) {
     // Return an Astro.locals object with a title property
     return {
       title: "Spider-man's blog",
     };
   }
   ```

## Using Vercel's Edge Middleware

Astro's middleware, which should be in `src/middleware.ts`, is distinct from Vercel Edge Middleware, which should be a `

middleware.ts` file at the root of your project.

Vercel recommends using framework-native solutions. You should use Astro's middleware over Vercel's Edge Middleware wherever possible.

If you still want to use Vercel's Edge Middleware, see the Quickstart to learn how.

# Rewrites

Rewrites only work for static files with Astro. You must use Vercel's Edge Middleware for rewrites. You should not use `vercel.json` to rewrite URL paths with Astro projects; doing so produces inconsistent behavior and is not officially supported.

# Redirects

In general, Vercel recommends using framework-native solutions, and Astro has built-in support for redirects. That said, you can also do redirects with Vercel's Edge Middleware.

## Redirects in your Astro config

You can do redirects on Astro with `astro.config.ts` using the `redirects` config option as shown below:

```typescript
// astro.config.ts

import { defineConfig } from 'astro/config';

export default defineConfig({
  redirects: {
    '/old-page': '/new-page',
  },
});
```

## Redirects in Server Endpoints

You can also return a redirect from a Server Endpoint using the redirect utility:

```typescript
// src/pages/links/[id].ts

export async function GET({ params, redirect }): APIRoute {
  return redirect('/redirect-path', 307);
}
```

## Redirects in components

You can redirect from within Astro components with `Astro.redirect()`:

```typescript
// src/pages/account.astro

---
import { isLoggedIn } from '../utils';

const cookie = Astro.request.headers.get('cookie');

// If the user is not logged in, redirect them to the login page
if (!isLoggedIn(cookie)) {
  return Astro.redirect('/login');
}
---

<h1>You can only see this page while logged in</h1>
```

## Astro Middleware on Vercel:

- Executes before a request is processed on a site, allowing you to modify responses to user requests
- Runs on all requests but can be scoped to specific paths through a matcher config
- Uses Vercel's lightweight Edge Runtime to keep costs low and responses fast
- [Learn more about Edge Middleware](#)

# Caching

Vercel automatically caches static files at the Edge after the first request and stores them for up to 31 days on Vercel's Edge Network. Dynamic content can also be cached, and both dynamic and static caching behavior can be configured with Cache-Control headers.

The following Astro component will show a new time every 10 seconds. It does so by setting a 10-second max age on the contents of the page, then serving stale content while new content is being rendered on the server when that age is exceeded.

[Learn more about Cache Control options](#)

```typescript
// src/pages/ssr-with-swr-caching.astro

---
Astro.response.headers.set('Cache-Control', 's-maxage=10, stale-while-revalidate');
const time = new Date().toLocaleTimeString();
---

<h1>{time}</h1>
```

## CDN Cache-Control headers

You can also control how the cache behaves on any CDNs you may be using outside of Vercel's Edge Network with CDN Cache-Control Headers.

The following example tells downstream CDNs to cache the content for 60 seconds, and Vercel's Edge Network to cache it for 3600 seconds:

[Learn more about CDN Cache-Control headers](#)

```typescript
// src/pages/ssr-with-swr-caching.astro

---
Astro.response.headers.set('Vercel-CDN-Cache-Control', 'max-age=3600',);
Astro.response.headers.set('CDN-Cache-Control', 'max-age=60',);
const time = new Date().toLocaleTimeString();
---

<h1>{time}</h1>
```

[Learn more about CDN Cache-Control headers](#)

## Caching on Vercel:

- Automatically optimizes and caches assets for the best performance
- Requires no additional services to procure or set up
- Supports zero-downtime rollouts
- [Learn more about Caching](#)

# Speed Insights

Vercel Speed Insights provides you with a detailed view of your website's performance metrics, facilitating informed decisions for its optimization. By enabling Speed Insights, you gain access to the Speed Insights dashboard, which offers in-depth information about scores and individual metrics without the need for code modifications or leaving the dashboard.

To enable Speed Insights with Astro, see the Speed Insights quickstart.

To summarize, using Speed Insights with Astro on Vercel:

- Enables you to track traffic performance metrics, such as First Contentful Paint, or First Input Delay
- Enables you to view performance metrics by page name and URL for more granular analysis
- Shows you a score for your app's performance on each recorded metric, which you can use to track improvements or regressions
- [Learn more about Speed Insights](#)

# More benefits

See our [Frameworks documentation page](#) to learn about the benefits available to all frameworks when you deploy on Vercel.

# More resources

Learn more about deploying Astro projects on Vercel with the following resources:

- [Vercel CLI](#)
  Learn how to deploy your Astro project with Vercel CLI.
- [Serverless Function docs](#)
  Learn more about Vercel's SSR features.
- [Astro docs](#)
  See the full Astro documentation for information on their Vercel adapter.

Last updated on March 2, 2023
```

Feel free to customize the formatting as needed for your documentation.