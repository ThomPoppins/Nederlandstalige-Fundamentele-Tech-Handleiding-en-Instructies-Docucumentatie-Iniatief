#### Vercel offers built-in image optimization, automatically delivering the optimal image to your visitors. This feature is available on all plans.

Vercel streamlines the image optimization process, handling uploading, optimizing, and delivering images based on factors such as pixel density, format, size, and quality. Optimized images are cached on the Vercel Edge Network, ensuring swift delivery to users.

## Integration with Frameworks

Popular frameworks like Next.js, Astro, and Nuxt seamlessly integrate with Vercel's Image Optimization. The built-in components of these frameworks allow you to optimize images effortlessly.

For a live example demonstrating the usage with the `next/image` component, refer to the [Image Optimization demo](#link-to-demo).

## Getting Started

To start using Image Optimization with Next.js, Astro, or Nuxt, follow the [quickstart guide](#link-to-quickstart).

### Using the Build Output API

If you are building a custom web framework, you can implement Image Optimization using the Build Output API. Learn more in the [Build your own web framework blog post](#link-to-blog-post).

## Optimized URL Format

When utilizing the Images component in common frameworks and deploying your project on Vercel, the Image Optimization feature dynamically adjusts image URLs for different device screen sizes. For example:

- **Next.js:** `/next/image?url={link/to/my/image}&w=3840&q=75`
- **Nuxt.js or Astro:** `/_vercel/image?url={link/to/my/image}&w=3840&q=75`
- **Build Output API:** `/_vercel/image?url={link/to/my/image}&w=3840&q=75`

## Caching

Optimized images are automatically cached on the Vercel Edge Network, serving subsequent requests from the cache. Caching behavior differs for local and remote images.

### Local Images

- **Cache Key:**
  - Query string parameters:
    - `q`: Quality of the optimized image (1 to 100).
    - `w`: Width (in pixels) of the optimized image.
    - `url`: URL of the optimized image (content hash).

- **Local Image Cache Invalidation:**
  - Redeploying your app doesn't invalidate the image cache. To invalidate, replace the image with different content and redeploy.

- **Local Image Cache Expiration:**
  - Cached for up to 31 days on the Edge Network.

### Remote Images

- **Cache Key:**
  - Query string parameters same as local images.

- **Remote Image Cache Invalidation:**
  - Adding a query string to the image URL or configuring cache expiration serves a new image to visitors.

- **Remote Image Cache Expiration:**
  - Determined by `minimumCacheTTL` (default: 60 seconds) or `Cache-Control max-age` header from the upstream image.

## Limits, Pricing, and Performance Measurement

Refer to the [Limits and Pricing page](#link-to-limits-and-pricing) for details. Measure real-world performance using Speed Insights before and after adopting Image Optimization.

## Why Optimize Images on Vercel?

Optimizing images on Vercel provides several advantages:

- Enhanced website performance, user experience, and bandwidth savings.
- Improved Core Web Vitals, reduced bounce rates, and faster page loads.
- Properly sized images for different devices, support for modern formats like WebP and AVIF.
- Vercel manages the infrastructure for generating and caching optimized images at the Edge for quick responses.

## Related Information

For more information and guidance, explore the following articles:

- [Image Optimization Quickstart](#link-to-quickstart)
- [Managing Costs](#link-to-managing-costs)
- [Pricing](#link-to-pricing)

_Last updated on March 2, 2023._