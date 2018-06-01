#!/usr/bin/env python
import argparse

from sitemapper import create_sitemaps

def main():

  parser = argparse.ArgumentParser(description='Create sitemap xml files.')

  parser.add_argument('--input-file', required=True, help='A newline delimited text file which contains URLS')
  parser.add_argument('--output-directory', required=True,
    help='The output directory into which sitemap and sitemap index files will be written')
  parser.add_argument('--change-freq', default='weekly', type=str)
  parser.add_argument('--max-urls-per-sitemap', default=45000, type=int)
  parser.add_argument('--sitemap-root', required=True, type=str)
  parser.add_argument('--pretty-print', action='store_true')

  args = parser.parse_args()

  create_sitemaps(
    args.sitemap_root,
    open(args.input_file).read().split("\n"),
    args.output_directory,
    max_urls_per_sitemap=args.max_urls_per_sitemap,
    changefreq=args.change_freq,
    pretty_print=args.pretty_print
    )


if __name__ == "__main__":
    main()
