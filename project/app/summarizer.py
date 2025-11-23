import nltk
import logging
from newspaper import Article
from newspaper.article import ArticleException
from app.models.tortoise import TextSummary

log = logging.getLogger(__name__)


async def generate_summary(summary_id: int, url: str) -> None:
    try:
        article = Article(url)
        article.download()
        article.parse()

        try:
            nltk.data.find("tokenizers/punkt_tab")
        except LookupError:
            log.info("Downloading NLTK punkt tokenizer...")
            nltk.download("punkt_tab")
        finally:
            article.nlp()

        summary = article.summary
        await TextSummary.filter(id=summary_id).update(summary=summary)
        log.info(f"Summary generated: ID={summary_id}, length={len(summary)} chars")
    except ArticleException as e:
        log.error(f"Failed to process article ID={summary_id}, URL={url}: {e}")
        await TextSummary.filter(id=summary_id).update(
            summary=f"Error: Could not process article - {str(e)}"
        )
    except Exception as e:
        log.error(
            f"Error generating summary ID={summary_id}, URL={url}: {e}", exc_info=True
        )
        await TextSummary.filter(id=summary_id).update(
            summary=f"Error: Failed to generate summary - {str(e)}"
        )
