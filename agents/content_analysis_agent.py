import os
from dotenv import load_dotenv
from agents.influencer_agent import create_influencer_agent

def main():
    load_dotenv()

    topic = input("Enter the topic: ")

    try:
        influencer_agent = create_influencer_agent(topic)
        print("Discovering influencers...")
        raw_output = influencer_agent.run(topic)

        if isinstance(raw_output, str):
            influencers = [line.strip() for line in raw_output.split("\n") if line.strip()]
        else:
            influencers = raw_output

        print("\nFinal Answer: Some of the top influencers on Instagram include:")
        for idx, influencer in enumerate(influencers, start=1):
            print(f"{idx}. {influencer}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
