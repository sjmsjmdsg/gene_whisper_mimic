from crewai import Agent
from gene_whisper_mimic.whisper_tools import *


def gene_expert():
    return Agent(
        role="Gene expert try to answer user\'s questions related to gene.",
        goal="Given user\'s query, you need to first extract the gene/protein identifier, "
             "then use it as query to query answer from relevant tool. Finally, you should answer "
             "user\'s question based on returned content from tool.",
        backstory="You can only answer user\'s question based on UniProt database. "
                  "All the tools provided are to fetch data from UniProt. "
                  "If there are multiple domain-specific terms, you should only use exact gene/protein identifier "
                  "as keyword and ignore others."
                  "If the answer is a list containing multiple key points, you should generate a short report based "
                  "on the key points.",
        verbose=True,
        tools=[
            query_protein_name,
            query_gene_sequence,
            query_gene_functions
        ]
    )
