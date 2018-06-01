import os
from datetime import datetime
import xml.etree.cElementTree as ET

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def indent(elem, level=0):
    i = "\n" + level*"  "
    j = "\n" + (level-1)*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = j
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = j
    return elem        


def create_sitemap_index(sitemap_root, sitemap_files, output_file, pretty_print=False):
  now = datetime.utcnow().date().isoformat()
  sitemapindex = ET.Element("sitemapindex", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
  for sitemap_file in sitemap_files:
    sitemap_node = ET.SubElement(sitemapindex, "sitemap")
    loc = ET.SubElement(sitemap_node, "loc").text = "{}/{}".format(sitemap_root.rstrip('/'), os.path.split(sitemap_file)[-1])
    lastmod = ET.SubElement(sitemap_node, "lastmod").text = now
  tree = ET.ElementTree(sitemapindex)
  if pretty_print:
    indent(sitemapindex, level=0)
  print("Writing sitemapindex to {}".format(output_file))
  tree.write(output_file, xml_declaration=True, encoding='utf-8', method="xml")


def create_sitemap(urls, output_file, changefreq='weekly', pretty_print=False):
  now = datetime.utcnow().date().isoformat()
  urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
  for url in urls:
    url_node = ET.SubElement(urlset, "url")
    loc = ET.SubElement(url_node, "loc").text = url
    changefreq = ET.SubElement(url_node, "changefreq").text = changefreq
  tree = ET.ElementTree(urlset)
  if pretty_print:
    indent(urlset, level=0)
  print("Writing sitemap to {}".format(output_file))
  tree.write(output_file, xml_declaration=True, encoding='utf-8', method="xml")
  return output_file

def create_sitemaps(sitemap_root, urls, output_directory, max_urls_per_sitemap=45000, changefreq='weekly', pretty_print=False):
  """
  sitemap_root: The path where sitemaps will be served from eg http://example.com/
  urls: a list of urls.
  output_directory: The directory into which we'll store sitemaps and index files, it must not exist.
  max_urls_per_sitemap: The max number of files to store per sitemap file (typically should be less than 50k)
  changefreq: Create sitemap entries with changefreq equal to this.
  """
  if os.path.exists(output_directory):
    print('Output directory {} already exists exiting.'.format(output_directory))
    exit(1)
  else:
    os.mkdir(output_directory)
  i = 0
  sitemap_files = []
  for url_chunk in chunks(urls, max_urls_per_sitemap):
    sitemap_file = os.path.join(output_directory, 'sitemap{}.xml'.format(i))
    create_sitemap(url_chunk, sitemap_file, changefreq=changefreq, pretty_print=pretty_print)
    sitemap_files.append(sitemap_file)
    i += 1
  sitemapindex = os.path.join(output_directory, 'sitemapindex.xml')
  create_sitemap_index(sitemap_root, sitemap_files, sitemapindex, pretty_print=pretty_print)
