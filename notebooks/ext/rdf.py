import requests
import pandas as pd
from rdflib import Graph
from IPython.display import HTML, display

def query_endpoint(endpoint: str, query: str) -> pd.DataFrame:
    """
    Run a SPARQL query against a remote endpoint and return a pandas DataFrame.
    """
    headers = {"Accept": "application/sparql-results+json"}
    r = requests.post(endpoint, data={"query": query}, headers=headers)
    r.raise_for_status()
    data = r.json()
    cols = data["head"]["vars"]
    rows = [[row.get(c, {}).get("value") for c in cols] for row in data["results"]["bindings"]]
    
    df = pd.DataFrame(rows, columns=cols)
    
    # Convert columns to numeric datatype if possible
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except Exception:
            pass
    
    return df

def query_ttl(ttl: str, query: str) -> pd.DataFrame:
    """
    Run a SPARQL query against a turtle string and return a pandas DataFrame.
    """
    g = Graph()
    g.parse(data=ttl, format="turtle")
    res = g.query(query)
    cols = [str(v) for v in res.vars]
    rows = [[str(v) for v in r] for r in res]
    
    df = pd.DataFrame(rows, columns=cols)
    
    # Convert columns to numeric datatype if possible
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except Exception:
            pass
    
    return df

def display_result(df: pd.DataFrame):
    """
    Display a pandas DataFrame with clickable links in Jupyter.
    """
    df = HTML(df.to_html(render_links=True, escape=False))
    display(df)