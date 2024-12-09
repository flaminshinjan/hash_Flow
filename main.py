import os
from dotenv import load_dotenv
from agents.influencer_agent import create_influencer_agent

def main():
    load_dotenv()

    topic = input("Enter the topic: ").strip()

    if not topic:
        print("No topic provided. Exiting.")
        return

    try:
        influencer_agent = create_influencer_agent()
        print(f"\nPerforming initial web search for topic: {topic}")
        initial_search_query = f"Find top Instagram influencers related to {topic}"
        initial_output = influencer_agent.run(initial_search_query)
        if isinstance(initial_output, str):
            initial_influencers = [line.strip() for line in initial_output.split("\n") if line.strip()]
        else:
            initial_influencers = initial_output

        if not initial_influencers:
            print("\nNo influencers found in the initial search.")
            return
        niche_subtopic = f"Find more niche Instagram influencers specifically in {topic} focusing on a sub-niche."
        print(f"\nPerforming refined search: {niche_subtopic}")
        refined_output = influencer_agent.run(niche_subtopic)

        if isinstance(refined_output, str):
            refined_influencers = [line.strip() for line in refined_output.split("\n") if line.strip()]
        else:
            refined_influencers = refined_output
        all_influencers = list(set(initial_influencers + refined_influencers))

        if not all_influencers:
            print("\nNo influencers found after refinement.")
            return
        print("\nFinal List of Potential Instagram Profiles:")
        for idx, influencer in enumerate(all_influencers, start=1):
            print(f"{idx}. {influencer}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
