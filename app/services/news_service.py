import httpx
from app.utils import NEWS_API_KEY, NEWS_API_URL
from datetime import datetime, timedelta

def get_news_data(city:str):
    curr_date = datetime.today().date()
    week_ago = curr_date - timedelta(weeks=4)
    query = f"{city} AND (weather OR storm OR rainfall OR climate OR temperature OR forecast)"

    
    url = f"{NEWS_API_URL}?q={query}&from={week_ago}&sortBy=publishedAt&apiKey={NEWS_API_KEY}"

    try:
        res = httpx.get(url, timeout=10)
        res.raise_for_status()
        print(res.status_code)

        data = res.json()

        weather_keywords = ["weather","climate", "rainfall","temperature","forecast","storm"]
        filtered_articles = [article for article in data.get("articles",[]) 
                             if any(keyword.lower() in article["title"].lower() for keyword in weather_keywords)]

        return filtered_articles
    except httpx.HTTPStatusError as e:
        return {"Error: " f"Failed to fetch data: {e.response.status_code} {e.response.text}"}
    except httpx.RequestError as e:
        return {"Error: " f"Request failed: {str(e)}"}