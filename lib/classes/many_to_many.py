class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        object.__setattr__(self, '_title', title)
        self.author = author
        self.magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    def __setattr__(self, name, value):
        if name == 'title':
            return  # Ignore attempts to set title
        super().__setattr__(name, value)
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        object.__setattr__(self, '_name', name)

    @property
    def name(self):
        return self._name

    def __setattr__(self, name, value):
        if name == 'name':
            return  # Ignore attempts to set name
        super().__setattr__(name, value)

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass