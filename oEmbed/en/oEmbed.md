oEmbed is a format that allows an embedded representation of a URL on third-party sites. This simple API enables a website to display embedded content, such as photos or videos, when a user posts a link to that resource, without needing to parse the resource directly.

This document is stored on GitHub.

## Table Of Contents

1. [Quick Example](#quick-example)
2. [Full Spec](#full-spec)
3. [Security Considerations](#security-considerations)
4. [Discovery](#discovery)
5. [More Examples](#more-examples)
6. [Authors](#authors)
7. [Implementations](#implementations)

---

### 1. Quick Example

A consumer (e.g., WordPress) makes the following HTTP request:

```http
http://www.flickr.com/services/oembed/?format=json&url=http%3A//www.flickr.com/photos/bees/2341623661/
```

The provider (e.g., Flickr) then responds with an oEmbed response:

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

This allows the consumer to turn a URL to a Flickr photo page into structured data to allow embedding of that photo on the consumer's website.

### 2. Full Spec

#### 2.1. Configuration

Configuration for oEmbed is straightforward. Providers must specify URL scheme and API endpoint pairs. For instance:

- URL scheme: `http://www.flickr.com/photos/*`
- API endpoint: `http://www.flickr.com/services/oembed/`

...and more details are provided regarding URL schemes and API endpoints.

#### 2.2. Consumer Request

Details about the parameters required for a consumer request are provided: `url`, `maxwidth`, `maxheight`, and `format`.

#### 2.3. Provider Response

Details about JSON and XML response formats, response parameters, response types (photo, video, link, rich), and errors are provided.

### 3. Security Considerations

Security-related recommendations are provided for URL scheme filtering and handling HTML to avoid XSS attacks.

### 4. Discovery

Instructions for making oEmbed support discoverable by adding `<link>` elements to HTML documents or using Link headers are detailed.

### 5. More Examples

Two examples (video and link) along with their request and response details are given.

### 6. Authors

The list of authors and their contact details are provided.

### 7. Implementations

Lists of providers, consumers, and libraries supporting oEmbed are detailed with their respective links.

---

Press and Links

- The official oEmbed mailing list
- Webmonkey tutorial
- Leah's blog
- ajaxian

This document is stored on GitHub. Please check the mailing list, fork, and contribute.
Certainly! Continuing from where we left off:
### 7. Implementations (Continued)

#### 7.3. Libraries (Continued)

More libraries supporting oEmbed:

- Django: [micawber](https://github.com/coleifer/micawber)
- Java: [java-oembed](https://github.com/michael-simons/java-oembed)
- .Net: [oEmbed API Wrapper](http://oembed.codeplex.com/)
- JQuery: [oEmbed API Wrapper](https://github.com/starfishmod/jquery-oembed-all)
- Node.js: [oEmbed API Gateway](https://github.com/itteco/iframely)
- Elixir: [furlex](https://github.com/claytongentry/furlex)
- Elixir: [elixir-oembed](https://github.com/r8/elixir-oembed)

#### Press and Links (Continued)

Links to resources related to oEmbed:

- The official oEmbed mailing list
- [Webmonkey tutorial](#)
- [Leah's blog](#)
- [ajaxian](#)

---

Feel free to adjust the content or add more information as needed.