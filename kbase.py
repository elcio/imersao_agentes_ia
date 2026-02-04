from agno.knowledge.knowledge import Knowledge
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.knowledge.embedder.openai import OpenAIEmbedder
from agno.db.sqlite import SqliteDb
from crawler import Crawler
from rich import print

knowledge = Knowledge(
    vector_db=LanceDb(
        uri="lancedb/knowledge1",
        table_name="visie",
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    ),
    contents_db=SqliteDb("kbase.visie.sqlite"),
)


if __name__ == "__main__":
    crawler = Crawler('https://visie.com.br/')
    data = crawler.crawl()
    for page in data:
        print('Indexing', page['url'])
        knowledge.insert(
            name=page['url'],
            text_content=f'# {page["title"]}\n\n{page["text"]}',
            metadata={
                'url': page['url'],
                'title': page['title'],
            }
        )
