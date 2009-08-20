# Copyright 2009 Jason Stitt
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from distutils.core import setup

longdesc = """\
A new Python wrapper for tidylib_, which allows
you to convert slightly invalid HTML/XHTML markup into valid markup. E.g. this
will correct unescaped ampersands, some unclosed tags, missing elements,
missing attributes, etc. Tidylib is highly configurable; it can output HTML or
XHTML, and perform other functions such as converting named entities to numeric
entities (named entities work only along with an HTML or XHTML doctype;
numeric entities work in generic XML data).

Note 1: The SourceForge download mirror has been corrected.

Note 2: Unfortunately, neither this library, nor uTidyLib, nor a barebones
test case seems to work with the prepackaged tidy.dll on Windows. Until this
is fixed, this is a Linux/BSD/OS X/Cygwin library.

Trivial example of use::

    from tidylib import tidy_document
    document, errors = tidy_document('''<p>f&otilde;o <img src="bar.jpg">''',
        options={'numeric-entities':1})
    print document
    print errors
    
For documentation see the `pytidylib project page`_
    
.. _tidylib: http://tidy.sourceforge.net/
.. _`pytidylib project page`: http://countergram.com/software/pytidylib/
"""

setup(
    name="pytidylib",
    version="0.1.2",
    description="New Python wrapper for tidylib",
    long_description=longdesc,
    author="Jason Stitt",
    author_email="js@jasonstitt.com",
    url="http://countergram.com/software/pytidylib/",
    download_url="https://sourceforge.net/projects/pytidylib/files/pytidylib-0.1.2.tar.gz/download",
    packages=['tidylib'],
    classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Other Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Natural Language :: English',
          'Topic :: Utilities',
          'Topic :: Text Processing :: Markup :: HTML',
          'Topic :: Text Processing :: Markup :: XML',
          ],
    )

