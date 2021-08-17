import os
import argparse

class CitramanikOptions:
    def __init__(self):
        parser = argparse.ArgumentParser("citramanik-qt", description="Citramanik: More Export, Less Effort!")
        parser.add_argument('inputfile', default="", nargs='?', action='store',
                help="SVG file to be processed")
        parser.add_argument('-o', dest='outputdir', action='store', default=os.path.expanduser("~/"),
                help="Output directoy name to save your exported files")
        parser.add_argument('-p', dest='pattern', action='store',
                help="ID pattern to be processed, i.e: icon -> it will export all objects \
                    which have object id prefixed with icon")
        parser.add_argument('--jpg', dest='with_jpg', action='store_true',
                help="Export to JPG format")
        parser.add_argument('--png', dest='with_png', action='store_true',
                help="Export to PNG Format")
        parser.add_argument('--eps', dest='with_eps', action='store_true',
                help="Export to EPS format")
        parser.add_argument('--pdf', dest='with_pdf', action='store_true',
                help="Export to PDF")
        parser.add_argument('--svg', dest='with_svg', action='store_true',
                help="Export to optimized SVG")
        parser.add_argument('--booklet', dest='with_booklet', action='store_true',
                help="Export to PDF with multiple page (Booklet)")
        parser.add_argument('--webp', dest='with_webp', action='store_true',
                help="Export to WEBP format")
        parser.add_argument('--colorspace', choices=['rgb', 'cmyk'], dest='colorspace', action='store', default='rgb',
                help="Use CMYK colorspace for JPG, PDF, EPS, or booklet format")
        parser.add_argument('--with-zip', dest='with_zip', action='store_true',
                help="Zip all exported files based on its name")
        parser.add_argument('--dpi', type=int, dest='dpi', action='store', default=96,
                help="DPI for PNG/JPG/PDF, default value is 96")
        parser.add_argument('--quality', type=int, dest='quality', action='store', default=90,
                help="Compression quality for JPG export, default value is 90")
        parser.add_argument('--inkscape-path', dest='inkscape_path', action='store', 
                help="Inkscape Path")
        parser.add_argument('--gs-path', dest='ghostscript_path', action='store', 
                help="Ghostscript Path")
        parser.add_argument('--pngquant-path', dest='pngquant_path', action='store', 
                help="Optipng Path")
        parser.parse_known_args(namespace=self)

    def __repr__(self):
        return str(self.__dict__)
