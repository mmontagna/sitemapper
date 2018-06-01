# Sitemapper

A utility for generating sitemaps from a list of URLs.

## Installation

```
pip install sitemapper
```

## Usage

```
sitemapper --input-file URLs.txt --output-directory out --change-freq weekly --max-urls-per-sitemap 50000 --sitemap-root https://example.com --pretty-print
```


## Sample output

```
<?xml version='1.0' encoding='utf-8'?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap>
    <loc>https://marcomontagna.com/sitemap0.xml</loc>
  <lastmod>2018-06-01T19:02:17.440168</lastmod>
  </sitemap>
<sitemap>
    <loc>https://marcomontagna.com/sitemap1.xml</loc>
  <lastmod>2018-06-01T19:02:17.440168</lastmod>
</sitemap>
</sitemapindex>
```

```
<?xml version='1.0' encoding='utf-8'?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
    <loc>https://marcomontagna.com/</loc>
    <changefreq>weekly</changefreq>
    </url>
  <url>
    <loc>https://marcomontagna.com/blog.html</loc>
    <changefreq>weekly</changefreq>
  </url>
</urlset>
```
