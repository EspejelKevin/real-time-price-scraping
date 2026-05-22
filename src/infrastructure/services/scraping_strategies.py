from bs4 import BeautifulSoup
from lxml import etree

from abc import ABC, abstractmethod


class ExtractionStrategy(ABC):
    @abstractmethod
    def extract(self, html_content: str, selector: str) -> float:
        raise NotImplementedError
    
    def _clean_price(self, text: str) -> float:
        price_text = text.replace('$', '').replace(',', '').strip()
        return float(price_text)
    

class CSSExtractionStrategy(ExtractionStrategy):
    def extract(self, html_content: str, selector: str) -> float:
        soup = BeautifulSoup(html_content, 'html.parser')
        element = soup.select_one(selector)

        if not element:
            raise ValueError(f'Selector CSS no encontrado: {selector}')
        
        return self._clean_price(element.text)
    

class XPathExtractionStrategy(ExtractionStrategy):
    def extract(self, html_content: str, selector: str) -> float:
        parser = etree.HTMLParser()
        tree = etree.fromstring(html_content, parser)
        elements = tree.xpath(selector)

        if not elements:
            raise ValueError(f"Selector XPath no encontrado: {selector}")
        
        text = elements[0] if isinstance(elements[0], str) else elements[0].text
        return self._clean_price(text)


class MetaTagExtractionStrategy(ExtractionStrategy):
    def extract(self, html_content: str, selector: str) -> float:
        """
        Para MetaTags, el 'selector' suele ser el nombre de la propiedad.
        Ejemplo: 'id=price' o 'property=og:price:amount'
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        # Buscamos dinámicamente un tag <meta> que cumpla con el atributo enviado
        # Ejemplo: selector = "property='product:price:amount'"
        element = soup.find("meta", attrs={selector.split('=')[0].strip(): selector.split('=')[1].strip().replace("'", "").replace('"', "")})
        
        if not element or not element.get("content"):
            raise ValueError(f"MetaTag no encontrado para el atributo: {selector}")
        
        return self._clean_price(element["content"])
