from research_and_blog_crew.crew import ResearchAndBlogCrew


def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Analyze whether the demand for Data Analytics roles in the Indian job market is decreasing. Provide insights using recent hiring trends, industry reports, and market forecasts. Highlight key factors influencing demand, such as technology adoption, AI integration, and sector-specific needs. Conclude with a clear assessment of whether demand is declining, stable, or growing.',
    }

    try:
        ResearchAndBlogCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


