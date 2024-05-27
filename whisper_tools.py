from crewai_tools import tool
from urllib import request, parse
import json


def retrieve_via_query(query: str) -> dict:
    """
    Query gene content from UniProt website.
    :param query: query to be searched in the UniProt website.
    :return: dict with full gene content from UniProt website.
    """
    encoded_query = parse.quote_plus(query)
    url = f'https://rest.uniprot.org/uniprotkb/search?query={encoded_query}'
    with request.urlopen(url) as r:
        resp = r.read().decode('utf-8').strip()
        resp = json.loads(resp)
        return resp


@tool("query_protein_name")
def query_protein_name(query: str) -> str:
    """
    Fetch protein name from UniProt website.
    :param query: query to be searched in the UniProt website.
    :return: protein name from search result.
    """
    resp = retrieve_via_query(query)
    if len(resp['results']) > 0:
        return resp['results'][0]['proteinDescription']['recommendedName']['fullName']['value']
    else:
        return "There is no information in UniProt website."


@tool("query_gene_sequence")
def query_gene_sequence(query: str) -> str:
    """
    Fetch gene sequence from UniProt website.
    :param query: query to be searched in the UniProt website.
    :return: gene sequence from search result.
    """
    resp = retrieve_via_query(query)
    if len(resp['results']) > 0:
        return resp['results'][0]['sequence']['value']
    else:
        return "There is no information in UniProt website."


@tool("query_gene_functions")
def query_gene_functions(query: str) -> str:
    """
    Fetch gene function list from UniProt website.
    :param query: query to be searched in the UniProt website.
    :return: string of gene function list from search result.
    """
    resp = retrieve_via_query(query)
    if len(resp['results']) > 0:
        cross_references = resp['results'][0]['uniProtKBCrossReferences']
        go_properties = [one_ref['properties'][0]['value'].split(':')[-1] for one_ref in cross_references
                         if one_ref['database'] == 'GO' and len(one_ref['properties']) > 0]
        return str(go_properties)
    else:
        return "There is no information in UniProt website."
