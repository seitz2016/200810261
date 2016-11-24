%%writefile my.xml
<?xml version="1.0" encoding="utf-8"?>
<wikimedia>
  <projects>
    <project name="Wikipedia" launch="2001-01-05">
      <editions>
        <edition language="English">en.wikipedia.org</edition>
        <edition language="German">de.wikipedia.org</edition>
        <edition language="French">fr.wikipedia.org</edition>
        <edition language="Polish">pl.wikipedia.org</edition>
        <edition language="Spanish">es.wikipedia.org</edition>
      </editions>
    </project>
    <project name="Wiktionary" launch="2002-12-12">
      <editions>
        <edition language="English">en.wiktionary.org</edition>
        <edition language="French">fr.wiktionary.org</edition>
        <edition language="Vietnamese">vi.wiktionary.org</edition>
        <edition language="Turkish">tr.wiktionary.org</edition>
        <edition language="Spanish">es.wiktionary.org</edition>
      </editions>
    </project>
  </projects>
</wikimedia>
import xml.etree.ElementTree as ET
tree=ET.parse('my.xml')
root=tree.getroot()
for i in root.getiterator():
import lxml
import lxml.etree
help(lxml.etree.parse)
tree=lxml.etree.parse('my.xml')
root=tree.getroot()
nodes=tree.xpath("/wikimedia/projects/project/@launch") 
len(nodes)
for node in nodes:
type(nodes)
%%HTML
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>My Home Page</title>
    <style>
        h1 {text-align: center;
           color:blue;
        };
    </style>
</head>
<body>
    <h1>안녕하십니까</h1>
    <p>오늘은 프로그래밍 하는 날...</p>
    <p>Today we do programming...</p>
</body>
</html>


