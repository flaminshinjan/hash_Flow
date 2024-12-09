import os
from langchain.agents import initialize_agent, Tool
from langchain_community.chat_models import ChatOpenAI
from utils.search_util import search_influencers
from utils.instagram_api import get_recent_posts_by_username

def create_influencer_agent():
    """
    Create an agent that has two tools:
    - WebSearch: to find influencers related to a given topic.
    - FetchInstagramPosts: to verify or fetch posts of an influencer's handle.
    """
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY is not set in the environment.")

    llm = ChatOpenAI(model="gpt-4", temperature=0.7)
    def web_search(query):
        return search_influencers(query)

    def fetch_instagram_posts(username):
        data = get_recent_posts_by_username(username)
        if not isinstance(data, dict):
            return []
        if "data" not in data or not isinstance(data["data"], list):
            return []
        return [post.get("caption", "") for post in data["data"] if isinstance(post, dict)]

    tools = [
        Tool(
            name="WebSearch",
            func=web_search,
            description="Search the web for top influencers in the given topic. Input: topic or related search query.",
        ),
        Tool(
            name="FetchInstagramPosts",
            func=fetch_instagram_posts,
            description="Given an Instagram username, fetch recent posts to verify or explore their content.",
        ),
    ]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent="zero-shot-react-description",
        verbose=True,
        max_iterations=5,
        max_execution_time=60,
    )
    return agent
